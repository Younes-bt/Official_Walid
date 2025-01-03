# Generated by Django 5.1.3 on 2024-12-02 23:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_article_pdfurldownload_article_pdfurlview'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to=settings.AUTH_USER_MODEL),
        ),
    ]
