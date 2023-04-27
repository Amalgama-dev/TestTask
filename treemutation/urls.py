from django.contrib import admin
from django.urls import path
from main.views import ParaphraseView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paraphrase', ParaphraseView.as_view())
]
