# Generated by Django 2.1.7 on 2019-10-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0014_opportunity_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='visible',
            field=models.BooleanField(default=False, help_text='Is the material currently visible?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opportunity',
            name='visible',
            field=models.BooleanField(default=False, help_text='Is the opportunity currently visible'),
        ),
        migrations.AlterField(
            model_name='opportunity',
            name='image',
            field=models.ImageField(blank=True, help_text='Image displayed for the opportunity', upload_to=''),
        ),
    ]
