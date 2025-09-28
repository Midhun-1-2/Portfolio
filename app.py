from flask import Flask, render_template, request, redirect, url_for , flash
from flask_mail import Mail, Message
from datetime import datetime


app = Flask(__name__)





mail = Mail(app)
@app.route("/")
def home():
    current_year = datetime.now().year
    # Passing first 3 blog posts as preview on home page
    return render_template("index.html")

@app.route("/blog")
def blog():
    # Full blog listing page
    return render_template("blog.html")





if __name__ == "__main__":
    app.run(debug=True)
