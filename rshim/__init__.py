from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.update(
        DEBUG=True,
        #EMAIL SETTINGS
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME='xxxxxxxxxx',
        MAIL_PASSWORD='xxxxxxxxxx'
        )
mail = Mail(app)

# main page
@app.route('/')
def homepage():
    with app.open_resource('static/textFiles/aboutMe.txt', 'r') as f:
        aboutMe = f.read().split('\n')
    return render_template("main.html",
            title="RYAN SHIM",
            paragraph="Website in production!",
            bio=aboutMe,
            gitLink="https://github.com/ryanshim",
            gitLogo="static/images/GitHub-Mark-Light-64px.png",
            resumeLink="static/textFiles/resume.pdf",
            resumeIcon="static/images/resumeIcon1.png",
            linkedInLink="https://www.linkedin.com/in/ryan-shim-2a119a1a",
            linkedInLogo="static/images/In-White-66px-TM.png")

# projects page
@app.route('/projects/')
def projects():
    with app.open_resource('static/textFiles/abtPortfolioWebsite.txt', 'r') as f1:
        data1 = f1.read().split('\n')
    with app.open_resource('static/textFiles/abtSatTracker.txt', 'r') as f2:
        data2 = f2.read().split('\n')
    return render_template("project.html",
            title="PROJECTS",
            paragraph="This is the projects page; website in production",
            gitPrj1="https://github.com/ryanshim/portfolio_website/",
            gitPrj1Name="Portfolio Website",
            gitPrj1Desc=data1,
            gitPrj2="https://github.com/ryanshim/sat_tracker/",
            gitPrj2Name="Satellite Tracker",
            gitPrj2Desc=data2,
            gitPrj3="https://github.com/ryanshim/dataStructuresAlgo/",
            gitPrj3Name="Data Structures and Algorithms (c++)",
            pyEphemLink="http://rhodesmill.org/pyephem/",
            sgp4Link="https://pypi.python.org/pypi/sgp4/")

# contact page (form)
@app.route('/contact/')
def contact():
    return render_template("contactForm.html",
            title="CONTACT ME",
            paragraph="This is the contact me page; website in production")

# message sent confirmation page
@app.route('/sendMail/', methods=["GET", "POST"])
def handleRequests():
    userEmail = request.form["inputEmail"]
    userText = request.form["inputText"]

    if request.method == "POST":
        sendMail(userEmail, userText)
        return render_template("result.html",
                confirm="Message sent! I will get back to you shortly!",
                backHome="Click here to go back to the homepage.")
    else:
        return render_template("result.html",
                confirm="Message failed to deliver")

def sendMail(userEmail, userText):
    try:
        msg = Message("New website contact message from: " + str(userEmail),
                sender="xxxxxxxxxx",
                recipients=["xxxxxxxxxx"])
        msg.body = userText
        mail.send(msg)
        return "Mail Sent"

    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run()
