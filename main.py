from flask import Flask, request, redirect, render_template 


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return redirect('/signup')

@app.route('/signup', methods=['POST', 'GET'])
def user_submission():
   
    if request.method == 'POST':
    
        username = request.form['username']
        password = request.form['password']
        verify_password = request.form['verify_password']
        email = request.form['email']

        username_error = ''
        password_error = ''
        ver_error = ''
        email_error = ''

        
       
        if ' ' in username or username == '':
            username_error = 'invalid username.'
        
           
        else:
            if len(username) > 20 or len(username) < 3:
                username_error = 'username must be between (4-19) characters.'
             
                
        
        if ' ' in password or password == '':
            password_error = 'invalid password.' 
            password = ''
        
        elif len(password) > 20 or len(password) < 3:
                password_error = 'password must be between (4-19) characters.'
        
        elif verify_password == '':
            ver_error = 'please verify password' 
        
        else:
            if password != verify_password:
                ver_error = 'passwords do not match.'
                password = ''
                verify_password = ''

    

        if email != '':
            at_count = 0
            dot_count = 0
            if (len(email) > 20 or len(email) < 3):
                email_error = 'email must be between (4-19) characters.'
            for i in email:
                if i == ' ':
                    email_error = 'email cannot contain spaces.'
                elif i == '@':
                    at_count = at_count + 1
                elif i == '.':
                    dot_count = dot_count + 1
            if at_count > 1 or at_count < 1:
                email_error = 'invalid email.'
            if dot_count > 1 or dot_count < 1:
                email_error = 'invalid email.'


            
        if not username_error and not password_error and not ver_error and not email_error:
            return render_template('welcome.html', username=username, email=email)

        else:  
            return render_template('signup-form.html', username=username, username_error=username_error, password=password, verify_password=verify_password, password_error=password_error, ver_error=ver_error, email=email, email_error=email_error)
 
    else:
        return render_template('signup-form.html')




if __name__ == '__main__':
    app.run()