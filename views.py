from flask import Blueprint, render_template

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("base.html")

@views.route("/login")
def login():
    return render_template("login.html")

@views.route("/logout")
def logout():
    return render_template("logout.html")