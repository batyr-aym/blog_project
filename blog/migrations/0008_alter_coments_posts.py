# Generated by Django 5.1.5 on 2025-02-22 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_user_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coments',
            name='posts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coments', to='blog.posts'),
        ),
    ]
