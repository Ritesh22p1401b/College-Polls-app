# Generated by Django 4.0.2 on 2022-07-11 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.position'),
        ),
    ]
