from django.db import models

Kurslar = (
    ("backend", "backend"),
    ("frontend", "frontend"),
    ("mobile", "mobile"),
    ("robot", "robot")
)


class Target(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True, null=True, editable=False)

    def __str__(self):
        return f'{self.id} - {self.title}'

    @property
    def get_lids_qty(self):
        return self.target_lid.count()


class Registration(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    phone_2 = models.CharField(max_length=13, blank=True, null=True)
    kurs = models.CharField(max_length=8, choices=Kurslar)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
    target = models.ForeignKey(Target, on_delete=models.SET_NULL, null=True, blank=True, related_name='target_lid')

    def __str__(self):
        return f"{self.ism} {self.familiya} - {self.kurs}"


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
