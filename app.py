from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/projects")
def projects():
    return render_template('projects.html')

app.run(debug = True)