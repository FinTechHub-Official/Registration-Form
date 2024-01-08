from django.contrib import admin
from .models import Registration, Banner
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class RegistrationResource(resources.ModelResource):
    class Meta:
        model = Registration
        fields = ("phone", "ism", "familiya", "kurs", "created_at", "updated_at",)


admin.site.register(Banner)

@admin.register(Registration)
class RegistrationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RegistrationResource
    list_display = ("id", "phone", "ism", "familiya", "kurs", "note", "created_at", "updated_at")

