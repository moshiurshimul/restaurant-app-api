from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user_account.views import UserRegistrationView, UserUpdateView, UserLogoutView, UserChangePasswordView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('reg/', UserRegistrationView.as_view()),
    path('update/', UserUpdateView.as_view()),
    path('change-password/', UserChangePasswordView.as_view()),
    path('logout/', UserLogoutView.as_view()),

]
