# DevDash

Kişisel Not ve Görev Takip Sitesi. Bu proje İnternet Programcılığı dersi için geliştirilmiştir.

## Teknolojiler
- Flask 3.x
- Flask-SQLAlchemy, Flask-Migrate
- Flask-Login, Flask-WTF
- Python 3

## Kurulum
1. Repoyu klonlayın.
2. Sanal ortam oluşturup aktif edin: `python -m venv venv` ve `venv\Scripts\activate` (Windows için)
3. Gereksinimleri yükleyin: `pip install -r requirements.txt`
4. `.env.example` dosyasını `.env` olarak kopyalayın ve içerisindeki değişkenleri kendi ortamınıza göre ayarlayın.
5. Veritabanını oluşturun: `flask db upgrade` (Migrasyonlar eklendiğinde kullanılacak)
6. Uygulamayı çalıştırın: `python run.py`
