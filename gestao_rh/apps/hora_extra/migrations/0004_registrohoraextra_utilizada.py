# Generated by Django 2.1.5 on 2019-02-07 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hora_extra', '0003_registrohoraextra_horas'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrohoraextra',
            name='utilizada',
            field=models.BooleanField(default=False),
        ),
    ]