# Generated by Django 4.0.5 on 2022-06-13 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_account_open_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'SAVINGS'), (1, 'CREDIT')], default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='action',
            field=models.PositiveSmallIntegerField(choices=[(0, 'DEPOSIT'), (1, 'WITHDRAWAL')], default=0),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]