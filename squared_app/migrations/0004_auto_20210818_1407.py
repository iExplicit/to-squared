# Generated by Django 3.2.6 on 2021-08-18 08:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('squared_app', '0003_alter_squared_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squared',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='squared',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='squared',
            name='done',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='squared',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
