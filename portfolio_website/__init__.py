import sqlite3
import collections
import json
from flask import Flask, render_template, request
from flask_mail import Mail, Message

#################
#### GLOBALS ####
#################
DATABASE = '/var/www/portfolio_website/portfolio_website/static/data/tle.db'
#DATABASE = './static/data/tle.db'   # delete before commit

############################
#### FLASK EMAIL CONFIG ####
############################
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

####################
### PAGE ROUTES ####
####################
# MAIN PAGE
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

# PROJECTS PAGE
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

# CESIUM PAGE
@app.route('/sat_track/')
def ces_track():
    dict_tle = {} 

    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()

    for row in c.execute('SELECT * FROM tles'):
        dict_tle[row[0]] = [row[1], row[2]]

    conn.close()

    # JSON doesn't accept escape characters
    for k,v in dict_tle.items():
        dict_tle[k] = [v[0].strip('\r'), v[1].strip('\r')]

    return render_template('cesiumPage.html', 
            tle_data=json.dumps(dict_tle))

# CONTACT PAGE (FORM)
@app.route('/contact/')
def contact():
    return render_template("contactForm.html",
            title="CONTACT ME",
            paragraph="This is the contact me page; website in production")

# EMAIL SENT CONFIRMATION PAGE
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

##########################
#### HELPER FUNCTIONS ####
##########################
# EMAIL HELPER FUNCTION
def sendMail(userEmail, userText):
    try:
        msg = Message("New website contact message from: " + str(userEmail),
                sender=userEmail,
                recipients=["xxxxxxxxxx"])
        msg.body = userText
        mail.send(msg)
        return "Mail Sent"

    except Exception as e:
        return str(e)

############################
#### APP RUN AND GUARDS ####
############################
if __name__ == "__main__":
    app.run()
