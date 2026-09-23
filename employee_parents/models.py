from django.db import models


class EmployeeParent(models.Model):
    employee_name = models.CharField(max_length=120)
    employee_id = models.CharField(max_length=50, unique=True)
    father_name = models.CharField(max_length=120, blank=True)
    mother_name = models.CharField(max_length=120, blank=True)
    guardian_name = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True)
    relation = models.CharField(max_length=50, default='Parent')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['employee_name']
        verbose_name = 'Employee Parent'
        verbose_name_plural = 'Employee Parents'

    def __str__(self):
        return f'{self.employee_name} ({self.employee_id})'
