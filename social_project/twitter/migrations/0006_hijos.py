# Generated by Django 4.0.6 on 2022-08-02 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_alter_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hijos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='nombre', max_length=50)),
                ('sexo', models.BooleanField(default=True)),
                ('tipo', models.CharField(default='nino', max_length=30)),
                ('profile_pic', models.ImageField(default='default.png', upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.profile')),
            ],
        ),
    ]
