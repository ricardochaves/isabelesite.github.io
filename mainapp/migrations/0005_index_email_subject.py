# Generated by Django 2.0.7 on 2018-09-05 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20180905_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='email_subject',
            field=models.CharField(help_text='Mais informações obre o tendimento.', max_length=30, null=True, verbose_name='Assunto do E-mail'),
        ),
    ]
