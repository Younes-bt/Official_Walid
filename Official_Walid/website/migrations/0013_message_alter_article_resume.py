# Generated by Django 5.1.3 on 2025-01-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_article_downloadcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=300)),
                ('emailPhone', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='resume',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]
