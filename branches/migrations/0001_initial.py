from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=180)),
                ('city', models.CharField(max_length=80)),
                ('tag', models.CharField(max_length=64)),
                ('focus', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('established', models.PositiveIntegerField()),
                ('specialization', models.CharField(max_length=255)),
                ('page_title', models.CharField(max_length=180)),
                ('page_lead', models.TextField()),
                ('detail_intro', models.TextField()),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Філія',
                'verbose_name_plural': 'Філії',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='CompanyFact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('badge', models.CharField(max_length=32)),
                ('title', models.CharField(max_length=180)),
                ('text', models.TextField()),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Факт',
                'verbose_name_plural': 'Факти',
                'ordering': ['sort_order', 'id'],
            },
        ),
        migrations.CreateModel(
            name='HistoryEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=16)),
                ('event', models.TextField()),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Історична подія',
                'verbose_name_plural': 'Історичні події',
                'ordering': ['sort_order', 'id'],
            },
        ),
    ]
