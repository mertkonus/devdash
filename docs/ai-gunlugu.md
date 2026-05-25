# Yapay Zeka Günlüğü (AI Günlüğü)

## Oturum: 1
**Tarih:** 23 Mayıs 2026  
**Mod:** Plan  
**Model:** Gemini 3.1 Pro  
**Görünüm:** Manager  
**Hedef:** Proje iskeleti kurulumu

### Neler Yapıldı?
- Projenin Application Factory ve Blueprint'lere uygun klasör hiyerarşisi oluşturuldu.
- `requirements.txt`, `.gitignore`, `config.py` ve `run.py` dosyaları kök dizine eklendi.
- Flask 3.x versiyon kısıtlamasıyla gerekli paketler tanımlandı (`flask`, `flask-sqlalchemy`, `flask-migrate`, `flask-login`, `flask-wtf`, `python-dotenv`, `pytest`).
- `app`, `app/main`, `app/auth` ve `tests` dizinlerine Python paketi olmaları için `__init__.py` dosyaları yerleştirildi.
- `templates`, `static` ve `migrations` klasörlerinin içleri boş kalacak şekilde `.gitkeep` dosyalarıyla projenin dizin yapısına eklendi.
- Projenin amacını, teknolojilerini ve kurulum adımlarını açıklayan sade ve Türkçe bir `README.md` dosyası oluşturuldu.
- Bu dosya (AI Günlüğü) ilgili rubriğe uygun olarak başlatıldı.

## Oturum: 2
**Tarih:** 24 Mayıs 2026
**Mod:** Plan
**Model:** Gemini 3.1 Pro
**Görünüm:** Manager
**Hedef:** Veritabanı mimarisi ve SQLAlchemy 2.x modellerinin kurulması

### Neler Yapıldı?
- Projenin veri saklama altyapısını oluşturmak üzere hocanın rubrikte zorunlu kıldığı "en az 3 ilişkili tablo" kısıtlamasına uygun bir mimari planlandı.
- Kullanıcıların sistemde barınabilmesi için `User`, kullanıcıya ait verilerin tutulması için ise `Note` (Notlar) ve `Task` (Görevler) tabloları belirlendi.
- Rubrikteki en kritik ceza maddelerinden biri olan eski stil `db.Column` kullanımı tamamen pas geçildi; tüm tablolar modern SQLAlchemy 2.x standartlarına uygun olarak `Mapped[]` ve `mapped_column()` yapılarıyla esnek şekilde kodlandı.
- Güvenlik kısıtlarına tam uyum sağlamak adına, kullanıcı şifrelerinin veritabanında kabak gibi açık metin olarak saklanmasının önüne geçildi. `werkzeug.security` kütüphanesi entegre edilerek şifrelerin hashlenmiş (kriptolanmış) olarak tutulması için model içerisine `set_password` ve `check_password` metotları yazıldı.
- İleride yapılacak olan oturum açma / üyelik işlemleri altyapısına hazırlık olması için `User` modeline `flask_login` kütüphanesinden `UserMixin` sınıfı başarıyla miras olarak eklendi.
- Tablolar arası ilişkilerde rubriğe uygun olarak bire-çok (One-to-Many) mantığı kuruldu; her bir notun ve görevin mutlaka bir kullanıcıya ait olması zorunlu tutularak `user_id` Foreign Key (yabancı anahtar) bağlantıları yapıldı.
- `db = SQLAlchemy()` nesnesi `app/models.py` dosyasında temiz bir şekilde tanımlandı ve ileride ana uygulama fabrikasında (`create_app`) çağrılmak üzere hazırlandı.

## Oturum: 3
**Tarih:** 25 Mayıs 2026
**Mod:** Plan
**Model:** Gemini 3.1 Pro
**Görünüm:** Manager
**Hedef:** Kayıt ve Giriş Akışının (Auth) Python Backend Altyapısının Kurulması

### Neler Yapıldı?
- Hocanın rubrikte belirttiği 15 anlamlı commit kuralına sadık kalmak adına, üyelik sistemi operasyonu iki ayrı parçaya bölündü ve bu ilk aşamada sadece iş mantığı (Python) kodlandı.
- `app/auth/forms.py` dosyası sıfırdan oluşturularak Flask-WTF tabanlı `RegisterForm` ve `LoginForm` sınıfları yazıldı. Güvenlik için CSRF koruması varsayılan olarak aktif bırakıldı.
- Kayıt formunun içerisine, veritabanını tarayarak girilen e-posta ve kullanıcı adının daha önceden alınıp alınmadığını SQLAlchemy 2.x yapısıyla kontrol eden `validate_email` ve `validate_username` özel doğrulama metotları entegre edildi.
- `app/auth/routes.py` içerisinde `/register`, `/login` ve `/logout` rotalarının mantığı kuruldu. Giriş yapmış kullanıcıların bu sayfalara tekrar erişmesi engellenerek doğrudan anasayfaya postalanmaları sağlandı. Şifrelerin `werkzeug.security` ile hash kontrolü yapıldı ve kullanıcıya dönecek tüm bildirimler için Türkçe flash mesajları tanımlandı.
- `app/__init__.py` (Application Factory) dosyası güncellenerek `LoginManager` nesnesi uygulamaya bağlandı; oturum yönetimi için gereken `user_loader` fonksiyonu modern `db.session.get()` standardıyla koda eklendi.

## Oturum: 4
**Tarih:** 25 Mayıs 2026
**Mod:** Plan
**Model:** Gemini 3.1 Pro
**Görünüm:** Manager
**Hedef:** Kayıt ve Giriş Akışının (Auth) Frontend / HTML Tasarımlarının ve Şablon Entegrasyonunun Tamamlanması

### Neler Yapıldı?
- Oturum 3'te kurulan Python backend altyapısını görselleştirmek ve kullanıcı deneyimine sunmak üzere yepyeni bir oturumla frontend/şablon geliştirme süreci başlatıldı.
- Projenin ana iskeletini oluşturacak olan `app/templates/base.html` şablonu yazıldı. Bootstrap 5 CSS ve JS kütüphaneleri CDN üzerinden projeye dahil edildi.
- `base.html` içerisindeki navigasyon barı (navbar) dinamik hale getirildi. `{% if current_user.is_authenticated %}` Jinja2 kontrolüyle, sisteme giriş yapmış kullanıcılara "Notlarım", "Görevlerim" ve "Çıkış Yap" linklerinin, ziyaretçilere ise sadece "Giriş Yap" ve "Kayıt Ol" bağlantılarının görünmesi sağlandı. Ayrıca Bootstrap'in `alert-dismissible` sınıfı kullanılarak sayfanın üst orta kısmında belirecek dinamik Türkçe flash mesaj alanı entegre edildi.
- `app/templates/auth/login.html` ve `app/templates/auth/register.html` arayüz dosyaları sıfırdan oluşturuldu. Her iki şablonun da `{% extends "base.html" %}` ifadesiyle ana tasarımdan miras alması (Jinja2 template inheritance) sağlandı.
- Formlar, Bootstrap 5'in `card` ve `row justify-content-center` bileşenleri kullanılarak dikey ve yatayda ortalanmış, mobil uyumlu (responsive) kutular içine yerleştirildi.
- Güvenlik kısıtlarına tam uyum sağlamak adına, her iki formun da gövdesine `{{ form.hidden_tag() }}` kodu eklenerek CSRF Token koruması arayüze zorunlu olarak enjekte edildi.
- Kullanıcının formları eksik veya hatalı doldurması durumunda tetiklenecek olan doğrulama hataları (örneğin e-postanın önceden alınmış olması veya şifrelerin eşleşmemesi), Jinja2 döngüleri yardımıyla ilgili alanın hemen altında Bootstrap `invalid-feedback` ve `text-danger` sınıflarıyla kırmızı uyarı metni olarak esnek bir biçimde kurgulandı.

