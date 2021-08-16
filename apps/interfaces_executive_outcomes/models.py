from django.db import models

from utils.base_models import BaseModel


class ProjectExecutiveOutcomes(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    system = models.ForeignKey('system.System', on_delete=models.CASCADE, related_name='interface_executive_outcomes',
                               help_text='系统id')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name='interface_executive_outcomes',
                                help_text='项目id')
    execute_log = models.ForeignKey('execute_logs.ExecuteLogs', on_delete=models.CASCADE,
                                    related_name='interface_executive_outcomes',
                                    help_text='执行记录id')
    threads = models.IntegerField('线程数', help_text='线程数')
    average = models.CharField('平均数', max_length=200, help_text='平均数')
    median = models.CharField('中位数', max_length=200, help_text='中位数')
    ninety_percentile = models.CharField('90%百分位', max_length=200, help_text='90%百分位')
    ninety_five_percentile = models.CharField('95%百分位', max_length=200, help_text='95%百分位')
    ninety_nine_percentile = models.CharField('99%百分位', max_length=200, help_text='99%百分位')
    least_value = models.CharField('最小值', max_length=200, help_text='最小值')
    maximum_value = models.CharField('最大值', max_length=200, help_text='最大值')
    error_rate = models.CharField('平均数', max_length=200, help_text='平均数')
    tps = models.CharField('吞吐量', max_length=200, help_text='吞吐量')
    receives_traffic = models.CharField('接受流量', max_length=200, help_text='接受流量')
    send_traffic = models.CharField('发送流量', max_length=200, help_text='发送流量')

    class Meta:
        db_table = 'p_interface_executive_outcomes'
        verbose_name = '接口执行结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
