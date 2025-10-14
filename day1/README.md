# walmart_LLM_Desing_Model_APIs_14thOct2025

### Basic intro to GenAI 

<img src="gen1.png">

### any LLM is massively trained on public / private data as well

<img src="gen2.png">

### LLM model understanding with data 

<img src="gen3.png">


## any AI tools for Developer / tester ..etc 

<img src="gen4.png">


### github copilot modes 

<img src="gen5.png">


### creating directory and install flask in codespace 

```
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025 (master) $ mkdir  webapp-python
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025 (master) $ python -V
Python 3.12.1
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025 (master) $ pip install flask 
Collecting flask
  Downloading flask-3.1.2-py3-none-any.whl.metadata (3.2 kB)
Collecting blinker>=1.9.0 (from flask)

```
### running python flask code 

```
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025 (master) $ ls
README.md  day1  day2  day3  webapp-python
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025 (master) $ cd webapp-python/
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025/webapp-python (master) $ ls
ashu.py
@redashu ➜ /workspaces/walmart_LLM_Desing_Model_APIs_14thOct2025/webapp-python (master) $ python  ashu.py 
 * Serving Flask app 'ashu'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.0.0.230:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 134-685-345
127.0.0.1 - - [14/Oct/2025 17:30:26] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [14/Oct/2025 17:30:27] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [14/Oct/2025 17:30:50] "GET /json HTTP/1.1" 200 -

```


https://reimagined-journey-r4gv7x45g6f5744.github.dev/


https://reimagined-journey-r4gv7x45g6f5744-5001.app.github.dev/


### sample app.py code 

```
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/json")
def hello_json():
    return jsonify(message="Hello, World!")

# create /home route which must run index.html in templates folder
@app.route("/home")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    # Bind to 0.0.0.0 so the container/devcontainer host can reach it
    app.run(host="0.0.0.0", port=5001, debug=True)
```
