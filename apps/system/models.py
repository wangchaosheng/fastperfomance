from django.db import models

from utils.base_models import BaseModel


class System(BaseModel):
    id = models.AutoField(verbose_name='系统id', primary_key=True, help_text='系统id')
    name = models.CharField('系统名称', max_length=50, unique=True, help_text='系统名称')
    annotation = models.TextField('备注', help_text='备注', max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'p_system'
        verbose_name = '系统信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

