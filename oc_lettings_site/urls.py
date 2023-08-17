from django.contrib import admin
from django.urls import path

import lettings.views
import profiles.views
# from . import views

# Fonction pour déclancher une erreur 500
def trigger_error(request):
  division_by_zero = 1 / 0

urlpatterns = [
    path('', lettings.views.index, name='index'),
    path('lettings/', lettings.views.lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings.views.letting, name='letting'),
    path('profiles/', profiles.views.profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profiles.views.profile, name='profile'),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),

]
