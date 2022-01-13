from django.db import models


class Employee(models.Model):

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        ordering = ["id"]

    employee_name = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=254,)
    department = models.CharField(max_length=255, null=False, blank=False)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#{}".format(self.external_key)

