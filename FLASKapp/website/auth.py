from flask import Blueprint,render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import random
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.objects(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('LOGGED in successfully', category='Success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password,please try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.objects(email=email).first()
        if user:
            flash('Email already exists.',  category='error')
        elif len(email) < 4:
            flash('Email is too short, must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('firstName is too short, must be greater than 1 characters.', category='error')
        elif password1 != password2 :
            flash('passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('password is too short, must be greater than 6 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method="sha256"),user_id=random.randint(0, 123453) )
            new_user.save()
            flash('Account created!', category='success')
            user = User.objects(email=email).first()
            if user is None:
                return redirect(url_for('auth.login'))
            else:
                login_user(user, remember=True,)
                return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user)