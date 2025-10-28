from flask import Flask, render_template, request, redirect, url_for, jsonify
import os
import json
import re

# Create Flask app and ensure templates/static are served from my-flask-app/templates & my-flask-app/static
app = Flask(__name__, template_folder="templates", static_folder="static")

# Static credentials (example)
VALID_USERNAME = "admin"
VALID_PASSWORD = "Secret123"

# Load feedback dataset from static/data/feedback.json at startup
_FEEDBACK_PATH = os.path.join(app.static_folder, "data", "feedback.json")
_feedback_data = []
if os.path.exists(_FEEDBACK_PATH):
    try:
        with open(_FEEDBACK_PATH, "r", encoding="utf-8") as f:
            _feedback_data = json.load(f)
    except Exception:
        _feedback_data = []

def _find_relevant_feedback(user_text, limit=4):
    """
    Simple keyword matching to find relevant feedback entries.
    Returns up to `limit` matching items (most matches first).
    """
    text = (user_text or "").lower()
    if not text:
        return []

    # split into words, ignore very short terms
    terms = [t for t in re.findall(r"\w+", text) if len(t) > 2]

    # score each feedback by number of matching terms in product_name, category, and review_text
    scored = []
    for item in _feedback_data:
        hay = " ".join([
            str(item.get("product_name", "")).lower(),
            str(item.get("category", "")).lower(),
            str(item.get("review_text", "")).lower()
        ])
        score = sum(hay.count(t) for t in terms)
        if score > 0:
            scored.append((score, item))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [it for _, it in scored[:limit]]

@app.route("/")
def index():
    # render the templates/index.html file
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    GET:
      - If no query params -> show login form.
      - If username/password provided as query params (form method=GET) -> process them.
    POST:
      - Process credentials from form data.
    On success -> render welcome.html (chatbot UI).
    On failure -> redirect back to login page.
    """
    # get credentials from POST form or GET query params
    if request.method == "POST":
        username = (request.form.get("username") or "").strip()
        password = request.form.get("password") or ""
    else:
        # GET
        username = request.args.get("username")
        password = request.args.get("password")
        # if no credentials provided, render the login form
        if not username and not password:
            return render_template("login.html")

    # simple credential check against static values
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        # render the welcome.html template (chatbot UI)
        return render_template("welcome.html", username=username)

    # failed login -> redirect back to login page
    return redirect(url_for("login"))

@app.route("/chat", methods=["POST"])
def chat():
    """
    Chat endpoint used by the client-side chatbot UI.
    Expects JSON: { "message": "<user text>" }
    Returns JSON: { "reply": "<bot reply>" }
    """
    data = request.get_json(force=True, silent=True) or {}
    user_text = (data.get("message") or "").strip()
    if not user_text:
        return jsonify({"reply": "Please send a question or message."})

    # find relevant feedback entries
    matches = _find_relevant_feedback(user_text, limit=4)

    if matches:
        # build a concise reply that references found feedback entries
        reply_lines = []
        reply_lines.append("I found some customer feedback related to your query:")
        for m in matches:
            prod = m.get("product_name", "Unknown product")
            rating = m.get("rating", "n/a")
            snippet = (m.get("review_text") or "")[:140]
            reply_lines.append(f"- {prod} (rating: {rating}): \"{snippet}\"")
        reply_lines.append("Ask for more details about any product above, or ask about returns, shipping, or common issues.")
        reply = "\n".join(reply_lines)
        return jsonify({"reply": reply})

    # fallback generic responses using simple keyword checks
    lt = user_text.lower()
    if "return" in lt or "refund" in lt:
        return jsonify({"reply": "Most items can be returned within the seller's return window. Check the product's return policy on its page for exact details."})
    if "shipping" in lt or "deliver" in lt:
        return jsonify({"reply": "Shipping times depend on the seller and selected shipping method. Orders often show estimated delivery dates at checkout."})
    if "price" in lt or "cost" in lt or "discount" in lt:
        return jsonify({"reply": "Prices vary by seller and promotions. For best deals, check the product page and active coupons or clearance sections."})

    # final fallback
    return jsonify({"reply": "I don't have a direct match in the feedback dataset. You can ask about returns, shipping, pricing, or include a product name."})

if __name__ == "__main__":
    # Bind to 0.0.0.0 so the dev container exposes the server to the host
    app.run(host="0.0.0.0", port=5000, debug=True)