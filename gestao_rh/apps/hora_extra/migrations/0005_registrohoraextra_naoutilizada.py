# Generated by Django 2.1.5 on 2019-02-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hora_extra', '0004_registrohoraextra_utilizada'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='naoutilizada',
            field=models.BooleanField(default=False),
        ),
    ]
