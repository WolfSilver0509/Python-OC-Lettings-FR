from django.contrib import admin

from lettings.models import Letting, Addresse
from .models import Profile


admin.site.register(Letting)
admin.site.register(Addresse)
admin.site.register(Profile)
