# Generated by Django 2.2.12 on 2020-05-12 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djstripe', '0007_auto_20200507_1913'),
        ('plans', '0006_auto_20200511_1823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerplan',
            name='default_payment_method',
        ),
        migrations.AddField(
            model_name='order',
            name='charge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Charge'),
            preserve_default=False,
        ),
    ]