from django.db import models
from wangeditor.fields import WangRichTextField


class Article(models.Model):
    """
    前台用户模板
    """
    title = models.CharField(verbose_name='标题', max_length=100)
    author = models.CharField(verbose_name='作者', max_length=50)
    description = models.TextField(verbose_name='摘要')
    content = WangRichTextField(verbose_name='内容')
    views = models.IntegerField(verbose_name='浏览量', default=0)
    publish_time = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)

    class Meta:
        db_table = 'tb_article'
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name


class Image(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200, default=None)
    image = models.ImageField(verbose_name='上传图片', upload_to='')
    views = models.IntegerField(verbose_name='浏览量', default=0)
    publish_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        db_table = "tb_image"
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name


class Travel(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200)
    image = models.ImageField(verbose_name='上传图片', upload_to='')
    description = WangRichTextField(verbose_name='简介')
    views = models.IntegerField(verbose_name='浏览量', default=0)
    publish_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        db_table = 'tb_travel'
        verbose_name = '旅养'
        verbose_name_plural = verbose_name


class Video(models.Model):
    title = models.CharField(verbose_name="标题", max_length=200)
    description = WangRichTextField(verbose_name="摘要", blank=True)
    video_file = models.FileField(verbose_name="上传视频", upload_to='videos/')
    uploaded_at = models.DateTimeField(verbose_name="上传时间", auto_now_add=True)

    class Meta:
        db_table = 'tb_video'
        verbose_name = '视频'
        verbose_name_plural = verbose_name


class User(models.Model):
    """
    前台用户模板
    """
    username = models.CharField(verbose_name='用户名称', max_length=200)
    email = models.EmailField(verbose_name='邮箱')
    password = models.CharField(verbose_name="密码", max_length=32)
    register_time = models.DateTimeField(verbose_name='注册时间', auto_now_add=True)

    class Meta:
        db_table = "tb_user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
