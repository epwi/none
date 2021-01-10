# Generated by Django 3.1.4 on 2020-12-25 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'verbose_name': 'تیکت', 'verbose_name_plural': 'تیکت ها'},
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TMessages', to='App1.ticket', verbose_name='مربوط به تیکت'),
        ),
    ]
