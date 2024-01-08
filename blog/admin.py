from django.contrib import admin
<<<<<<< HEAD
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

=======
from .models import Registration, Banner, Target


admin.site.register(Registration)
admin.site.register(Banner)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'get_lids_qty', 'link')
    list_display_links = ('id', 'link')
>>>>>>> 38ac1d8 (Bug fixed)
