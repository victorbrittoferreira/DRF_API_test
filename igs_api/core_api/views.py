from rest_framework import  generics, filters
from rest_framework.views import APIView
from core_api.models import Employee
from core_api.serializers import EmployeeSerializer
from django.shortcuts import render, redirect, reverse

#LIST
class EmployeeListAPIView(generics.ListAPIView):
    
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["employee_name", "email", "department"]
    
    
#CREATE
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDetailAPIView(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


#UPDATE
class EmployeeUpdateAPIView(generics.UpdateAPIView):
    queryset = Employee.objects.all().order_by("employee_name")
    serializer_class = EmployeeSerializer


#DESTROY
class EmployeeDestroyAPIView(generics.DestroyAPIView):

    queryset = Employee.objects.all().order_by("employee_name")
    serializer_class = EmployeeSerializer

# ERROR Handling

def error(request):
    context = {
    }
    return render(request, "api/error.html", context)
