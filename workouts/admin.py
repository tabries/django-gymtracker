from django.contrib import admin
from .models import User, Routine, Exercise, History

# admin.site.register(User)
admin.site.register(Routine)
admin.site.register(Exercise)
admin.site.register(History)