from django.db import models

# Create your models here.


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.full_name} - {self.subject}"
    
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email