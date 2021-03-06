# Generated by Django 2.1.1 on 2018-09-11 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name="Tweet's author")),
                ('content', models.CharField(max_length=50, verbose_name="Tweet's content")),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name="Tweet's creation timestamp")),
            ],
        ),
    ]
