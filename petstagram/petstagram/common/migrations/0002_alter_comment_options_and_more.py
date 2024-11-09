# Generated by Django 5.1.2 on 2024-11-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_time_of_publication']},
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['date_time_of_publication'], name='common_comm_date_ti_d3f02d_idx'),
        ),
    ]