# Generated by Django 4.2.6 on 2024-01-26 20:20

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='code',
            name='markdown',
        ),
        migrations.AddField(
            model_name='code',
            name='text',
            field=django_ckeditor_5.fields.CKEditor5Field(default='Hello World!', verbose_name='Text'),
            preserve_default=False,
        ),
    ]
