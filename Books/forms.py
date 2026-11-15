from django import forms

from .models import Book , Category


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['name']


        widgest = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),

        }



class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title' , 
            'author' ,
            'pages', 
            'price' , 
            'categoer',
            'photo_book',
            'photo_author',
            'rental_price_day',
            'rental_period', 
            'rental_total',    
            'status',
        ] 
        widgets = {

        'title' : forms.TextInput(attrs={'class': 'form-control'}),
        'author' : forms.TextInput(attrs={'class': 'form-control'}),
        'pages' : forms.NumberInput(attrs={'class': 'form-control'}),
        'price': forms.NumberInput(attrs={'class': 'form-control'}),
        'categoer' : forms.Select(attrs={'class': 'form-control'}),
        'photo_book' : forms.FileInput(attrs={'class': 'form-control'}),
        'photo_author' : forms.FileInput(attrs={'class': 'form-control'}),
        'rental_price_day' : forms.NumberInput(attrs={'class': 'form-control', 'id' : 'rentalpriceday'}),
        'rental_period' : forms.NumberInput(attrs={'class': 'form-control', 'id' : 'rentalperiod'}),
        'rental_total' : forms.NumberInput(attrs={'class': 'form-control', 'id' : 'rentaltotal'}),
        'status' : forms.Select(attrs={'class': 'form-control'}),


        
        }


