from django.contrib import admin
from .models import Student

class AdminStudent(admin.ModelAdmin):
    def name(self, obj):
        return str(obj)
    name.short_description = 'Name'

    def verified(self, obj):
        return obj.otp == ''
    verified.boolean = True
    verified.short_description = 'OTP Verified'

    def is_active(self, obj):
        return obj.user.is_active
    is_active.boolean = True
    is_active.short_description = 'Active'

    list_display = ('name', 'branch', 'verified', 'is_active')

    def deactivate(self, request, queryset):
        for student in queryset:
            student.user.is_active = False
            student.user.save()
    deactivate.short_description = 'Deactivate selected users'

    def activate(self, request, queryset):
        for student in queryset:
            student.user.is_active = True
            student.user.save()
    activate.short_description = 'Activate selected users'

    actions = [deactivate, activate]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    search_fields = ['user__first_name', 'user__last_name', 'roll_no', 'branch']

admin.site.register(Student, AdminStudent)