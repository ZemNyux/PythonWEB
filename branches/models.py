from django.db import models
from django.urls import reverse


class Branch(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=180)
    city = models.CharField(max_length=80)
    tag = models.CharField(max_length=64)
    focus = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=64)
    email = models.EmailField()
    established = models.PositiveIntegerField()
    specialization = models.CharField(max_length=255)
    page_title = models.CharField(max_length=180)
    page_lead = models.TextField()
    detail_intro = models.TextField()
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Філія'
        verbose_name_plural = 'Філії'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('branch_detail', kwargs={'slug': self.slug})


class HistoryEvent(models.Model):
    year = models.CharField(max_length=16)
    event = models.TextField()
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Історична подія'
        verbose_name_plural = 'Історичні події'

    def __str__(self):
        return f'{self.year}'


class CompanyFact(models.Model):
    badge = models.CharField(max_length=32)
    title = models.CharField(max_length=180)
    text = models.TextField()
    sort_order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Факт'
        verbose_name_plural = 'Факти'

    def __str__(self):
        return self.title
