# Generated by Django 5.0.2 on 2024-03-15 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bizease_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('a_id', models.AutoField(primary_key=True, serialize=False)),
                ('a_email', models.CharField(blank=True, max_length=30, null=True)),
                ('a_password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
    ]
