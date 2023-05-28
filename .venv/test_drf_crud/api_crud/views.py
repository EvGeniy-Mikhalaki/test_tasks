from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TestCRUDItem, TestModel_2, TestModel_1, TestBorrowed, TestModelOtm_1, TestModelOtm_2
from .serializer import TestCRUDSerializer, ModelBorrowedSerializer, Model2Serializer, Model1Serializer

from rest_framework import serializers
from rest_framework import status

from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from django.http import HttpResponseRedirect, HttpResponseNotFound

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }
 
    return Response(api_urls)

@api_view(['POST'])
def add_items(request):
    item = TestCRUDSerializer(data=request.data)
    if TestCRUDItem.objects.filter(**request.data).exists(): # проверка уже существующих данных
        raise serializers.ValidationError('эти данные уже существуют!')
 
    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_items(request):
    # проверка параметров по URL-адресу
    if request.query_params: 
        items = TestCRUDItem.objects.filter(**request.query_params.dict())
    else:
        items = TestCRUDItem.objects.all()
 
    # если в элементах есть что-то еще то вызвать ошибку
    if items:
        serializer = TestCRUDSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_items(request, pk):
	item = TestCRUDItem.objects.get(pk=pk)
	data = TestCRUDSerializer(instance=item, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_items(request, pk):
    item = get_object_or_404(TestCRUDItem, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

# добавление начальных данных в таблицу 
def create_init_data():
      
     if TestModelOtm_1.objects.all().count() == 0:
          TestModelOtm_1.objects.create(name_model = "c0p0k1_1")
          TestModelOtm_1.objects.create(name_model = "c0p0k1_2")
          TestModelOtm_1.objects.create(name_model = "c0p0k1_3")

# получение данных из бд
def sample_index(request):
    testmodelotm2 = TestModelOtm_2.objects.all()
    return render(request, "sample_index.html", {"testmodelotm2": testmodelotm2})

# добавление данных в бд
def sample_create(request):
    create_init_data()
 
    # если запрос POST, сохраняем данные
    if request.method == "POST":
        _test_model_otm_2 = TestModelOtm_2()
        _test_model_otm_2.name_model = request.POST.get("name_model")
        _test_model_otm_2.just_int = request.POST.get("just_int")
        _test_model_otm_2.relation_to_what = request.POST.get("relation_to_what")
        _test_model_otm_2.save()
        return HttpResponseRedirect("/")
    # передаем данные в шаблон
    _test_model_otm_1 = TestModelOtm_1.objects.all()
    return render(request, "sample_create.html", {"_test_model_otm_1": _test_model_otm_1})

# изменение данных в бд
def sample_edit(request, id):
    try:
        _test_model_otm_2 = TestModelOtm_2.objects.get(id=id)
 
        if request.method == "POST":
            _test_model_otm_2.name_model = request.POST.get("name_model")
            _test_model_otm_2.just_int = request.POST.get("just_int")
            _test_model_otm_2.relation_to_what = request.POST.get("relation_to_what")
            _test_model_otm_2.save()
            return HttpResponseRedirect("/")
        else:
            _test_model_otm_1 = TestModelOtm_1.objects.all()
            return render(request, "sample_edit.html", {"_test_model_otm_2": _test_model_otm_2, "_test_model_otm_1": _test_model_otm_1})
    except TestModelOtm_2.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")
    
# удаление данных из бд
def sample_delete(request, id):
    try:
        _test_model_otm_2 = TestModelOtm_2.objects.get(id=id)
        _test_model_otm_2.delete()
        return HttpResponseRedirect("/")
    except _test_model_otm_2.DoesNotExist:
        return HttpResponseNotFound("<h2>Product not found</h2>")

# api_view Классы
class M1Viewset(viewsets.ModelViewSet):
    queryset = TestModel_1.objects.all()
    serializer_class = Model1Serializer

class M2Viewset(viewsets.ModelViewSet):
    queryset = TestModel_2.objects.all()
    serializer_class = Model2Serializer

class BorrowedViewset(viewsets.ModelViewSet):
    queryset = TestBorrowed.objects.all()
    serializer_class = ModelBorrowedSerializer