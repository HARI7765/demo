from django.db import models

class UserProfile(models.Model):
    # Name field (string)
    name = models.CharField(max_length=255)
    
    # Email field (email type)
    email = models.EmailField(unique=True)
    
    # Phone number field (string-based for flexibility)
    phone = models.CharField(max_length=15)  # using CharField for flexibility
    
    # Date of birth field
    dob = models.DateField(default='2000-01-01')  # Example default date

    def __str__(self):
        return self.name
