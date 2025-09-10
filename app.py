from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/")
def home():
    current_year = datetime.now().year
    # Passing first 3 blog posts as preview on home page
    return render_template("index.html", projects=projects, posts=posts, current_year=current_year)

@app.route("/blog")
def blog():
    # Full blog listing page
    return render_template("blog.html", posts=posts)

@app.route("/contact", methods=["POST"])
def contact():
    # Basic contact form handling (print to console)
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    print(f"New message from {name} ({email}): {message}")
    # Redirect to home page with a success message (optional)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
