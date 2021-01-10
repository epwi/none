from django.urls import path
from .views import UserLogin, UserLogout, nothing

app_name = 'accounts'

urlpatterns = [
	path('login/', UserLogin, name="login"),
	path('logout/', UserLogout, name="logout"),
	path('nothing/', nothing, name="nothing"),
]