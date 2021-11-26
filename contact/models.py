from django.db import models


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField(max_length=13)
    business_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created_at')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
