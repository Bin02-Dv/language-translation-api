# Generated by Django 5.0.1 on 2024-01-04 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_language', models.CharField(max_length=10)),
                ('target_language', models.CharField(max_length=10)),
                ('source_text', models.TextField()),
                ('translated_text', models.TextField()),
            ],
        ),
    ]
