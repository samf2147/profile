from flask import Flask, render_template, redirect, url_for
import os

#global constants, including URLs
BASE_URL = 'http://localhost:5000/'
RESUME_PATH = 'resources/resume.pdf'
# RESUME_PATH = '/resources/resume.pdf'

app = Flask(__name__)

@app.route('/')
@app.route('/home/')
def home():
    return render_template('home.html')

@app.route('/personal/')
def personal():
    return render_template('personal.html')

@app.route('/resume/')
def resume():
    return redirect(url_for('static',filename=RESUME_PATH))

if __name__ == '__main__':
    app.run(debug=True)