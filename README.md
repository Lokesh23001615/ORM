# Ex02 Django ORM Web Application
## Date: 29.02.2024

## AIM
To develop a Django application to store and retrieve data from a Book database using Object Relational Mapping(ORM).

## Entity Relationship Diagram

![alt text](<Screenshot 2024-02-29 135332.png>)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

from django.db import models
from django.contrib import admin
class Book(models.Model):
   bookid=models.IntegerField(primary_key=True);
   bookname=models.CharField(max_length=30);
   bookprice=models.IntegerField();
   author=models.CharField(max_length=30);
   qty=models.IntegerField();
class BookAdmin(admin.ModelAdmin):
   list_display=("bookid","bookname","bookprice","author","qty");

admin.py

from django.contrib import admin
from .models import Book,BookAdmin
admin.site.register(Book,BookAdmin)
```

## OUTPUT

![alt text](<Screenshot 2024-02-27 144927.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
