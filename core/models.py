from django.db import models


class CompanyStat(models.Model):
    value = models.CharField(max_length=32)
    label = models.CharField(max_length=120)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Показник'
        verbose_name_plural = 'Показники'

    def __str__(self):
        return f'{self.value} — {self.label}'


class ServiceDirection(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    icon = models.CharField(max_length=16, blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Напрямок діяльності'
        verbose_name_plural = 'Напрямки діяльності'

    def __str__(self):
        return self.title


class CompanyPrinciple(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Принцип'
        verbose_name_plural = 'Принципи'

    def __str__(self):
        return self.title


class NewsArticle(models.Model):
    BADGE_CHOICES = [
        ('badge-primary', 'Primary'),
        ('badge-success', 'Success'),
        ('badge-info', 'Info'),
        ('badge-warning', 'Warning'),
    ]

    title = models.CharField(max_length=255)
    published_on = models.DateField()
    category = models.CharField(max_length=64)
    badge_class = models.CharField(max_length=32, choices=BADGE_CHOICES, default='badge-primary')
    summary = models.TextField()
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_on', '-id']
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=180)
    bio = models.TextField()
    initials = models.CharField(max_length=4)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Член керівництва'
        verbose_name_plural = 'Керівництво'

    def __str__(self):
        return self.name


class ContactOffice(models.Model):
    code = models.SlugField(unique=True)
    name = models.CharField(max_length=120)
    city = models.CharField(max_length=120)
    flag = models.CharField(max_length=8, blank=True)
    short_desc = models.TextField()
    page_title = models.CharField(max_length=255)
    page_lead = models.TextField()
    related_branch_slug = models.SlugField(blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Представництво'
        verbose_name_plural = 'Представництва'

    def __str__(self):
        return self.name


class ContactLocation(models.Model):
    office = models.ForeignKey(ContactOffice, related_name='locations', on_delete=models.CASCADE)
    title = models.CharField(max_length=180)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    hours = models.CharField(max_length=120, blank=True)
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Локація офісу'
        verbose_name_plural = 'Локації офісів'

    def __str__(self):
        return f'{self.office.code}: {self.title}'


class ContactInquiry(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=180)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Запит з форми'
        verbose_name_plural = 'Запити з форми'

    def __str__(self):
        return f'{self.subject} ({self.email})'
