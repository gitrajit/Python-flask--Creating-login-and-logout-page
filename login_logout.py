import base64
from flask import *
import os
from datetime import datetime
from functools import wraps
import MySQLdb

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainlogin.html')


@app.route('/log', methods=['GET', 'POST'])
def login():
    e = None
    if request.method == 'POST':
        username_form = request.form['username']
        password_form = request.form['password']
        passwd = base64.b64encode(password_form)
        try:
            dcn, cur = get_connecttion()
            cur.execute("SELECT COUNT(1) FROM user WHERE user_name = %s;", [username_form]) # CHECKS IF USERNAME EXSIST
            if cur.fetchone()[0]:
                cur.execute("SELECT password FROM user WHERE user_name = %s;", [username_form]) # FETCH THE HASHED PASSWORD
                for row in cur.fetchall():
                    if passwd == row[0]:
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
        except (MySQLdb.Error, MySQLdb.Warning) as e:

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
 
 
 @app.route('/signup')
def sign_up():
    return render_template('signupMODI.html')
 @app.route("/adduseraction", methods=["post"])
def add_user_action():
    # global first_name, last_name, email
    if request.form:
        user_name = request.form['usernamesignup']
        password = request.form['passwordsignup']
        email = request.form['emailsignup']
        passwd = base64.b64encode(password)
    query = "insert into user values (0,'%s','%s','%s')"
    query = query % (user_name, passwd, email)
    try:
        dcn, cur = get_connecttion()
        cur.execute(query)
        dcn.commit()
        return render_template('Sucess.html', user=user_name )
    except (MySQLdb.Error, MySQLdb.Warning) as e:
        e = "{} is already a user. Please use another username.".format(user_name)
        return render_template('signupMODI.html', err = e)

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
    app.run(port=10 , debug=False)

