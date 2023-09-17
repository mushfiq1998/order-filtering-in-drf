from .models import Student
from .serializers import StudentSerializer 
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter

class StudentList(ListAPIView): 
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # It performs ordering filter based on all fields
    # Because we have not specified any filed
    filter_backends = [OrderingFilter]

    # performs ordering filter based on name field
    # ordering_fields = ['name']

    # performs ordering filter based on name and city fields
    ordering_fields = ['name', 'city']
