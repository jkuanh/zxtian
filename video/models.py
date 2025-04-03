from django.db import models
from wangeditor.fields import WangRichTextField


class Video(models.Model):
    title = models.CharField(verbose_name="标题", max_length=200)
    description = WangRichTextField(verbose_name="摘要", blank=True)
    video_file = models.FileField(verbose_name="上传视频", upload_to='videos/')
    uploaded_at = models.DateTimeField(verbose_name="上传时间", auto_now_add=True)

    class Meta:
        db_table = 'tb_video'
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
