from django.db import models
from django.contrib.auth.models import User

class ProjectNames(models.Model):
    project_name=models.CharField(max_length=150)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.project_name

    class Meta:
        verbose_name = 'Project Name'
        verbose_name_plural = 'Project Names'

class UserTasks(models.Model):
    employee=models.ForeignKey(User,on_delete=models.CASCADE)           # Relationship with auth.User Model
    projects=models.ForeignKey(ProjectNames,on_delete=models.CASCADE)    # Relation with ProjectNames Model
    task_title=models.CharField(max_length=200)
    start_time=models.CharField(max_length=200)
    end_time=models.CharField(max_length=200,blank=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.task_title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'