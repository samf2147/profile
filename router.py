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
#     return redirect('static/resources/Samuel_Frank_Resume.pdf')
    return redirect(url_for('static',filename=RESUME_PATH))
#     return app.send_static_file(os.path.join('static',RESUME_PATH))
    
    
    #Why doesn't this work?
    #return redirect(str(request.host) + 'Samuel_Frank_Resume.pdf')

# resume_path = 'static/resources/Samuel_Frank_Resume.pdf'
# app.add_url_rule('/resume/', resume_path, build_only=True)


# @app.route('/resume/')
# def resume():
#     resume_path = 'static/resources/Samuel_Frank_Resume.pdf'
#     
    
#     with open(resume_path,'r') as resume:
#         response = make_response(resume)
#         response.headers['Content-Type'] = 'application/pdf'
#         response.headers['Content-Disposition'] = \
#                 'inline; filename={}.pdf'.format(resume_path)
#         return response
    
    #return render_template('resume.xml')

if __name__ == '__main__':
    app.run(debug=True)