from django.db import models

class RequestInfo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    content = models.TextField()
    link = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)


