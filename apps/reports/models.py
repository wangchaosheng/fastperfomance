from django.db import models

from utils.base_models import BaseModel


class Reports(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    name = models.CharField(verbose_name='报告名称', max_length=200, unique=True, help_text='报告名称')
    path = models.URLField(verbose_name='报告文件地址', max_length=200, help_text='报告文件地址')  # 1为成功, 0为失败
    interface_execute = models.ForeignKey('interfaces_executive_outcomes.ProjectExecutiveOutcomes',
                                          on_delete=models.CASCADE,
                                          help_text='所属接口执行结果id', related_name='reports')

    class Meta:
        db_table = 'p_reports'
        verbose_name = '测试报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
