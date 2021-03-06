# Generated by Django 2.1.7 on 2019-04-06 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bpapp', '0002_auto_20190406_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='bp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='node',
            name='fp',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='problem',
            name='root',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='problem', to='bpapp.Node'),
        ),
    ]
