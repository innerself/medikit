from django.contrib import admin

from .models import Kit, Medication


@admin.register(Kit)
class KitAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'kit', 'kit_user')

    def kit_user(self, obj):
        return obj.kit.user if isinstance(obj.kit, Kit) else "Shared kit"

    kit_user.short_description = 'Kit user'
