# Generated by Django 2.1.9 on 2019-07-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_cloudinformation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloudinformation',
            name='aws_id',
            field=models.CharField(blank=True, default=None, max_length=60, null=True),
        ),
    ]