# Generated by Django 4.0.2 on 2022-07-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_controlvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='total_vote',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
    ]