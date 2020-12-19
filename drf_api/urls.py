from django.contrib import admin
from django.urls import path, include
from core.views import test
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', test.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name = 'abtain-token')
]
