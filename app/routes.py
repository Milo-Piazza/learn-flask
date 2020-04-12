from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import LoginForm

posts = []

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html.j2", posts=posts)

@app.route('/about')
def about():
    return render_template("about.html.j2", title="My blog")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data,
            form.remember_me.data
        ))
        return redirect(url_for("home"))
    return render_template("login.html.j2", form=form)

@app.route('/register')
def register():
    return redirect(url_for("home"))
