from django.db import models
from wangeditor.fields import WangRichTextField


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
