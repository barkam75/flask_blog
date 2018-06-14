from flask_blog import app
from flask import render_template, redirect, url_for, session,request

from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required

import bcrypt


@app.route('/login', methods=('GET','POST'))
def login():
    form = LoginForm()
    error = None
    #Check if login page has been an effect of redirection from other page
    if request.method == 'GET' and request.args.get('next'):
        #Save redirection for post login action
        session['next'] = request.args.get('next', None)
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=form.username.data,
            ).first()
        if author:
            #Interesting stuff you hash form data with salt of author password
            #in order to compare two hashed passwords
            if bcrypt.hashpw(form.password.data,author.password)==author.password:
                #If login was successful save username to the session
                session['username']=form.username.data
                session['is_author']=author.is_author
                if 'next' in session:
                    #If session has set next field perform return back after login
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
                else:
                    return redirect(url_for('login_success'))
            else:#Otherwise return error message
                error = "Incorrect username and password"
        else:#Otherwise return error message
            error = "Incorrect username and password"
    return render_template('author/login.html', form=form, error=error)
    
@app.route('/register', methods=('GET','POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    return render_template('author/register.html', form=form)

@app.route('/success')
def success():
    return "Author registered"
    
@app.route('/login_success')
@login_required
def login_success():
    return "Author logged in"
    
@app.route('/logout')
def logout():
    session.pop('username')
    session.pop('is_author')
    return redirect(url_for('index'))
