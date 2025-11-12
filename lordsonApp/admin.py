from django.contrib import admin

from lordsonApp.models import Banner


# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')