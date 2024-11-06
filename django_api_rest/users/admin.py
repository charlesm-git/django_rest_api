from django.contrib import admin
from users.models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "date_of_birth",
        "can_be_contacted",
        "can_data_be_shared",
    )


admin.site.register(User, UserAdmin)
