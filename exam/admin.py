from django.contrib import admin


class UserModel(admin.ModelAdmin):
    list_display = ['name', 'age ', 'salary']
    list_filter = ['created_at']
    search_fields = ['name']
