# DevDash Geliştirici AI Günlüğü

## Oturum 1 — 25 Mayıs 2026 — 19:00-20:30

### Hedef
Uygulamanın temel mimarisini ve dizin yapısını ölçeklenebilir, sürdürülebilir bir yapıda kurmak amacıyla Application Factory Pattern düzeninde tasarlamak.

### Kullandığım Mod ve Model
- Mod: Plan / Fast
- Model: Gemini 3 Pro
- Görünüm: Manager / Editor

### Verdiğim Promptlar
1. "Flask 3.x ve Python kullanarak DevDash adında bir mikroblog ve görev yönetim uygulaması iskeleti oluştur. Proje kesinlikle Application Factory yapısında olmalı ve blueprint mimarisi içermeli."

### Ajanın Önerdiği Plan
Ajan, kök dizinde bir `run.py` ve çekirdek yapı için `app/` klasörü açıp altında `__init__.py` oluşturmayı, auth ve ana modüller için iki ayrı blueprint tasarlamayı önerdi.

### Plan'da Sorguladıklarım
- Ajan ilk başta tüm konfigürasyonları doğrudan `__init__.py` içine gömmeyi teklif etti. Bu yaklaşıma mimari açıdan karşı çıktım. Güvenlik ve temiz kod prensipleri gereği konfigürasyonların bağımsız bir `config.py` dosyasından okunması gerektiğini, özellikle `.env` bağımlılığının burada yönetilmesi gerektiğini belirterek planı daha profesyonel bir yapıya revize ettirdim.

### Üretilen Kodda Düzelttiklerim
- `app/__init__.py` içerisinde ajanın ürettiği ilk kod bloğunda blueprint'lerin import sırası döngüsel bağımlılığa (circular import) sebep oluyordu. Kodun factory fonksiyonunun en altında import edilmesi gerektiğini belirterek satır dizilimini manuel olarak teknik olarak doğruladım.

### Karşılaştığım Hatalar ve Çözümler
- **Hata:** Flask sunucusu çalıştırıldığında konfigürasyon sınıfının bulunamaması hatası alındı.
- **Çözüm:** `config.py` içindeki `Config` sınıfının isimlendirmesinde ajan küçük harf kullanmıştı, bunu standart isimlendirme kurallarına uygun olarak büyük harfe çevirerek entegrasyonu sağladım.

### Bu Oturumdan Öğrendiğim
Yaygın kullanılan yapay zeka ajanları karmaşık mimarileri hızlıca kurabilse de konfigürasyon yönetimi ve dosya hiyerarşisi gibi mimari hassasiyetlerde pratik ama güvensiz yolları tercih edebiliyor. Tasarımın başında doğru mimariyi dikte etmek projenin gelecekteki teknik borçlarını engeller.

### Sonraki Oturum İçin Notlar
- Bir sonraki oturumda veritabanı modellerinin veri tutarlılığı açısından yapılandırılması planlanmıştır.

---

## Oturum 2 — 26 Mayıs 2026 — 15:30-17:00

### Hedef
Uygulamanın veri modelleme aşamasını tamamlamak; User, Note ve Task tablolarını aralarındaki ilişkilerle birlikte nesne tabanlı olarak tanımlamak.

### Kullandığım Mod ve Model
- Mod: Plan
- Model: Gemini 3 Pro
- Görünüm: Manager / Editor

### Verdiğim Promptlar
1. "Uygulama için app/models.py dosyasını oluştur. User, Note ve Task adında 3 modelimiz olacak. Kullanıcı şifreleri kesinlikle güvenli şekilde hashlenmeli."

### Ajanın Önerdiği Plan
Ajan, Flask-SQLAlchemy kütüphanesini kullanarak modelleri tek bir dosya altında yapılandırmayı ve şifre güvenliği için `werkzeug.security` entegrasyonunu yapmayı planladı.

### Plan'da Sorguladıklarım
- **Kritik Müdahale:** Ajan modelleri üretirken eski tip SQLAlchemy 1.x standardı olan `db.Column` yapılarını kullandı. Projenin modern ve güncel teknoloji yığınında kalması adına bu yaklaşıma müdahale ettim. En güncel standart olan SQLAlchemy 2.x tiplerini (`Mapped` ve `mapped_column`) kullanması konusunda ajanı yönlendirerek planı tamamen modernize ettim.

### Üretilen Kodda Düzelttiklerim
- `User` modelinde tanımlanan `notes` ilişkisinde (relationship) ajan ters ilişkiyi (`back_populates`) eklemeyi unutmuştu. Veritabanı bütünlüğünün ve çift yönlü sorguların bozulmaması adına koda müdahale edip ilişkileri elle güncelledim.

### Karşılaştığım Hatalar ve Çözümler
- **Hata:** Modeller import edilirken `ContextualSelect` uyarısı ve ilişki haritalama hatası fırlatıldı.
- **Çözüm:** Görev (Task) modelindeki yabancı anahtar tanımında tablo isminin küçük harfle yazılması gerekirken ajan büyük harf yazmıştı; `user.id` olarak düzelterek ilişki zincirini bağladım.

### Bu Oturumdan Öğrendiğim
Yapay zeka modelleri, internetteki eski veri yoğunluğundan dolayı veritabanı tasarımlarında eski kalıpları (SQLAlchemy 1.x) kullanmaya meyilli. Geliştiricinin güncel dökümantasyon kısıtlarını bilmesi ve ajanı bu doğrultuda denetlemesi projenin kalitesini doğrudan etkiler.

### Sonraki Oturum İçin Notlar
- Kullanıcı kayıt ve giriş formlarının veri doğrulama (validation) katmanlarının yazılması.

---

## Oturum 3 — 27 Mayıs 2026 — 11:00-12:30

### Hedef
Güvenli kullanıcı kimlik doğrulama (Authentication) backend yapısının kurulması, Flask-Login entegrasyonu ve güvenli form sınıflarının kodlanması.

### Kullandığım Mod ve Model
- Mod: Plan / Fast
- Model: Gemini 3 Pro
- Görünüm: Manager

### Verdiğim Promptlar
1. "Flask-WTF kullanarak RegisterForm ve LoginForm sınıflarını yaz. Flask-Login ile kullanıcı oturum yönetimini app/auth/views.py içinde yapılandır."

### Ajanın Önerdiği Plan
Ajan, `forms.py` dosyası açıp alanları tanımlamayı, ardından auth blueprint'i altında `login`, `register` ve `logout` rotalarını yazmayı planladı.

### Plan'da Sorguladıklarım
- Ajan kullanıcı kayıt olurken e-posta adresi veritabanında zaten var mı diye bir benzersizlik kontrolü (validator) planlamamıştı. Sisteme aynı e-posta ile mükerrer kayıt yapılabilmesi gibi ciddi bir mantıksal açığa müdahale ederek, form sınıfı içerisine dinamik `validate_email` metodunu eklettim.

### Üretilen Kodda Düzelttiklerim
- `LoginForm` backend doğrulamasında ajan şifre kontrolünü güvensiz bir şekilde düz metin olarak eşleştirmeye çalıştı. Oturum 2'de şifreleri hashlediğimizi hatırlatarak `check_password_hash` kullanımını koda ekletip güvenlik açığını kapattım.

### Karşılaştığım Hatalar ve Çözümler
- **Hata:** `UserMixin` sınıfı `User` modeline dahil edilmediği için Flask-Login `current_user` nesnesinde yetkilendirme hatası fırlattı.
- **Çözüm:** `models.py` dosyasına dönüp `User` sınıfına `UserMixin` kalıtımını manuel olarak ekleyerek oturum yönetimini aktif hale getirdim.

### Bu Oturumdan Öğrendiğim
Güvenlik kritik katmanlarda ajanın ürettiği kodları satır satır denetlemek hayati önem taşıyor. Şifre hash kontrolünü atlayarak düz metin eşlemesi önermesi, yapay zekanın güvenlik mimarilerinde ne kadar büyük mantıksal zaaflar üretebileceğinin somut bir örneğidir.

### Sonraki Oturum İçin Notlar
- Yazılan auth mekanizmasının kullanıcı dostu arayüzler ile giydirilmesi.

---

## Oturum 4 — 28 Mayıs 2026 — 14:00-16:00

### Hedef
Kullanıcı giriş ve kayıt sayfalarının Bootstrap 5 kullanılarak mobil uyumlu arayüzlerinin tasarlanması ve Jinja2 şablon kalıtımı (inheritance) mimarisinin oturtulması.

### Kullandığım Mod ve Model
- Mod: Plan
- Model: Gemini 3 Pro
- Görünüm: Editor / Manager

### Verdiğim Promptlar
1. "Bootstrap 5 kullanarak base.html, login.html ve register.html sayfalarını tasarla. Tasarım modern, temiz ve tamamen responsive olmalı."

### Ajanın Önerdiği Plan
Ajan, `templates/` klasörü altında ana iskeleti, ardından bu iskeletten türeyen giriş ve kayıt form sayfalarını HTML olarak üretmeyi önerdi.

### Plan'da Sorguladıklarım
- **Kritik Güvenlik Müdahalesi:** Ajan HTML formlarını oluştururken `{{ form.hidden_tag() }}` yapısını planına dahil etmemişti. Formlarda CSRF (Cross-Site Request Forgery) koruma tokenı olmazsa uygulamanın dışarıdan gelebilecek siber saldırılara tamamen açık hale geleceğini fark ettim. Ajanı uyararak tüm formların en başına CSRF token mühürlerini eklettim.

### Üretilen Kodda Düzelttiklerim
- Ajan mesaj kutularında (Flash messages) Bootstrap'in dinamik kapanma özelliğini (`data-bs-dismiss="alert"`) yanlış sözdizimi ile yazmıştı. Arayüzde kapanmayan uyarı kutularını düzeltmek için HTML kodundaki ilgili Bootstrap niteliğini elle revize ettim.

### Karşılaştığım Hatalar ve Çözümler
- **Hata:** Giriş butonuna basıldığında form verileri POST rotasına gönderilirken 400 Bad Request hatası fırlatıldı.
- **Çözüm:** Formun HTML tagında `method="POST"` niteliğinin eksik olduğunu fark ettim ve koda ekleyerek veri akışını sağladım.

### Bu Oturumdan Öğrendiğim
Arayüz giydirme süreçlerinde ajanlar görsel tasarıma odaklanıp web formlarının en temel güvenlik gereksinimlerini atlayabiliyorlar. Tamamen güvenli ve yayınlanabilir bir ürün elde etmek için yapay zekanın görsel çıktılarının arkasındaki güvenlik taglarını tek tek denetlemek şarttır.

### Sonraki Oturum İçin Notlar
- Veritabanı sürüm kontrol süreçlerinin (Flask-Migrate) başlatılması ve tabloların fiziksel hale getirilmesi.

---

## Oturum 5: DevDash Veritabanı Versiyonlama (Migrate) ve Altyapı Kurulumu
**Tarih:** 29 Mayıs 2026 — **Saat:** 13:30 - 15:45  
**Kullanılan Model/Mod:** Antigravity IDE - Plan & Act Modu

### 🎯 Oturum Hedefleri
1. DevDash projesinde veritabanı şema yönetimini otomatikleştirmek adına Flask-Migrate altyapısının entegre edilmesi.
2. Tasarlanan User, Note ve Task modellerine ait ilk veritabanı göç (migration) taslağının üretilmesi.
3. Üretilen taslağın yerel SQLite (`app.db`) veritabanına fiziksel olarak uygulanarak tabloların hazır hale getirilmesi.

### 💻 Yapılan Geliştirmeler ve Değişiklikler

#### 1. Flask-Migrate Entegrasyonu
* **`app/__init__.py`:** Factory fonksiyonu (`create_app`) içerisine `flask_migrate` kütüphanesinden `Migrate` nesnesi dahil edildi. `migrate.init_app(app, db)` satırı eklenerek veritabanı ile versiyonlama motoru birbirine bağlandı.

#### 2. Veritabanı Şema Üretimi ve Fiziksel Dağıtım
* Sandbox terminali üzerinden `$env:FLASK_APP="run.py"` ortam değişkeni set edilerek sırasıyla şu operasyonlar yürütüldü:
    * `flask db init` komutuyla projeye `migrations/` mimari dizini kazandırıldı.
    * `flask db migrate -m "initial_schema"` komutu tetiklenerek modeller otomatik tarandı ve `migrations/versions/4d3ad2f79f13_initial_schema.py` dosyası altında ilk SQL şemaları (User, Note, Task tabloları, veri tipleri ve Foreign Key ilişkileri) kod düzeyinde üretildi.
    * `flask db upgrade` komutu koşturularak yerel dizinde `app.db` fiziksel SQLite veritabanı dosyası ilk kez ayağa kaldırıldı ve tablolar içeriye mühürlendi.
    * `flask db current` sorgusuyla veritabanının güncel takip sürümünün başarıyla `4d3ad2f79f13 (head)` noktasına eşitlendiği teknik olarak doğrulandı.

### 🔍 Karşılaşılan Hatalar ve Çözümler
* **Git Uyarı Yönetimi:** `git add .` aşamasında üretilen göç dosyaları için Windows ve Linux satır sonu karakter farklılığından kaynaklı terminalde beliren sarı renkli CRLF/LF uyarıları (`warning: in the working copy of...`) incelendi. Bu durumun projenin çalışma stabilitesine veya Git geçmişine bir engel teşkil etmediği siber güvenlik ve sistem mimarisi standartlarında doğrulanarak süreç pürüzsüzce devam ettirildi.

### 🧠 Öğrenilenler ve Kazanımlar
* Canlı projelerde veritabanını manuel SQL komutlarıyla veya sıfırlayarak yönetmek yerine, Flask-Migrate (Alembic) kullanarak veri kaybı yaşamadan şema versiyonlamanın önemi ve mantığı kavrandı.
* Windows PowerShell üzerinde Flask ortam değişkenlerini (`$env:FLASK_APP`) doğru yönetme pratikleri pekiştirildi.

---

## Oturum 6: Çekirdek Özelliklerin (Notlar ve Görevler) Geliştirilmesi
**Tarih:** 30 Mayıs 2026 — **Saat:** 14:08 - 15:20  
**Kullanılan Model/Mod:** Antigravity IDE - Plan & Act Modu

### 🎯 Oturum Hedefleri
1. DevDash uygulamasının ana işlevselliği olan "Notlar" ve "Görevler" modülleri için uçtan uca backend ve frontend katmanlarının inşa edilmesi.
2. SQLAlchemy 2.x standartlarına uygun, giriş yapmış kullanıcıya özel (`current_user`) veri izolasyonu ve güvenli silme/güncelleme mekanizmalarının kurulması.
3. Bootstrap 5 kütüphanesi kullanılarak, notların ve görevlerin listelenebileceği, durumlarının dinamik olarak değiştirilebileceği responsive bir gösterge paneli (Dashboard) tasarımı.

### 💻 Yapılan Geliştirmeler ve Değişiklikler

#### 1. Backend Katmanı (Rotalar ve Form Yapıları)
* **`app/main/forms.py` (Yeni):** Flask-WTF kütüphanesi kullanılarak, veri girişlerinde otomatik CSRF koruması sağlayan `NoteForm` (Başlık ve İçerik alanları) ve `TaskForm` (Görev Adı ve Açıklama alanları) sınıfları tanımlandı.
* **`app/main/routes.py` (Yeni/Düzenleme):** Tüm veri operasyonları `@login_required` dekoratörü ile koruma altına alındı.
    * `/note/add` ve `/task/add` rotalarıyla form verileri doğrulanarak aktif kullanıcıya ait yeni kayıtlar üretildi.
    * `/note/delete/<id>` ve `/task/delete/<id>` rotalarında sadece ID kontrolü yerine `where(Model.user_id == current_user.id)` kısıtı eklenerek yetkisiz veri silme girişimleri (ID spoofing) engellendi.
    * `/task/toggle/<id>` rotasıyla veritabanında ilgili görevin statüsü "Yapılacak" ve "Bitti" durumları arasında anlık olarak güncellenecek şekilde kurgulandı.

#### 2. Frontend Katmanı (Bootstrap 5 & Jinja2 Entegrasyonu)
* **`app/templates/main/index.html` (Yeni):** Ana sayfa tasarımı bilgisayar görünümlerinde iki eşit sütuna (`col-md-6`), mobil görünümlerde ise dikey esnek bloklara dönüştürülecek şekilde responsive tasarlandı.
* **Mavi (Primary) Tonlu Notlar Alanı:** Kullanıcının notları Jinja2 döngüsüyle modern Bootstrap kartları (`card`) şeklinde listelendi ve her kartın altına form tabanlı güvenli silme butonları yerleştirildi.
* **Yeşil (Success) Tonlu Görevler Alanı:** Tamamlanan görevlerin (`task.status == 'Bitti'`) arayüzde dinamik olarak üstünün çizilmesi (`text-decoration-line-through`) ve arka planının soluklaştırılması (`text-muted`, `bg-light`) Jinja2 lokal değişkenleri yardımıyla sağlandı. Görev durumunu anlık değiştiren mikro buton grupları entegre edildi.

### 🔍 Karşılaşılan Hatalar ve Çözümler
* **Kritik Durum:** Ajan, yerel dizinde önceki adımdan kalan ve içi boş olan `app.db` dosyasını tespit ettiğinde doğrudan veri sorgulama hatası yaşanmaması adına akıllıca bir uyarı üretti. Bu doğrultuda, durum kontrolünden (`current`) önce veritabanı tablolarının fiziksel olarak işlenmesi adına plan revize edilerek `flask db upgrade` adımı pürüzsüzce yürütüldü ve şema takibi `4d3ad2f79f13` sürümüne başarıyla eşitlendi.

### 🧠 Öğrenilenler ve Kazanımlar
* Flask-WTF form mimarisinin backend doğrulama süreçlerini ne kadar kısalttığı deneyimlendi.
* Jinja2 şablon motoru içerisinde logic operasyonlar (`{% set is_done = ... %}`) yürüterek arka plana yük bindirmeden dinamik kullanıcı deneyimi (UX) tasarlama pratikleri kazanıldı.
* Veritabanı sorgularında `current_user.id` kısıtlamasının, siber güvenlik ve veri izolasyonu açısından ne kadar hayati olduğu kavrandı.

---

## Oturum 6: Çekirdek Özelliklerin (Notlar ve Görevler) Geliştirilmesi
**Tarih:** 30 Mayıs 2026 — **Saat:** 14:05 - 15:20  
**Kullanılan Model/Mod:** Antigravity IDE - Plan & Act Modu

### 🎯 Oturum Hedefleri
1. DevDash uygulamasının ana işlevselliği olan "Notlar" ve "Görevler" modülleri için uçtan uca backend ve frontend katmanlarının inşa edilmesi.
2. SQLAlchemy 2.x standartlarına uygun, giriş yapmış kullanıcıya özel (`current_user`) veri izolasyonu ve güvenli silme/güncelleme mekanizmalarının kurulması.
3. Bootstrap 5 kütüphanesi kullanılarak, notların ve görevlerin listelenebileceği, durumlarının dinamik olarak değiştirilebileceği responsive bir gösterge paneli (Dashboard) tasarımı.

### 💻 Yapılan Geliştirmeler ve Değişiklikler

#### 1. Backend Katmanı (Rotalar ve Form Yapıları)
* **`app/main/forms.py` (Yeni):** Flask-WTF kütüphanesi kullanılarak, veri girişlerinde otomatik CSRF koruması sağlayan `NoteForm` (Başlık ve İçerik alanları) ve `TaskForm` (Görev Adı ve Açıklama alanları) sınıfları tanımlandı.
* **`app/main/routes.py` (Yeni/Düzenleme):** Tüm veri operasyonları `@login_required` dekoratörü ile koruma altına alındı.
    * `/note/add` ve `/task/add` rotalarıyla form verileri doğrulanarak aktif kullanıcıya ait yeni kayıtlar üretildi.
    * `/note/delete/<id>` ve `/task/delete/<id>` rotalarında sadece ID kontrolü yerine `where(Model.user_id == current_user.id)` kısıtı eklenerek yetkisiz veri silme girişimleri (ID spoofing) engellendi.
    * `/task/toggle/<id>` rotasıyla veritabanında ilgili görevin statüsü "Yapılacak" ve "Bitti" durumları arasında anlık olarak güncellenecek şekilde kurgulandı.

#### 2. Frontend Katmanı (Bootstrap 5 & Jinja2 Entegrasyonu)
* **`app/templates/main/index.html` (Yeni):** Ana sayfa tasarımı bilgisayar görünümlerinde iki eşit sütuna (`col-md-6`), mobil görünümlerde ise dikey esnek bloklara dönüştürülecek şekilde responsive tasarlandı.
* **Mavi (Primary) Tonlu Notlar Alanı:** Kullanıcının notları Jinja2 döngüsüyle modern Bootstrap kartları (`card`) şeklinde listelendi ve her kartın altına form tabanlı güvenli silme butonları yerleştirildi.
* **Yeşil (Success) Tonlu Görevler Alanı:** Tamamlanan görevlerin (`task.status == 'Bitti'`) arayüzde dinamik olarak üstünün çizilmesi (`text-decoration-line-through`) ve arka planının soluklaştırılması (`text-muted`, `bg-light`) Jinja2 lokal değişkenleri yardımıyla sağlandı. Görev durumunu anlık değiştiren mikro buton grupları entegre edildi.

### 🔍 Karşılaşılan Hatalar ve Çözümler
* **Kritik Durum:** Ajan, yerel dizinde önceki adımdan kalan ve içi boş olan `app.db` dosyasını tespit ettiğinde doğrudan veri sorgulama hatası yaşanmaması adına akıllıca bir uyarı üretti. Bu doğrultuda, durum kontrolünden (`current`) önce veritabanı tablolarının fiziksel olarak işlenmesi adına plan revize edilerek `flask db upgrade` adımı pürüzsüzce yürütüldü ve şema takibi `4d3ad2f79f13` sürümüne başarıyla eşitlendi.

### 🧠 Öğrenilenler ve Kazanımlar
* Flask-WTF form mimarisinin backend doğrulama süreçlerini ne kadar kısalttığı deneyimlendi.
* Jinja2 şablon motoru içerisinde logic operasyonlar (`{% set is_done = ... %}`) yürüterek arka plana yük bindirmeden dinamik kullanıcı deneyimi (UX) tasarlama pratikleri kazanıldı.
* Veritabanı sorgularında `current_user.id` kısıtlamasının, siber güvenlik ve veri izolasyonu açısından ne kadar hayati olduğu kavrandı.

---

## Oturum 7: Özel Hata Sayfaları, Profil Yönetimi ve Güvenli Dosya Yükleme (Avatar)
**Tarih:** 31 Mei 2026 — **Saat:** 12:45 - 14:30  
**Kullanılan Model/Mod:** Antigravity IDE - Plan & Act Modu

### 🎯 Oturum Hedefleri
1. Proje isterlerinde (PDF) yer alan Custom Error Pages mimarisinin kurularak 404 ve 500 hatalarının yakalanması.
2. SQLAlchemy 2.x yapısına uygun olarak `User` modeline profil resmi (`avatar_img`) alanının entegre edilmesi ve şemanın güncellenmesi.
3. Kullanıcıların profil bilgilerini güncelleyebileceği ve sunucuya güvenli bir şekilde profil fotoğrafı (Avatar) yükleyebileceği backend rotalarının ve Bootstrap 5 tabanlı `profile.html` arayüzünün tamamlanması.

### 💻 Yapılan Geliştirmeler ve Değişiklikler

#### 1. Modüler Hata Yönetimi (Custom Error Pages)
* **`app/errors/` (Yeni Blueprint):** Hata yakalayıcıları ana uygulama mimarisinden izole etmek ve kod kalitesini artırmak adına yeni bir blueprint tanımlandı ve `app/__init__.py` (Application Factory) içerisine kaydedildi.
* **`app/errors/handlers.py` (Yeni):** `@errors.app_errorhandler()` dekoratörü kullanılarak tüm uygulama genelindeki 404 ve 500 hataları merkezi kontrol altına alındı. 500 hata durumlarında veritabanı kilitlenmelerini önlemek adına `db.session.rollback()` mekanizması kuruldu.
* **`app/templates/errors/` (Yeni):** `base.html` şablonundan türetilen, `text-center` ile dikey/yatay ortalanmış ve ana sayfaya dönüş butonu barındıran responsive `404.html` ve `500.html` şablonları Bootstrap 5 sınıflarıyla tasarlandı.

#### 2. Veritabanı Şema Genişletmesi
* **`app/models.py`:** `User` model sınıfı içerisine, SQLAlchemy 2.x standartlarına uygun biçimde `avatar_img: Mapped[Optional[str]] = mapped_column(String(150), default='default_avatar.png', nullable=True)` kolonu eklendi.
* Sandbox terminali üzerinden `flask db migrate -m "add avatar_img to user"` komutu tetiklenerek `19296ff4c76f` sürüm göç dosyası üretildi. Ardından `flask db upgrade` komutu manuel olarak koşturularak şema yerel `app.db` (SQLite) dosyasına fiziksel olarak işlendi.

#### 3. Profil Yönetimi ve Güvenli Dosya Yükleme (File Upload)
* **`app/main/forms.py`:** Flask-WTF bünyesindeki `FileField` ve `FileAllowed` bileşenleri kullanılarak sadece `jpg`, `jpeg` ve `png` uzantılarını kabul eden, CSRF korumalı `ProfileForm` sınıfı üretildi.
* **`app/main/routes.py` (`/profile` rotası):** GET isteklerinde kullanıcının mevcut verilerini form alanlarına dolduran, POST isteklerinde ise yüklenen dosyaları `werkzeug.utils.secure_filename` süzgecinden geçiren mantık kuruldu. Dosya adı çakışmalarını (Override) kesin olarak önlemek adına dosya isimlerinin başına dinamik olarak `user_{current_user.id}_` ön eki (prefix) eklendi ve `app/static/avatars/` dizinine fiziksel kaydı yapıldı.
* **`app/templates/main/profile.html` (Yeni):** Sol sütunda kullanıcının güncel avatarını mavi canlı bir çerçevede (`border-primary`, `img-thumbnail rounded-circle`) sergileyen, sağ sütunda ise profil formunu barındıran modern bir kullanıcı arayüzü inşa edildi. Form elementine ikili veri aktarımı için `enctype="multipart/form-data"` kısıtı başarıyla uygulandı.

### 🔍 Karşılaşılan Hatalar ve Çözümler
* **Hata 1 (ModuleNotFoundError):** Profil doğrulamaları esnasında WTForms kütüphanesinin string e-posta format doğrulaması yapabilmek için yerel sanal ortamda (`venv`) `email-validator` paketine ihtiyaç duyduğu tespit edildi ve sistem *500 Internal Server Error* verdi. Sunucu anlık olarak durdurulup `pip install email-validator` komutuyla bağımlılık çözüldü, sistem yeniden başlatılarak stabilite sağlandı.
* **Hata 2 (TypeError - NoneType):** Yeni geliştirilen `/profile` rotası ilk kez test edilirken, veritabanı göçünden önce oluşturulmuş mevcut test kullanıcılarının `avatar_img` alanlarının veritabanında `Null` (Python tarafında `None`) kalmasından ötürü `TypeError: can only concatenate str (not "NoneType") to str` hatası tetiklendi ve sistem yeni yazılan özel 500 hata sayfasını başarıyla devreye soktu. `app/main/routes.py` dosyası üzerinde yapılan kod müdahalesiyle dinamik bir `fallback` (varsayılan atama) mekanizması kurgulandı: Eğer `current_user.avatar_img` boş gelirse otomatik olarak `default_avatar.png` çağrılacak şekilde rota güvenli hale getirilerek çökme kesin olarak giderildi.

### 🧠 Öğrenilenler ve Kazanımlar
* Web uygulamalarında kullanıcı kaynaklı dosya yükleme işlemlerinde siber güvenlik risklerini (zararlı dosya isimleri, uzantı manipülasyonları ve dosya çakışmaları) yönetme pratikleri pekiştirildi.
* Flask projelerinde büyük mimarileri yönetirken hata sayfalarını ayrı bir Blueprint altında toplamanın kod okunabilirliği ve sürdürülebilirlik açısından faydaları kavrandı.
* Mevcut veritabanı verilerinin şema göçleri (migration) esnasında kod katmanında yaratabileceği veri tipi uyuşmazlıkları ve bunlara karşı defansif kodlama (defensive programming) teknikleri deneyimlendi.