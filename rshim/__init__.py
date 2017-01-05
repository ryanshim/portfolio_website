from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    with app.open_resource('static/aboutMe.txt') as f:
        aboutMe = f.read().split('\n')
    return render_template("main.html",
                            title="Ryan Shim",
                            paragraph="Website in production!",
                            bio=aboutMe,
                            gitLink="https://github.com/ryanshim",
                            gitLogo="static/images/GitHub-Mark-64px.png",
                            linkedInLink="https://www.linkedin.com/in/ryan-shim-2a119a1a",
                            linkedInLogo="static/images/linkedIn.png")

@app.route('/projects/')
def projects():
    return render_template("project.html",
                            title="Projects",
                            paragraph="This is the projects page; website in production",
                            gitPrj1="https://github.com/ryanshim/portfolio_website/",
                            gitPrj1Name="Portfolio Website",
                            home="Return to homepage")

@app.route('/contact/')
def contact():
    return render_template("contactForm.html",
                            title="Contact Me",
                            paragraph="This is the contact me page; website in production",
                            home="Return to homepage")

if __name__ == "__main__":
    app.run()
