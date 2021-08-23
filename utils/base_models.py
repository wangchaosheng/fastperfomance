from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间', help_text='更新时间')
    creator = models.TextField('创建人', null=True, help_text='创建人')
    updater = models.TextField('更新人', null=True, help_text='更新人')
    is_delete = models.IntegerField('是否删除', null=True, help_text='是否删除', default=0)

    class Meta:
        # 指定在迁移时不创建表
        abstract = True
