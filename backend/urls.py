"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from listings.view import ListingList as listings_api_views
from listings.view import ListingCreate as listings_api_views2
from listings.view import ListingDetail as listings_api_views3
from listings.view import ListingDelete as listings_api_views4
from listings.view import ListingUpdate as listings_api_views5
from users import view as users_api_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('api/listings/', listings_api_views.as_view()),
                  path('api/listings/create/', listings_api_views2.as_view()),
                  path('api/listings/<int:pk>/', listings_api_views3.as_view()),
                  path('api/listings/<int:pk>/delete/', listings_api_views4.as_view()),
                  path('api/listings/<int:pk>/update/', listings_api_views5.as_view()),
                  path('api/profiles/', users_api_view.ProfileList.as_view()),
                  path('api/profiles/<int:seller>/', users_api_view.ProfileDetail.as_view()),
                  path('api/profiles/<int:seller>/update/', users_api_view.ProfileUpdate.as_view()),
                  path('api_auth_djoser/', include('djoser.urls')),
                  path('api_auth_djoser/', include('djoser.urls.authtoken')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)
