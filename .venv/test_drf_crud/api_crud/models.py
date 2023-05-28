from django.db import models

class TestCRUDItem(models.Model):
    test_field_1 = models.CharField(max_length=24)
    test_field_2 = models.CharField(max_length=24)
    test_field_3 = models.CharField(max_length=24)
    test_field_4 = models.PositiveIntegerField()
    
    def __str__(self) -> str:
        return self.test_field_1
    
class TestModel_1(models.Model):
    just_str_model_1 = models.CharField(max_length=24)
    
class TestModel_2(models.Model):
    just_str_model_2 = models.CharField(max_length=24)
    
class TestBorrowed(models.Model):
    _TestModel_1 = models.ForeignKey(TestModel_1, on_delete=models.CASCADE)
    _TestModel_2 = models.ForeignKey(TestModel_2, on_delete=models.CASCADE)
    when = models.DateTimeField(auto_now_add=True)
    returned = models.DateTimeField(null=True, blank=True)
    

class TestModelOtm_1(models.Model):
    name_model = models.CharField(max_length=34)
    
class TestModelOtm_2(models.Model):
    relation_to_what = models.ForeignKey(TestModelOtm_1, on_delete = models.CASCADE)
    name_model = models.CharField(max_length=34)
    just_int = models.IntegerField()