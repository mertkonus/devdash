from flask import Flask

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Veritabanı ve eklentilerin init edilmesi
    
    # Blueprint kayıtları
    from app.main import main as main_bp
    app.register_blueprint(main_bp)

    from app.auth import auth as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
