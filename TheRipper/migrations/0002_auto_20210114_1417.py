# Generated by Django 3.1.4 on 2021-01-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TheRipper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
