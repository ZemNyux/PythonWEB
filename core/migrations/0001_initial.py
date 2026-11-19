import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyPrinciple',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Принцип',
                'verbose_name_plural': 'Принципи',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='CompanyStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=32)),
                ('label', models.CharField(max_length=120)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Показник',
                'verbose_name_plural': 'Показники',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ContactInquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=180)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Запит з форми',
                'verbose_name_plural': 'Запити з форми',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ContactOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('flag', models.CharField(blank=True, max_length=8)),
                ('short_desc', models.TextField()),
                ('page_title', models.CharField(max_length=255)),
                ('page_lead', models.TextField()),
                ('related_branch_slug', models.SlugField(blank=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Представництво',
                'verbose_name_plural': 'Представництва',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('published_on', models.DateField()),
                ('category', models.CharField(max_length=64)),
                ('badge_class', models.CharField(choices=[('badge-primary', 'Primary'), ('badge-success', 'Success'), ('badge-info', 'Info'), ('badge-warning', 'Warning')], default='badge-primary', max_length=32)),
                ('summary', models.TextField()),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Новина',
                'verbose_name_plural': 'Новини',
                'ordering': ['-published_on', '-id'],
            },
        ),
        migrations.CreateModel(
            name='ServiceDirection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('icon', models.CharField(blank=True, max_length=16)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Напрямок діяльності',
                'verbose_name_plural': 'Напрямки діяльності',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('role', models.CharField(max_length=180)),
                ('bio', models.TextField()),
                ('initials', models.CharField(max_length=4)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Член керівництва',
                'verbose_name_plural': 'Керівництво',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='ContactLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=180)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('hours', models.CharField(blank=True, max_length=120)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='core.contactoffice')),
            ],
            options={
                'verbose_name': 'Локація офісу',
                'verbose_name_plural': 'Локації офісів',
                'ordering': ['sort_order', 'id'],
            },
        ),
    ]
