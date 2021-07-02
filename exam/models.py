from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=50, null=True, )
    age = models.IntegerField(null=False)
    salary = models.FloatField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
