from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
	return render_template("index.html", title="Test Title", paragraph="This is a file transfer test; website in production!")

if __name__ == "__main__":
    app.run()
