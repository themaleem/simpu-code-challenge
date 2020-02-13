from django.contrib import admin
from django.urls import path,include
from rest_framework.documentation import include_docs_urls
from cc import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include([
        path('',views.ExcursionList.as_view(), name='api'),
        path('<int:pk>', views.SingleExcursion.as_view(), name='single_exc'),
        path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        path('docs/', include_docs_urls(title='SIMPU code-challenge API Build')) #api documentation
        ])
    ),
]
