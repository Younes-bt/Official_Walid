# Generated by Django 5.1.3 on 2024-12-29 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_article_pdfid'),
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vidLink', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1500)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]