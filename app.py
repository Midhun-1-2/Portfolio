from flask import Flask, render_template, request, redirect, url_for , flash
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)


# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'kk8004419@gmail.com'      # Your email
app.config['MAIL_PASSWORD'] = 'kmnx xlyb eqxo bebi'         # Use app password, not your real password
app.config['MAIL_DEFAULT_SENDER'] = 'your_email@gmail.com'

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



@app.route("/contact1", methods=["POST"])
def contact1():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    # Compose email
    msg = Message(
        subject=f"New Contact Form Submission from {name}",
        sender=email,
        recipients=["kk8004419@gmail.com"],  # Your receiving email
        body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
    )

    try:
        mail.send(msg)
        flash("Message sent successfully!", "success")
        return redirect(url_for("home", success=1))
    except Exception as e:
        print(f"Error sending email: {e}")
        flash("Something went wrong. Please try again later.", "danger")
        return redirect(url_for("home", error=1))



if __name__ == "__main__":
    app.run(debug=True)
