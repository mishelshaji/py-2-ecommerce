# Generated by Django 3.1.5 on 2021-01-07 09:42

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerDetails',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=10, unique=True, validators=[django.core.validators.MinLengthValidator(10)], verbose_name='Phone Number')),
                ('address', models.TextField(max_length=300, verbose_name='Address')),
                ('pin', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$', 'Invalid Pin Number')], verbose_name='Postal Code')),
                ('city', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3, 'Invalid city name')], verbose_name='City')),
                ('state', models.CharField(choices=[('Kerala', 'Kerala'), ('Karnataka', 'Karnataka')], default='Kerala', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
