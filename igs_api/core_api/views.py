from django.shortcuts import render, redirect, reverse
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework import viewsets, generics, filters
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import JsonResponse, HttpResponse
#from core_api.models import Employee

#LIST
class EmployeeListAPIView(generics.ListAPIView):
    queryset = Employee.objects.all().order_by("employee_name","email", "department")
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    #search_fields = ["employee_name","email", "department"]


#class EmployeeListAPI(APIView):
#
#    def get(self, request):
#
#        employee = Employee.objects.all()
#        serializer = EmployeeSerializer(employee, many = True)
#
#        return Response(serializer.data)

#CREATE
class EmployeeCreateAPIView(generics.CreateAPIView):
    queryset = Employee.objects.all().order_by("employee_name","email", "department")
    #queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

#UPDATE

class EmployeeUpdateAPIView(generics.UpdateAPIView):
    #queryset = Employee.objects.all().order_by("-id")
    queryset = Employee.objects.all().order_by("-id")
    serializer_class = EmployeeSerializer


#DESTROY

class EmployeeDestroyAPIView(generics.DestroyAPIView):




    def get_object(self, id):
        employee = get_object_or_404(Employee, id=id)
        return employee

    queryset = Employee.objects.all().order_by("employee_name","email", "department")
    #queryset = Employee.objects.all().order_by
    serializer_class = EmployeeSerializer


#class EmployeeDeleteAPI(APIView):
#
#    def get_object(self, id):
#        employee = get_object_or_404(Employee, id=id)
#        return employee
#
#    def get(self, request, id):
#
#        try:
#            employee = Employee.objects.get(id=id)
#            employee.delete()
#
#            return redirect(reverse('api-employee-list'))
#
#        except:
#            return redirect(reverse('error'))


