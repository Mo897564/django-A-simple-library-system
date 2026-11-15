from django.shortcuts import redirect, render , get_object_or_404

from .models import *
from .forms import *


# Create your views here.




def index(request):

    if request.method == 'POST':
        add_book = BookForm(request.POST , request.FILES)
        if add_book.is_valid():
            add_book.save()
            return redirect ('index')

    else :
        add_book = BookForm() 


    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect ('index')
        
    else :
        add_cat = CategoryForm() 



    Context = { 
        'bookss' : Book.objects.all() ,
        'Category' : Category.objects.all()[:5],  
        'form' :  add_book,
        'formcat' :  add_cat,
        'allbooks' : Book.objects.filter(active = True).count(),   
        'book_Sold' : Book.objects.filter(status = 'تم بيعة').count(),
        'book_renter' : Book.objects.filter(status = 'مستأجر').count(),
        'book_available' : Book.objects.filter(status = 'متاح').count(),
    
    }


    return render(request , 'Books/pages/index.html', Context )


###################################################################


def books(request):


    if request.method == 'POST':
        add_cat = CategoryForm(request.POST)
        if add_cat.is_valid():
            add_cat.save()
            return redirect ('index')
        
    else :
        add_cat = CategoryForm() 


    search = Book.objects.all()

    title = request.GET.get('search_name')

    if title:
        search = search.filter(title__icontains=title)

    Context = {
        'formcat' :  add_cat,
        'bookss': search,
        'Category': Category.objects.all(),
        'formcat': CategoryForm(),

    }
    return render(request, 'Books/pages/books.html', Context)

###################################################################


def update(request , id):

    book_id =  Book.objects.get(id=id)

    if request.method =='POST':
        book_save = BookForm(request.POST , request.FILES , instance=book_id) 

        if book_save.is_valid :
            book_save.save()
            return redirect ('index')
        
    else :
       book_save =  BookForm(instance = book_id)


    Context = { 
          
        'formcat' :  CategoryForm(),
        'update_book' : book_save,
    
    
    }
    return render(request , 'Books/pages/update.html' , Context)



###################################################################



def delete(request , id):

    book_delete = get_object_or_404(Book , id=id)

    if request.method == 'POST':
        book_delete.delete()
        return redirect('index')

    Context = { 
        
        
        'formcat' :  CategoryForm(),     
        'delete_book' : book_delete
    
    }
    return render(request , 'Books/pages/delete.html' , Context )
