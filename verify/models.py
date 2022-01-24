from django.db import models
from accounts.models import CustomUser
import random

# Create your models here.


class Code(models.Model):
    number = models.CharField(max_length=6, blank=True,)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

    def save(self, *arg, **kwargs):
        nums = [n for n in range(10)]
        code_items = []
        for i in range(6):
            num = random.choice(nums)
            code_items.append(num)
        code_str = ''.join(str(i) for i in code_items)
        self.number = code_str
        super().save(*arg, **kwargs)
