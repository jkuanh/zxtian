from django.db import models


class Image(models.Model):
    title = models.CharField(verbose_name='标题', max_length=200, default=None)
    image = models.ImageField(verbose_name='上传图片', upload_to='')
    views = models.IntegerField(verbose_name='浏览量', default=0)
    publish_time = models.DateTimeField(verbose_name='上传时间', auto_now_add=True)

    class Meta:
        db_table = "tb_image"
        verbose_name = '图片列表'
        verbose_name_plural = verbose_name
