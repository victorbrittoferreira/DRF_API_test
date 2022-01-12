from django.contrib import admin
from django.urls import path
from core_api.views import(
    EmployeeListAPIView,
    EmployeeCreateAPIView, 
    EmployeeDetailAPIView, 
    EmployeeUpdateAPIView,
    EmployeeDestroyAPIView, 
    EmployeeCreateAPIView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # LIST all employees
    path("api/list-employee/", EmployeeListAPIView.as_view(), name="api-employee-list"),
    
    # CREATE a new employee
    path("api/create-employee/", EmployeeCreateAPIView.as_view(), name="api-create-employee"),
    
    # RETRIEVE a deleted employee
    path("api/retrieve-employee/<int:pk>", EmployeeDetailAPIView.as_view(), name="api-retrieve-employee"),
    
    # UPDATE employee's data
    path("api/update-employee/<int:pk>", EmployeeUpdateAPIView.as_view(), name="api-update-employee"),
    
    # DELETE an employee
    path("api/delete-employee/<int:pk>", EmployeeDestroyAPIView.as_view(), name="api-delete-employee"),
]




