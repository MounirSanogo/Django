from django.urls import path
from .views import TuteurinscripView, TeacherCourseListCreateView, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Tuteurinscrip/', TuteurinscripView.as_view(), name='Tuteurinscrip'),
    path('cours/', TeacherCourseListCreateView.as_view(), name='teacher-cours-list'),
    path('profile/', ProfileView.as_view(), name='tuteur-profile'),
]
#gérer les fichiers médias
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)