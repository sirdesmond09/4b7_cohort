# Generated by Django 4.0.1 on 2022-02-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=10, null=True)),
                ('song', models.CharField(max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
