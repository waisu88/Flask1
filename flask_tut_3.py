from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/test")
def test():
    return render_template("new.html")

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

