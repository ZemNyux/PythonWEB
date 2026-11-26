# Корпоративний веб-портал ZemNyux Inc. (Django Nested Routes)

Веб-проєкт на **Django 6.1** (Python **3.14+**), що демонструє архітектуру корпоративного сайту з **вкладеними маршрутами** (`nested routes`), динамічними параметрами (`<slug:...>`), регулярними виразами (`re_path`), переадресацією, кастомним 404, моделями/формами, сучасним UI та кастомними middleware.

---

## Швидкий старт

```bash
cp .env.example .env          # задайте DJANGO_SECRET_KEY
source .venv/bin/activate     # або створіть venv на Python 3.14+
pip install "django>=6.1.3"
python manage.py migrate
python manage.py runserver
python manage.py test
```

Налаштування через змінні середовища / `.env`:
- `DJANGO_SECRET_KEY` — секретний ключ (обовʼязково змінити поза локальною розробкою)
- `DJANGO_DEBUG` — `1` або `0`
- `DJANGO_ALLOWED_HOSTS` — список через кому

---

## Структура розділів та маршрутизації

### Основні розділи
1. **Головна** (`/`)
2. **Про компанію** (`/about/`; вкладені шляхи редіректять на канонічний URL)
3. **Керівництво** (`/management/`)
4. **Новини** (`/news/`)
5. **Філії** (`/branches/`) — додаток `branches`
6. **Контакти** (`/contacts/`) — список країн + форма звернення

### Підрозділи
* `/branches/london|paris|berlin/` — деталі філії (один generic view)
* `/branches/London/` тощо → **302** на lowercase-канон
* `/branches/history/`, `/branches/history/dates/`, `/branches/history/facts/`
* `/contacts/<slug:country>/` — представництва (ukraine, france, austria, germany)

### Redirects
* `/branch/` → `/branches/`
* `/contact/` → `/contacts/`
* `/history/` → `/branches/history/`
* `/news/...`, `/about/...`, `/management/...` → канонічні розділи

---

## Моделі та адмінка

Контент порталу зберігається в БД (SQLite) і наповнюється seed-міграціями:
- `core`: статистика, напрямки, принципи, новини, керівництво, представництва, запити з форми
- `branches`: філії, хронологія, факти

### Додаток `company` («Моя компанія») — 5 сутностей
Кожна модель має **5 полів** (без урахування `id`). Після `migrate` у `db.sqlite3` з’являються **порожні** таблиці:

| Модель | Призначення | Поля |
|--------|-------------|------|
| `Department` | Відділ | name, code, description, head_name, is_active |
| `Employee` | Працівник | full_name, position, email, phone, department |
| `Project` | Проєкт | title, code, status, budget, start_date |
| `Client` | Клієнт | name, industry, contact_email, country, is_active |
| `Contract` | Договір | number, title, amount, signed_on, client |

Адмінка: `/admin/` (після `createsuperuser`).

### Кастомна панель керування

`/admin/` оформлена як панель ZemNyux у темній бірюзовій палітрі: огляд реєстрів, швидкі переходи до таблиць, пошук, фільтри та стандартні форми Django для створення й редагування записів. Міграція `company.0002_seed_demo_data` додає демонстраційні відділи, працівників, проєкти, клієнтів і договори під час `migrate`.

### Реєстрація та вхід на сайт

- `/accounts/register/` — реєстрація за логіном, email і паролем із підтвердженням; після реєстрації користувач одразу входить.
- `/accounts/login/` і `/accounts/logout/` — вхід та вихід.
- Головна сторінка `/` доступна лише після входу; у шапці показується привітання з логіном.
- Акаунти зберігаються в пам'яті процесу, а не в моделях чи БД; паролі зберігаються як хеші. Після перезапуску сервера пам'ять очищається, тому облікові записи потрібно створити знову.

---

## Middleware
1. `log_requests` — лог методу, URL, статусу та часу
2. `CustomHeaderMiddleware` — `X-Powered-By`, `X-Company-Name`

---

## UI
* Шрифти: **Manrope** + **Source Serif 4**
* Палітра: ink / teal (без дефолтного «AI purple»)
* Sticky navbar, breadcrumbs, timeline, форма контактів

---

## Шаблони (лабораторне завдання)

1. **Складні словники + власні класи** (`core/entities.py`): `MetricCard`, `ServiceOffer`, `LeaderProfile` передаються у `portal_data` / `board_data`.
2. У шаблонах використано `{% with %}`, `{% if %}…{% else %}…{% endif %}`, `{% for %}`.
3. Стандартні фільтри: `length`, `date`, `truncatewords`, `upper`, `default`.
4. Кастомні фільтри: `format_phone`, `status_badge` (`core/templatetags/company_extras.py`).
5. Наслідування: розділи `{% extends 'base.html' %}` і перевизначають блоки `title`, `brand_name`, `page_intro`, `content`, `footer_note`.

## Окремий React-клієнт

У папці [`react-client/`](react-client/) розміщено окремий React-застосунок для панелі компанії. Він отримує дані з Django API `GET /api/company/` та показує відділи, працівників, проєкти, клієнтів і договори.

Запуск локально:

```bash
# термінал 1 — корінь Django-проєкту
python manage.py runserver

# термінал 2
cd react-client
npm install
npm run dev
```

Відкрийте адресу Vite (типово `http://localhost:5173`). Для роботи клієнта потрібен запущений Django-сервер на `http://127.0.0.1:8000`.
