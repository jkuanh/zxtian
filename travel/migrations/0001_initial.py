# Generated by Django 3.2.15 on 2025-03-15 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='标题')),
                ('image', models.ImageField(upload_to='', verbose_name='上传图片')),
                ('description', models.TextField(verbose_name='简介')),
                ('views', models.IntegerField(default=0, verbose_name='浏览量')),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
            ],
            options={
                'verbose_name': '旅养',
                'verbose_name_plural': '旅养',
                'db_table': 'tb_travel',
            },
        ),
    ]
