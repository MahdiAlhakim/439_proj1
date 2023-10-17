# Generated by Django 4.2.5 on 2023-09-15 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('profession', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
