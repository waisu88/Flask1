from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index.html", name=name, content=["Tim","joe", "Jack"])

if __name__ == "__main__":
    app.run()

