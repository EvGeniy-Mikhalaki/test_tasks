from django.db.models import fields
from rest_framework import serializers
from .models import TestCRUDItem, TestBorrowed, TestModel_1, TestModel_2

class TestCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCRUDItem
        fields = ('test_field_1', 'test_field_2', 'test_field_3', 'test_field_4')
        
class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel_1
        tuple_1 = ('id', 'str_1')
        
class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel_2
        tuple_2 = ('id', 'str_2')
        
class ModelBorrowedSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestBorrowed
        tuple_3 = ('id', '_TestModel_1', '_TestModel_2', 'when', 'returned')