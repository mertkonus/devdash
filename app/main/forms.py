from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class NoteForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired(message='Başlık alanı zorunludur.')])
    content = TextAreaField('İçerik', validators=[DataRequired(message='İçerik alanı zorunludur.')])
    submit = SubmitField('Kaydet')

class TaskForm(FlaskForm):
    title = StringField('Görev Adı', validators=[DataRequired(message='Görev adı zorunludur.')])
    description = TextAreaField('Açıklama')
    submit = SubmitField('Ekle')

class ProfileForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[DataRequired(message='Kullanıcı adı zorunludur.')])
    email = StringField('E-Posta', validators=[DataRequired(message='E-posta zorunludur.'), Email(message='Geçerli bir e-posta giriniz.')])
    picture = FileField('Profil Resmi Güncelle', validators=[FileAllowed(['jpg', 'png', 'jpeg'], 'Sadece JPG, PNG veya JPEG resim dosyaları eklenebilir!')])
    submit = SubmitField('Güncelle')
