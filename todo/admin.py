from django.contrib import admin
from .models import Task 

class TaskAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "due_time","image_display", "importance", "completed")
    list_filter = ("completed", "importance")  # les champs sur lesquels on peut utiliser le filtre de droite
    search_fields = ("^name", "description")  # Les champs à partir desquels on peut effectuer des recherches dans la barre de recherche

    def image_display(self, obj):
        return '<img src="%s" width="50" height="50" />' % obj.image.url if obj.image else ''
    
    image_display.allow_tags = True
    image_display.short_description = 'Image'

admin.site.register(Task, TaskAdmin)
