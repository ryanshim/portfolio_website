from flask import Flask, render_template, request, json
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='yourEmailHere',
        MAIL_PASSWORD='yourPassHere'
        )
mail = Mail(app)

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
                            gitPrj1Name="Portfolio Website")

@app.route('/contact/')
def contact():
    return render_template("contactForm.html",
                            title="Contact Me",
                            paragraph="This is the contact me page; website in production")

@app.route('/sendMail/', methods=["GET", "POST"])
def handleRequests():
    userEmail = request.form["inputEmail"]
    userText = request.form["inputText"]

    if request.method == "POST":
        sendMail(userEmail, userText)
        return render_template("result.html", userText=userText, userEmail=userEmail)
    else:
        return render_template("result.html", userText="F", userEmail="F")

def sendMail(userEmail, userText):
    try:
        msg = Message("New website contact message",
                sender="sendEmailToYourself",
                recipients=["sendEmailToYourself"])
        msg.body = userText
        mail.send(msg)
        return "Mail Sent"

    except Exception, e:
        return str(e)

if __name__ == "__main__":
    app.run()
