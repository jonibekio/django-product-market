# Django 

<p align="center">
  Django asosida yaratilgan mahsulotlar platformasi: kategoriya, profil, va bir nechta rasm bilan CRUD.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-1f6feb?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-6.0-0b3d2e?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Database-SQLite-003b57?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite">
  <img src="https://img.shields.io/badge/Template-Django_Templates-3f2b96?style=for-the-badge" alt="Templates">
</p>

---

## Loyiha haqida

Ushbu loyiha Django darslari uchun yozilgan amaliy market platforma.  
Foydalanuvchi ro'yxatdan o'tadi, tizimga kiradi, profilini boshqaradi, mahsulot qo'shadi va mahsulotga bir nechta rasm yuklaydi.

Frontend `templates/` asosida zamonaviy uslubda yozilgan va mahsulot rasmlari uchun slider mavjud.

## Asosiy imkoniyatlar

- Custom user modeli (`accounts.CustomUser`)
  - `age`, `address`, `avatar`
- Autentifikatsiya
  - ro'yxatdan o'tish, kirish, chiqish
  - profil ko'rish, tahrirlash, parol almashtirish
- Mahsulotlar moduli
  - kategoriya bo'yicha filter
  - yaratish, tahrirlash, o'chirish, detail
  - foydalanuvchining o'z mahsulotlari sahifasi
- Bir nechta rasm yuklash
  - `multiple` file input
  - backendda `request.FILES.getlist("images")`
- Slider
  - chap/o'ng orqali rasm almashtirish
  - tugmalar va nuqtalar bilan navigatsiya

## Afzalliklari

- Sodda va tushunarli arxitektura (`accounts` va `watch` app'lari alohida)
- Foydalanuvchi uchun to'liq CRUD oqimi (qo'shish, ko'rish, tahrirlash, o'chirish)
- Bir nechta rasm yuklash imkoniyati (`multiple upload`)
- Mobilga mos va zamonaviy template dizayn
- Ruxsatlar bilan himoyalangan sahifalar (tasodifiy kirishlar bloklanadi)
- Portfolio va o'quv loyiha sifatida GitHub uchun tayyor

## Kirishdan keyingi ruxsatlar

- Login qilgan foydalanuvchi (admin bo'lsa ham, saytning custom sahifalarida) faqat **o'z profil ma'lumotlarini** ko'ra oladi.
- Boshqa foydalanuvchi profiliga URL orqali kirishga urinsa, ruxsat berilmaydi.
- Mahsulotni faqat uni yaratgan foydalanuvchi tahrirlaydi yoki o'chira oladi.
- `My Products` sahifasida faqat kirgan foydalanuvchining o'z mahsulotlari chiqadi.

Eslatma: Django’ning standart `/admin/` panelida superuser barcha ma'lumotlarni ko'ra oladi. Yuqoridagi cheklovlar saytning custom sahifalari (`/profile/...`, `/watch/...`) uchun amal qiladi.

## Texnologiyalar

| Qism | Texnologiya |
|---|---|
| Backend | Django |
| DB | SQLite |
| Frontend | Django Templates, CSS, JavaScript |
| Media | Pillow + ImageField |

## O'rnatish va ishga tushirish

### 1) Virtual muhit

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Agar `python` ishlamasa:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Kutubxonalar

```powershell
pip install django pillow
```

### 3) Migratsiyalar

```powershell
python manage.py makemigrations
python manage.py migrate
```

### 4) Superuser (ixtiyoriy)

```powershell
python manage.py createsuperuser
```

### 5) Serverni ishga tushirish

```powershell
python manage.py runserver
```

Brauzerda oching: `http://127.0.0.1:8000/`

## URL yo'llar

### Accounts

| Yo'l | Tavsif |
|---|---|
| `/` | Bosh sahifa |
| `/signup/` | Ro'yxatdan o'tish |
| `/login/` | Kirish |
| `/logout/` | Chiqish |
| `/profile/<pk>/` | Profil |
| `/profile/<pk>/edit/` | Profilni tahrirlash |
| `/profile/<pk>/password/` | Parolni almashtirish |

### Watch (mahsulotlar)

| Yo'l | Tavsif |
|---|---|
| `/watch/category/<pk>/` | Kategoriya mahsulotlari |
| `/watch/create/` | Mahsulot qo'shish |
| `/watch/update/<pk>/` | Mahsulotni tahrirlash |
| `/watch/detail/<pk>/` | Mahsulot tafsiloti |
| `/watch/delete/<pk>/` | Mahsulotni o'chirish |
| `/watch/my_products/` | Mening mahsulotlarim |
| `/watch/products/` | Paginationsiz emas, sahifalangan ro'yxat |

## Media sozlamalari

`config/settings.py` ichida media sozlangan:

- `MEDIA_URL = '/media/'`
- `MEDIA_ROOT = BASE_DIR / 'media/'`

`DEBUG=True` holatda media fayllar lokalda avtomatik servis qilinadi.

## Loyiha strukturasi

```text
django_dars8/
  accounts/               # User, auth, profile
  watch/                  # Category, product, images
  templates/              # Barcha HTML shablonlar
  config/                 # settings.py, urls.py
  media/                  # Yuklangan rasmlar
  db.sqlite3
  manage.py
```

## Muhim eslatmalar

- `SECRET_KEY` va `DEBUG` productionga chiqarishda albatta o'zgartiriladi.
- `ALLOWED_HOSTS` production server uchun to'ldiriladi.
- Bu loyiha dars/portfolio uchun mos.

---

## Author

`Jonibeks` loyihasi asosida tayyorlangan Django amaliyoti.
