# Generated by Django 3.2.4 on 2021-06-10 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_language', models.CharField(help_text='Укажите языки книг', max_length=200)),
            ],
        ),
    ]
