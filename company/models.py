from django.db import models


class Department(models.Model):

    name = models.CharField('Назва', max_length=120)
    code = models.SlugField('Код', unique=True, max_length=32)
    description = models.TextField('Опис')
    head_name = models.CharField('Керівник', max_length=120)
    is_active = models.BooleanField('Активний', default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Відділ'
        verbose_name_plural = 'Відділи'

    def __str__(self):
        return self.name


class Employee(models.Model):

    full_name = models.CharField("Повне ім'я", max_length=150)
    position = models.CharField('Посада', max_length=120)
    email = models.EmailField('Email')
    phone = models.CharField('Телефон', max_length=32)
    department = models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='employees',
        verbose_name='Відділ',
    )

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Працівник'
        verbose_name_plural = 'Працівники'

    def __str__(self):
        return self.full_name


class Project(models.Model):

    STATUS_CHOICES = [
        ('planned', 'Заплановано'),
        ('active', 'В роботі'),
        ('done', 'Завершено'),
        ('paused', 'Призупинено'),
    ]

    title = models.CharField('Назва', max_length=180)
    code = models.CharField('Код проєкту', max_length=32, unique=True)
    status = models.CharField('Статус', max_length=16, choices=STATUS_CHOICES, default='planned')
    budget = models.DecimalField('Бюджет', max_digits=12, decimal_places=2)
    start_date = models.DateField('Дата старту')

    class Meta:
        ordering = ['-start_date', 'title']
        verbose_name = 'Проєкт'
        verbose_name_plural = 'Проєкти'

    def __str__(self):
        return f'{self.code} — {self.title}'


class Client(models.Model):

    name = models.CharField('Назва', max_length=180)
    industry = models.CharField('Галузь', max_length=120)
    contact_email = models.EmailField('Контактний email')
    country = models.CharField('Країна', max_length=80)
    is_active = models.BooleanField('Активний', default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Клієнт'
        verbose_name_plural = 'Клієнти'

    def __str__(self):
        return self.name


class Contract(models.Model):

    number = models.CharField('Номер договору', max_length=64, unique=True)
    title = models.CharField('Назва', max_length=180)
    amount = models.DecimalField('Сума', max_digits=12, decimal_places=2)
    signed_on = models.DateField('Дата підписання')
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='contracts',
        verbose_name='Клієнт',
    )

    class Meta:
        ordering = ['-signed_on']
        verbose_name = 'Договір'
        verbose_name_plural = 'Договори'

    def __str__(self):
        return self.number
