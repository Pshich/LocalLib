# Generated by Django 3.1.5 on 2021-01-28 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=200)),
                ('books', models.ManyToManyField(help_text='Select language', to='catalog.Book')),
            ],
        ),
    ]
