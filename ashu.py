from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'walmart_secret_key_2025'  # For session management

# Static user credentials
USERS = {
    'admin': 'admin123',
    'user': 'user123'
}

# Predefined chatbot responses
CHATBOT_RESPONSES = {
    'hello': 'Hello! I am BLU, your Walmart assistant. How can I help you today?',
    'hi': 'Hi there! How can I assist you?',
    'help': 'I can help you with product information, store locations, and general queries.',
    'products': 'We have a wide range of products including electronics, groceries, clothing, and more.',
    'store': 'We have stores located across the country. What location are you interested in?',
    'hours': 'Most of our stores are open from 8 AM to 10 PM. Store hours may vary by location.',
    'return': 'We have a flexible return policy. You can return most items within 90 days of purchase.',
    'contact': 'You can contact us at 1-800-WALMART or through our website contact form.',
    'bye': 'Goodbye! Have a great day!',
    'thanks': 'You\'re welcome! Is there anything else I can help you with?',
    'thank you': 'You\'re welcome! Feel free to ask if you need anything else.'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/chatbot')
def chatbot():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('chatbot.html')

@app.route('/chat', methods=['POST'])
def chat():
    if 'username' not in session:
        return jsonify({'error': 'Not authenticated'}), 401
    
    data = request.get_json()
    user_message = data.get('message', '').lower().strip()
    
    # Find matching response
    response = 'I\'m sorry, I don\'t understand that. Can you please rephrase?'
    for key in CHATBOT_RESPONSES:
        if key in user_message:
            response = CHATBOT_RESPONSES[key]
            break
    
    return jsonify({'response': response})

@app.route('/user-details')
def user_details():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session.get('username')
    role = 'Admin' if username == 'admin' else 'User'
    
    return render_template('user_details.html', username=username, role=role)

@app.route('/json')
def json_page():
    return render_template('json_page.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
