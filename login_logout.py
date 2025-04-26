import base64
from flask import *
import os
from datetime import datetime
from functools import wraps
from models import get_connecttion

app = Flask(__name__)
app.secret_key = 'Randon1234khkjhkjhkjhkjhkjstuwqqwe'
@app.route('/')
def index():
    print("i am here")
    return render_template('mainlogin.html')





@app.route('/log', methods=['GET', 'POST'])
def login():
    e = None
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']
        # passwd = base64.b64encode(password_form)
        try:
            con = get_connecttion()
            cur = con.cursor()
            cur.execute("SELECT COUNT(1) FROM users WHERE username = '%s'" % username_form) # CHECKS IF USERNAME EXSIST
            if cur.fetchone()[0]:
                cur.execute("SELECT password FROM users WHERE username = '%s'" % username_form) # FETCH THE HASHED PASSWORD
                for row in cur.fetchall():
                    if password_form == row[0]:
                        session['logged_in'] = True
                        session['STU'] = True
                        session['username'] = username_form
                        user1 = username_form.upper()

                        return render_template('home_new.html', user=user1)
                    else:
                        e = "Invalid Credential"
                        return render_template('mainlogin.html', error=e)
            else:
                e = "Invalid Credential"
                return render_template('mainlogin.html', error=e)
        except Exception as e:

            return render_template('mainlogin.html', error=e)
  
  
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first')
            return redirect(url_for('index'))
    return wrap


@app.route('/password', methods=["post"])
def password():
    if request.method == 'POST':
        username_form = request.form['username']
        # password_form = request.form['password']
        # passwd = base64.b64encode(password_form)
        try:
            con = get_connecttion()
            cur = con.cursor()
            cur.execute("SELECT COUNT(1) FROM users WHERE username = '%s'" % username_form) # CHECKS IF USERNAME EXSIST
            if cur.fetchone()[0]:
                passw = cur.execute("SELECT password FROM users WHERE username = '%s'" % username_form)  # FETCH THE HASHED PASSWORD
                flash(f"Password is {passw.fetchone()[0]}")
                return render_template('mainlogin.html')

            else:
                e = "Invalid Credential"
                return render_template('mainlogin.html', error=e)
        except Exception as e:
            flash(f"Error: {e}")
            return render_template('mainlogin.html')

@app.route('/signup')
def sign_up():
    return render_template('signupMODI.html')
@app.route("/adduseraction", methods=["post"])
def add_user_action():
    # global first_name, last_name, email
    if request.form:
        user_name = request.form['usernamesignup']
        password = request.form['passwordsignup']
        # email = request.form['emailsignup']
        # passwd = base64.b64encode(password)
    query = "insert into users values (0,'%s','%s')"
    query = query % (user_name, password)
    try:
        dcn = get_connecttion()
        cur = dcn.cursor()
        cur.execute(query)
        dcn.commit()
        return render_template('Sucess.html', user=user_name )
    except Exception as e:
        e = "{} is already a user. Please use another username.".format(user_name)
        return render_template('signupMODI.html', err = e)
@app.route('/forgot')
def forgot():
    return render_template('password.html')
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You logged out successfully!!")
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def server_error(e):
    flash("OOPS! Something went wrong.. Please login again OR contact System Admin")
    return render_template('mainlogin.html')

if __name__ == '__main__':
    app.run(port=5050 , debug=False)

