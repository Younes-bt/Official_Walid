# Generated by Django 5.1.3 on 2025-01-02 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_message_alter_article_resume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='emailPhone',
            new_name='email_or_phone',
        ),
    ]
