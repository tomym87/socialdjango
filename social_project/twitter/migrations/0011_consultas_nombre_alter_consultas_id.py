# Generated by Django 4.0.6 on 2022-08-02 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0010_alter_consultas_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultas',
            name='nombre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.hijos'),
        ),
        migrations.AlterField(
            model_name='consultas',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
