# Generated by Django 4.2.6 on 2024-03-05 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0016_alter_code_snippet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='snippet_image',
            field=models.URLField(default='https://i.pinimg.com/564x/bb/42/d1/bb42d137e3ad0bbcc44bc37e1c8ad00e.jpg'),
        ),
    ]