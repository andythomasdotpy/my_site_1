# Generated by Django 4.1.1 on 2022-11-28 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_1', '0003_alter_author_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='blog_1.tag'),
        ),
    ]
