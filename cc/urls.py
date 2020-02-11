from django.urls import path
from cc import views
from rest_framework_simplejwt import views as jwt_views
app_name='cc'

urlpatterns = [
    # path('',views.hello,name='hello'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.HelloView.as_view(), name='hello'),
]
