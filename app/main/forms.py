from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    title = StringField('Başlık', validators=[DataRequired(message='Başlık alanı zorunludur.')])
    content = TextAreaField('İçerik', validators=[DataRequired(message='İçerik alanı zorunludur.')])
    submit = SubmitField('Kaydet')

class TaskForm(FlaskForm):
    title = StringField('Görev Adı', validators=[DataRequired(message='Görev adı zorunludur.')])
    description = TextAreaField('Açıklama')
    submit = SubmitField('Ekle')
