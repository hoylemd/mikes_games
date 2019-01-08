from django.conf.urls import url

from .views import IndexView

app_name = 'minesweeper'
urlpatterns = [
    url(r'^minesweeper$', IndexView.as_view(), name="minesweeper")
]
