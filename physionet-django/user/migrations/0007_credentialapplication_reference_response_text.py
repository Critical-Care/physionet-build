# Generated by Django 2.1.7 on 2019-03-19 19:35

from django.db import migrations, models
import user.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190314_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentialapplication',
            name='reference_response_text',
            field=models.CharField(blank=True, default='', max_length=500, validators=[user.validators.validate_alphaplusplus]),
        ),
    ]
