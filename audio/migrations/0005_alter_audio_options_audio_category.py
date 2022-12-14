# Generated by Django 4.0.5 on 2022-08-03 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_audio_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='audio',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='audio',
            name='category',
            field=models.CharField(blank=True, choices=[(1, 'Sunday Sermons'), (2, 'Bible Studies'), (3, 'Thursday Prayers'), (4, 'E-Library')], max_length=100),
        ),
    ]
