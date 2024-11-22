from flask import Flask, render_template, request
from hl7apy.parser import parse_message
import time, webbrowser
import multiprocessing

app = Flask(__name__)

def open_browser():
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:5000')

def validate_message(message):
    message = message.strip('"\n').replace('\n', '\r') # match char to separate segments
    _, errors, warnings = parse_message(message, force_validation=True, return_errors=True)
    errors = [f"Error: {e}" for e in errors]
    warnings = [f"Warning: {warning}" for warning in warnings]
    output = errors + warnings
    return '\n'.join(output)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    user_input = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input:
            try:
                output = validate_message(user_input)
            except Exception as e: # caught any exception when parsing the message
                output = f"Error: {e}"
        else:
            output = ""
    return render_template("index.html", output=output, user_input=user_input)

if __name__ == "__main__":
    multiprocessing.freeze_support()
    multiprocessing.Process(target=open_browser).start()
    app.run()
