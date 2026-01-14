from django.urls import path
from users.apps import UsersConfig
from users.views import (
    UserRegisterView,
    UserAccount,
    LogoutView,
    UserDeleteView,
    CookieToken, UserUpdateView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("reg/", UserRegisterView.as_view(), name="register"),
    path("login/", CookieToken.as_view(), name="token_obtain_pair"),
    path("account/", UserAccount.as_view(), name="my_account"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/delete/", UserDeleteView.as_view(), name="delete"),
    path('user/update/', UserUpdateView.as_view(), name='user-update')
]
