from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    user_name = request.form["name"]
    user_password = request.form["password"]
    return render_template("login.html", name=user_name, password=user_password)

if __name__ == "__main__":
    app.run(debug=True)
