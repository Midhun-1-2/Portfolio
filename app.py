from flask import Flask, render_template, request, redirect, url_for , flash
from flask_mail import Mail, Message
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = "midhun@123"


app.config['MAIL_USERNAME'] = os.getenv('kk8004419@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('pcjv stvs tveu urcb')

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kk8004419@gmail.com'      # Your email
app.config['MAIL_PASSWORD'] = 'pcjv stvs tveu urcb'         # Use app password, not your real password
app.config['MAIL_DEFAULT_SENDER'] = 'kk8004419@gmail.com'

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
