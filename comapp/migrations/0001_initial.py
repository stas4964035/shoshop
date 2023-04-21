# Generated by Django 3.0.3 on 2023-04-21 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='название компании')),
                ('image', models.ImageField(blank=True, upload_to='com_img')),
                ('short_desc', models.TextField(blank=True, max_length=60, verbose_name='краткое описание компании')),
                ('description', models.TextField(blank=True, verbose_name='описание компании')),
                ('is_active', models.BooleanField(default=True, verbose_name='активна')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ListOfCountries')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Regions')),
            ],
        ),
    ]
