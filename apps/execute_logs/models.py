from django.db import models

from utils.base_models import BaseModel


class ExecuteLogs(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    # project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name='execute_logs',
    #                             help_text='项目id')
    # account = models.CharField('执行人', max_length=50, help_text='执行人')
    interface_id = models.IntegerField('接口用例ID',help_text='接口用例ID')
    reportdata = models.TextField('报告数据', help_text='报告数据')

    class Meta:
        db_table = 'p_execute_logs'
        verbose_name = '执行记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
