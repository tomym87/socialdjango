# Generated by Django 4.0.6 on 2022-08-02 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0012_alter_consultas_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='pic',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
