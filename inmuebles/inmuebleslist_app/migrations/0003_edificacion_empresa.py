# Generated by Django 3.2.8 on 2024-02-27 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0002_auto_20240227_1252'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='empresa',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='edificacion', to='inmuebleslist_app.empresa'),
            preserve_default=False,
        ),
    ]