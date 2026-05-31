from flask import render_template
from app.errors import errors
from app.models import db

@errors.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html', title='Sayfa Bulunamadı'), 404

@errors.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html', title='Sistemsel Hata'), 500
