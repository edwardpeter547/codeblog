# Generated by Django 4.0.5 on 2022-06-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitename', models.CharField(max_length=255)),
                ('created_by', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('website', models.CharField(max_length=255, null=True)),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Website Settings',
            },
        ),
    ]
