from django.db import models

from utils.base_models import BaseModel


class ProjectInterFaces(BaseModel):
    id = models.AutoField(verbose_name='id主键', primary_key=True, help_text='id主键')
    system = models.ForeignKey('system.System', on_delete=models.CASCADE, related_name='project_interfaces',
                               help_text='系统id')
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, related_name='project_interfaces',
                                help_text='项目id')

    class Meta:
        db_table = 'p_project_interfaces'
        verbose_name = '项目接口关系'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
