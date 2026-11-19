from datetime import date

from django.db import migrations


def seed_company_data(apps, schema_editor):
    Department = apps.get_model('company', 'Department')
    Employee = apps.get_model('company', 'Employee')
    Project = apps.get_model('company', 'Project')
    Client = apps.get_model('company', 'Client')
    Contract = apps.get_model('company', 'Contract')

    departments = {}
    for code, name, description, head in [
        ('engineering', 'Інженерія', 'Розробка цифрових продуктів і внутрішніх платформ.', 'Олена Коваль'),
        ('design', 'Дизайн', 'Дослідження користувачів та дизайн сервісів.', 'Марко Левченко'),
        ('operations', 'Операції', 'Підтримка команд, партнерств і бізнес-процесів.', 'Ірина Бондар'),
    ]:
        departments[code], _ = Department.objects.using(schema_editor.connection.alias).get_or_create(
            code=code, defaults={'name': name, 'description': description, 'head_name': head, 'is_active': True}
        )

    db = schema_editor.connection.alias
    for name, position, email, phone, dept in [
        ('Андрій Мельник', 'Технічний директор', 'andrii.melnyk@zemnyux.example', '+380 44 555 01 10', 'engineering'),
        ('Софія Романюк', 'Backend-розробниця', 'sofia.romaniuk@zemnyux.example', '+380 44 555 01 11', 'engineering'),
        ('Данило Шевченко', 'Frontend-розробник', 'danylo.shevchenko@zemnyux.example', '+380 44 555 01 12', 'engineering'),
        ('Марія Климчук', 'Product-дизайнерка', 'maria.klymchuk@zemnyux.example', '+380 44 555 02 10', 'design'),
        ('Тарас Гнатюк', 'Керівник партнерств', 'taras.hnatiuk@zemnyux.example', '+380 44 555 03 10', 'operations'),
    ]:
        Employee.objects.using(db).get_or_create(email=email, defaults={'full_name': name, 'position': position, 'phone': phone, 'department': departments[dept]})

    clients = {}
    for name, industry, email, country in [
        ('Northstar Mobility', 'Транспорт і логістика', 'hello@northstar.example', 'Україна'),
        ('Lumen Health', 'Медичні технології', 'team@lumen.example', 'Польща'),
        ('Greenline Foods', 'Агробізнес', 'office@greenline.example', 'Німеччина'),
    ]:
        clients[name], _ = Client.objects.using(db).get_or_create(name=name, defaults={'industry': industry, 'contact_email': email, 'country': country, 'is_active': True})

    for title, code, status, budget, started in [
        ('Єдина платформа міської мобільності', 'NS-MOB-26', 'active', '248000.00', date(2026, 2, 10)),
        ('Кабінет пацієнта Lumen', 'LH-PORTAL', 'active', '132500.00', date(2026, 4, 1)),
        ('Аналітика ланцюга постачання', 'GF-INSIGHT', 'planned', '89500.00', date(2026, 9, 15)),
    ]:
        Project.objects.using(db).get_or_create(code=code, defaults={'title': title, 'status': status, 'budget': budget, 'start_date': started})

    for number, title, amount, signed, client_name in [
        ('ZN-2026-014', 'Розробка платформи мобільності', '248000.00', date(2026, 2, 5), 'Northstar Mobility'),
        ('ZN-2026-021', 'Портал цифрового здоров’я', '132500.00', date(2026, 4, 18), 'Lumen Health'),
        ('ZN-2026-028', 'Система операційної аналітики', '89500.00', date(2026, 8, 20), 'Greenline Foods'),
    ]:
        Contract.objects.using(db).get_or_create(number=number, defaults={'title': title, 'amount': amount, 'signed_on': signed, 'client': clients[client_name]})


def unseed_company_data(apps, schema_editor):
    # Demo records are intentionally retained on reverse so existing content is safe.
    pass


class Migration(migrations.Migration):
    dependencies = [('company', '0001_initial')]
    operations = [migrations.RunPython(seed_company_data, unseed_company_data)]
