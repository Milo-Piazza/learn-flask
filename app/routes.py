from app import app, db
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app.forms import LoginForm, RegistrationForm
from app.models import User

posts = []

@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template("home.html.j2", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html.j2", title="My blog")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            return redirect(url_for("home"))
        return redirect(next_page)
    return render_template("login.html.j2", form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("You have successfully registered!")
        return redirect(url_for("home"))
    return render_template("register.html.j2", form=form)
