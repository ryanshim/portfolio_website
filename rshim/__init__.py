from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    aboutMe = open("./longTexts/aboutMe.txt", "r")
    line = aboutMe.read()
    return render_template("main.html", title="Ryan Shim", paragraph="Website in production!", about=line)

@app.route('/projects/')
def projects():
    return render_template("project.html", title="Projects Completed", paragraph="This is the projects page; website in production", home="Return to homepage")

@app.route('/contact/')
def contact():
    return render_template("contactForm.html", title="Contact Me", paragraph="This is the contact me page; website in production", home="Return to homepage")

if __name__ == "__main__":
    app.run()
