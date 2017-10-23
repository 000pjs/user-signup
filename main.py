from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/signup')
def display_signup_form():
    template = jinja_env.get_template('signup-form.html')
    return template.render()

@app.route('/signup', methods=['POST'])
def user_submission():

    username = request.form['user-name']
    password = request.form['password']
    verify_password = request.form['verify-password']

    username_error = ''
    password_error = ''

    if username == '':
        username_error = 'Please enter a username'
        username = ''
    else:
        for char in username:
            if char < 3 or char > 20 or char == '':
                username_error = 'Your username must be between 4 - 19 characters & may not contain spaces.'
                username = ''

    if password or varify_password == '':
        password_error = 'Please enter a password.'
        password = ''
    else:
        if password != verify_password:
            password_error = 'Your passwords do not match.'
            minutes = ''

    if not username_error and not password_error:
        return redirect('/welcome')
    else:
        template = jinja_env.get_template('signup_form.html')
        return template.render(username_error=username_error,
            password_error=password_error,
            username=username)


@app.route("/welcome", methods=['POST'])
def welcome():
    username = request.form['user-name']
    template = jinja_env.get_template('welcome.html')
    return template.render(username=user-name)


app.run()