from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    with app.open_resource('static/aboutMe.txt') as f:
        aboutMe1 = f.readline()
        aboutMe2 = f.readline()
        aboutMe3 = f.readline()
        aboutMe4 = f.readline()
    return render_template("main.html", title="Ryan Shim", paragraph="Website in production!", bio1=aboutMe1, bio2=aboutMe2, bio3=aboutMe3, bio4=aboutMe4)

@app.route('/projects/')
def projects():
    return render_template("project.html", title="Projects Completed", paragraph="This is the projects page; website in production", home="Return to homepage")

@app.route('/contact/')
def contact():
    return render_template("contactForm.html", title="Contact Me", paragraph="This is the contact me page; website in production", home="Return to homepage")

if __name__ == "__main__":
    app.run()
