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