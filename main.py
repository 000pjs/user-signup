from flask import Flask, request, redirect, render_template 


app = Flask(__name__)
app.config['DEBUG'] = True

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

        if ' ' in username or username == '':
            username_error = 'invalid username.'
        
           
        else:
            if len(username) > 20 or len(username) < 3:
                username_error = 'username must be between (4-19) characters.'
             
                
        
        if ' ' in password or password == '':
            password_error = 'invalid password.' 
            password = ''
        elif verify_password == '':
            ver_error = 'please verify password' 
        else:
            if password != verify_password:
                ver_error = 'passwords do not match.'
                password = ''
                verify_password = ''
               
            
        if not username_error and not password_error and not ver_error:
            return render_template('welcome.html', username=username)

        else:  
            return render_template('signup-form.html', username=username, username_error=username_error, password=password, verify_password=verify_password, password_error=password_error, ver_error=ver_error, email=email)
 
    else:
        return render_template('signup-form.html')




if __name__ == '__main__':
    app.run()