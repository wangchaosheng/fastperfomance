from django.db import models

from utils.base_models import BaseModel


class Interfaces(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    system= models.ForeignKey('system.System', on_delete=models.CASCADE, related_name='interfaces',
                                  help_text='系统id')
    name = models.CharField('接口名称', max_length=200, help_text='接口名称')
    request = models.TextField('请求数据', help_text='请求信息')
    path = models.CharField('接口路径', unique=True, help_text='接口路径', max_length=200)
    method = models.CharField('请求方式', help_text='请求方式', max_length=200)
    rig_id = models.IntegerField('网关api_id', help_text='网关api_id', null=True, blank=True)
    rig_env = models.IntegerField('网关环境', help_text='网关环境', null=True, blank=True)
    threads = models.IntegerField('线程数', help_text='线程数')
    rate = models.IntegerField('加压速率', help_text='加压速率')
    execution_time = models.IntegerField('执行时间', help_text='执行时间')
    latency_time = models.IntegerField('等待时间', help_text='等待时间')
    assertstr = models.CharField('断言', help_text='断言', max_length=50, null=True, blank=True)

    class Meta:
        db_table = 'p_interfaces'
        verbose_name = '接口信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
