from django.db import models

from utils.base_models import BaseModel


class Projects(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    system = models.ForeignKey('system.System', on_delete=models.CASCADE, related_name='projects', help_text='系统id')
    name = models.CharField(verbose_name='项目名称', max_length=50, help_text='项目名称')
    include = models.TextField('包含的接口', help_text='包含的接口')
    creator = models.CharField(verbose_name='创建人', max_length=50, help_text='创建人')
    updater = models.CharField(verbose_name='更新人', max_length=50, help_text='更新人')
    desc = models.CharField(verbose_name='简要描述', max_length=200, null=True, blank=True, default='', help_text='简要描述')

    class Meta:
        db_table = 'p_projects'
        verbose_name = '项目信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
