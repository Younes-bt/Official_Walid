# Generated by Django 5.1.3 on 2024-12-02 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pdfUrlDownload',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='pdfUrlView',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]