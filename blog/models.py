from django.db import models

Kurslar = (
    ("backend", "backend"),
    ("frontend", "frontend"),
<<<<<<< HEAD
    ("mobile", "mobile"),
    ("robot", "robot")
)


=======
    ("mobile", "mobile")
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


>>>>>>> 38ac1d8 (Bug fixed)
class Registration(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    kurs = models.CharField(max_length=8, choices=Kurslar)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< HEAD
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    
=======
    target = models.ForeignKey(Target, on_delete=models.SET_NULL, null=True, blank=True, related_name='target_lid')

>>>>>>> 38ac1d8 (Bug fixed)
    def __str__(self):
        return f"{self.ism} {self.familiya} - {self.kurs}"


class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
<<<<<<< HEAD
        return self.title
=======
        return self.title
>>>>>>> 38ac1d8 (Bug fixed)
