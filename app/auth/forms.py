from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User, db

class LoginForm(FlaskForm):
    email = StringField('E-posta', validators=[DataRequired(message='E-posta alanı zorunludur.'), Email(message='Geçerli bir e-posta adresi giriniz.')])
    password = PasswordField('Şifre', validators=[DataRequired(message='Şifre alanı zorunludur.')])
    remember_me = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')

class RegisterForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(message='Kullanıcı adı alanı zorunludur.')])
    email = StringField('E-posta', validators=[DataRequired(message='E-posta alanı zorunludur.'), Email(message='Geçerli bir e-posta adresi giriniz.')])
    password = PasswordField('Şifre', validators=[DataRequired(message='Şifre alanı zorunludur.')])
    confirm_password = PasswordField('Şifreyi Doğrula', validators=[DataRequired(message='Şifre doğrulama alanı zorunludur.'), EqualTo('password', message='Şifreler eşleşmelidir.')])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, username):
        user = db.session.scalar(db.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Lütfen farklı bir kullanıcı adı seçin, bu isim zaten kullanılıyor.')

    def validate_email(self, email):
        user = db.session.scalar(db.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Lütfen farklı bir e-posta adresi kullanın, bu adres zaten kayıtlı.')
