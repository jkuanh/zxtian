from django.db import models


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



