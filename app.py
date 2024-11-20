from flask import Flask, render_template, request

app = Flask(__name__)

def validate_message(text):
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        message = request.form.get("user_input")
        if message:
            output = validate_message(message)
        else:
            output = "Input is invalid. Please enter something."
    return render_template("index.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)
