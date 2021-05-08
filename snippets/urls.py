from django.urls import include, path
from rest_framework.routers import DefaultRouter

from snippets import views

# Create a default router and register the viewsets
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# The API urls are now determined automatically by the router
# Registering the viewsets with the router is similar to providing a urlpattern.
# We include two arguments - the URL prefix for the views, and the viewset itself.
# The DefaultRouter class we're using also automatically creates the API root view for us
urlpatterns = [
    path('', include(router.urls)),
]
