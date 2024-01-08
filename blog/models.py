from django.db import models

Kurslar = (
    ("backend", "backend"),
    ("frontend", "frontend"),
    ("mobile", "mobile"),
    ("robot", "robot")
)


class Registration(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    kurs = models.CharField(max_length=8, choices=Kurslar)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return f"{self.ism} {self.familiya} - {self.kurs}"


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
