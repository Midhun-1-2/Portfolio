from flask import Flask, render_template, request, redirect, url_for , flash
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Projects data - add your own projects here
projects = [
    {
        "title": "Personal Portfolio Website",
        "description": "A fully responsive portfolio site built with Flask and modern CSS.",
        "link": "#"
    },
    {
        "title": "AI Chatbot",
        "description": "An AI-powered chatbot using Python and machine learning.",
        "link": "#"
    },
    {
        "title": "DSA Practice Tracker",
        "description": "A tool to track daily problem-solving progress and performance.",
        "link": "#"
    }
]

# Blog posts data
posts = [
    {
        "id": 1,
        "title": "My Journey into Software Development After Graduation",
        "content": "Graduating in 2023 with a B.Tech degree, I began a focused journey into full-stack web development and problem-solving..."
    },
    {
        "id": 2,
        "title": "How AI is Reshaping Software Development",
        "content": "Artificial Intelligence isn’t just for research labs anymore. It’s impacting how we write code and build systems..."
    },
    {
        "id": 3,
        "title": "Top 5 Platforms I Use to Upskill as a Developer",
        "content": "As a tech enthusiast, I’m always learning. These are the platforms I rely on for continuous upskilling..."
    }
]
app.secret_key = "your_secret_key"  # For flash messages

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
    return render_template("index.html", projects=projects, posts=posts, current_year=current_year)

@app.route("/blog")
def blog():
    # Full blog listing page
    return render_template("blog.html", posts=posts)



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
