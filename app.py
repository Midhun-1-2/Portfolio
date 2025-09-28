from flask import Flask, render_template
from flask_mail import Mail
from datetime import datetime


app = Flask(__name__)





mail = Mail(app)
@app.route("/")
def home():
    current_year = datetime.now().year
    # Passing first 3 blog posts as preview on home page
    return render_template("index.html")







if __name__ == "__main__":
    app.run(debug=True)
