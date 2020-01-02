from django.db import models

#构建部门模型
class Department(models.Model):
    departmentname = models.CharField(max_length='64', unique=True)

#构建角色模型
class Role(models.Model):
    pass

# 构建用户模型
class User(models.Model):
    username = models.CharField(max_length='64', unique=True)
    employee_id = models.CharField(max_length='32', unique=True)
    pwd = models.CharField(max_length='128')
    realname = models.CharField(max_length='64')
    mobile = models.CharField(max_length='16', blank=True)
    email = models.EmailField()
    department_id = models.ForeignKey(Department)
    role_id = models.ForeignKey(Role)

    def __str__(self):
        return self.username



