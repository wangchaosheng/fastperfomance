# Generated by Django 3.2.1 on 2021-12-23 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('system', '0001_initial'),
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectInterFaces',
            fields=[
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('creator', models.TextField(help_text='创建人', null=True, verbose_name='创建人')),
                ('updater', models.TextField(help_text='更新人', null=True, verbose_name='更新人')),
                ('is_delete', models.IntegerField(default=0, help_text='是否删除', null=True, verbose_name='是否删除')),
                ('id', models.AutoField(help_text='id主键', primary_key=True, serialize=False, verbose_name='id主键')),
                ('project', models.ForeignKey(help_text='项目id', on_delete=django.db.models.deletion.CASCADE, related_name='project_interfaces', to='projects.projects')),
                ('system', models.ForeignKey(help_text='系统id', on_delete=django.db.models.deletion.CASCADE, related_name='project_interfaces', to='system.system')),
            ],
            options={
                'verbose_name': '项目接口关系',
                'verbose_name_plural': '项目接口关系',
                'db_table': 'p_project_interfaces',
            },
        ),
    ]
