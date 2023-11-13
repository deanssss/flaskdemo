from flask import Blueprint
from flask import request, flash, redirect, url_for, render_template
from flask_login import login_user, login_required, logout_user
from model.user import User

auth = Blueprint("auth", __name__, url_prefix="/auth")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash("Invalid input.")
            return redirect(url_for('auth.login'))

        user = User.query.first()
        if username == user.username and user.validate_password(password):
            login_user(user)
            flash('Login success.')
            return redirect(url_for('index'))

        flash('Invalid username or password.')
        return redirect(url_for('auth.login'))
    return render_template('login.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye.')
    return redirect(url_for('index'))