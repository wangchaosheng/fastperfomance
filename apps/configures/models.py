from django.db import models

from utils.base_models import BaseModel


class Configures(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    project = models.ForeignKey('projects.Projects',
                                on_delete=models.CASCADE,
                                related_name='configures',
                                help_text='所属接口')
    threads = models.IntegerField('线程数', help_text='线程数')
    rate = models.IntegerField('加压速率', help_text='加压速率')
    latency_time = models.IntegerField('等待时间', help_text='等待时间')
    execution_time = models.IntegerField('执行时间', help_text='执行时间')

    class Meta:
        db_table = 'p_configures'
        verbose_name = '配置信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
