from django.db import models

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name     = models.CharField(max_length=100)
    last_name      = models.CharField(max_length=100)
    roll_number    = models.CharField(max_length=20, unique=True)
    email          = models.EmailField(unique=True)
    phone          = models.CharField(max_length=15, blank=True)
    gender         = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth  = models.DateField()
    course         = models.CharField(max_length=100)
    admission_date = models.DateField(auto_now_add=True)
    is_active      = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"