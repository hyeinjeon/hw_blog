# Generated by Django 3.2 on 2021-04-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=200)),
                ('blog_writer', models.CharField(max_length=100)),
                ('blog_date', models.DateTimeField()),
                ('blog_body', models.TextField()),
            ],
        ),
    ]
