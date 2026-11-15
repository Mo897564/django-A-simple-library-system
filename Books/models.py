from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50 , verbose_name='الفئة')

    def __str__(self):
        return self.name


class Book(models.Model):

    status_book = [
        ('متاح','متاح') ,
        ('مستأجر','مستأجر'),
        ('تم بيعة','تم بيعة')
    ]


    title = models.CharField(max_length=250 , verbose_name='عنوان الكتاب')
    author = models.CharField(max_length=50 , null=True , blank=True , verbose_name='المؤلف')
    photo_book = models.ImageField(upload_to='photos/%y/%m/%d' , default='photos/default/phtoodefaultk.png' , verbose_name = 'صورة الكتاب')
    photo_author = models.ImageField(upload_to='photos/%y/%m/%d' , default='photos/default/phtoodefaultk.png', verbose_name = 'صورة المؤلف')
    pages = models.IntegerField(null=True , blank=True , verbose_name= 'عدد الصفحات')
    price = models.DecimalField(max_digits= 5 , decimal_places= 2 , null=True , blank=True , verbose_name= 'السعر')
    rental_price_day = models.DecimalField(max_digits= 5 , decimal_places= 2 , null=True , blank=True , verbose_name= 'سعر الايجار في اليوم')
    rental_period = models.IntegerField(null=True , blank=True, verbose_name= 'فترة الايجار')
    rental_total = models.IntegerField(null=True , blank=True, verbose_name= 'اجمالي الايجار')
    active = models.BooleanField(default=True , verbose_name= 'النشاط')
    status = models.CharField(max_length=50 , choices=status_book , null=True , blank=True , verbose_name= 'الحالة')
    categoer = models.ForeignKey(Category , on_delete= models.PROTECT , null=True , blank=True , verbose_name= 'الفئة')

    def __str__(self):
            return self.title
    