from flask import render_template, redirect, request, url_for, flash
from . import auth
from .forms import LoginForm, RegistrationForm
from flask.ext.login import login_user, login_required, logout_user, current_user
from ..models import User, db
from ..email import send_email

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('账户或密码错误。')
    return render_template('auth/login.html',form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user();
    flash('成功登出')
    return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('现在您可以登录了')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.before_app_request
def before_request():
    if current_user.is_authenticated():
        current_user.ping()
        if not current_user.confirmed and request.endpoint[:5]!='auth.':
            return redirect(url_for('auth.unconfirmed'))