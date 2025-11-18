from django.db import models

# Create your models here.
class contactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # Optional image uploaded with the contact message; stored in 'contact_images/' directory
    image = models.ImageField(upload_to=' contact_images/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
