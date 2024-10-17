from django.urls import path
from .views import EtudiantinscripView, CoursListView, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Etudiantinscrip/', EtudiantinscripView.as_view(), name='Etudiantinscrip'),
    path('courses/', CoursListView.as_view(), name='cours-list'),
    path('profile/', ProfileView.as_view(), name='etudiant-profile'),
]
#gérer les fichiers médias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)