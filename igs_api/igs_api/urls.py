from django.contrib import admin
from django.urls import path
#from core_api.views import EmployeeListAPIView,  EmployeeCreateAPIView
from core_api.views import EmployeeListAPIView, EmployeeCreateAPIView, EmployeeUpdateAPIView, EmployeeDestroyAPIView, EmployeeCreateAPIView


urlpatterns = [
    path('admin/', admin.site.urls),
    # List
    path("api/list-employee", EmployeeListAPIView.as_view(), name="api-employee-list"),
    # Create
    path("api/create-employee/", EmployeeCreateAPIView.as_view(), name="api-create-employee"),
    # Update
    path("api/update-employee/", EmployeeUpdateAPIView.as_view(), name="api-create-employee"),
    # Delete
    path("api/delete-employee/", EmployeeDestroyAPIView.as_view(), name="api-delete-employee"),
    ]


#from django.contrib import admin
#from django.urls import path, include
#from rest_framework.routers import DefaultRouter
#from core_api import views
#
#router = DefaultRouter()
#router.register(r"core_api", views.EmployeeListAPI, "Employee")


