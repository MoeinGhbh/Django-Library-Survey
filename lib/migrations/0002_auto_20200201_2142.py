# Generated by Django 3.0.2 on 2020-02-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(choices=[('c', 'comedi'), ('c', 'culture'), ('e', 'enviroment'), ('s', 'sience')], default='s', help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=1),
        ),
    ]