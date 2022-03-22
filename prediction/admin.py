from django.contrib import admin
from .models import Horizon, MLModel, FitResults


class MLModelAdmin(admin.ModelAdmin):
    list_display = ['code', 'fullname', 'algorithm', 'last_fit']
    ordering = ['code']
    list_filter = ['algorithm']


admin.site.register(Horizon)
admin.site.register(FitResults)
admin.site.register(MLModel, MLModelAdmin)
