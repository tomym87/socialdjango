# Generated by Django 4.0.6 on 2022-08-02 21:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('twitter', '0007_alter_hijos_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='consultas',
            fields=[
                ('tipo', models.IntegerField(default=0, max_length=5)),
                ('fecha', models.DateField(auto_now=True)),
                ('talla', models.CharField(blank=True, default='talla', max_length=20)),
                ('peso', models.CharField(blank=True, default='peso', max_length=20)),
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('recomendacion', models.CharField(default='Recomendacion', max_length=200)),
                ('dato1', models.CharField(default='dato1', max_length=100)),
                ('dato2', models.CharField(default='dato2', max_length=100)),
                ('dato3', models.CharField(default='dato3', max_length=100)),
            ],
        ),
    ]
