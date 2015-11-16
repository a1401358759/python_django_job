#coding:utf8
from django import forms

class Shop_form(forms.Form):
    name = forms.CharField(max_length=30,label='商品名称')
    price = forms.FloatField(label='商品价格')
    date = forms.DateField(label='出厂日期')
    address = forms.CharField(max_length=50,label='产地')
    expiration_time = forms.IntegerField(label='保质期')
    discribe = forms.CharField(widget=forms.Textarea,label='商品描述')

    def clean_expiration_time(self):
        expiration = self.cleaned_data['expiration_time']
        num = int(expiration)
        if num < 0:
            raise forms.ValidationError("expiration must biger than 0")
        return expiration


class D_form(forms.Form):
    adress = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=20)
    user_name = forms.CharField(max_length=20)
    
class Buy_form(forms.Form):
    shopping_id = forms.IntegerField()
    shoping_number = forms.IntegerField()
    shoping_price = forms.FloatField()
    Ding_id = forms.IntegerField()

