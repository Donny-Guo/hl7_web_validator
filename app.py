from flask import Flask, render_template, request
from hl7apy.parser import parse_message
from datetime import datetime
import os, threading, time, webbrowser

app = Flask(__name__)

def open_browser():
    time.sleep(2)
    webbrowser.open('http://127.0.0.1:5000')

def validate_message(message, output_dir="output/"):
    os.makedirs(output_dir, exist_ok=True) # create directory if not existed
    message = message.strip('"\n').replace('\n', '\r')
    current_time = datetime.now()
    formatted_date = current_time.strftime("%Y%m%d%H%M%S")
    report_file = output_dir + formatted_date + ".txt"
    parse_message(message, force_validation=True, report_file=report_file)
    with open(report_file, 'r') as file:
        output = ""
        # Read each line in the file and put it in the string output
        for line in file:
            output = output + line.strip() + "\n"
    return output

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
                output = e
        else:
            output = ""
    return render_template("index.html", output=output, user_input=user_input)

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run(debug=True)
