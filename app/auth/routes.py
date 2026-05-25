from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, current_user
from urllib.parse import urlsplit

from app.auth import auth
from app.auth.forms import LoginForm, RegisterForm
from app.models import User, db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(db.select(User).where(User.email == form.email.data))
        if user is None or not user.check_password(form.password.data):
            flash('Geçersiz e-posta veya şifre.', 'error')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('main.index')
        flash('Başarıyla giriş yaptınız.', 'success')
        return redirect(next_page)
    
    return render_template('auth/login.html', title='Giriş Yap', form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Kayıt işleminiz başarıyla tamamlandı. Artık giriş yapabilirsiniz!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', title='Kayıt Ol', form=form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('Başarıyla çıkış yaptınız.', 'success')
    return redirect(url_for('main.index'))
