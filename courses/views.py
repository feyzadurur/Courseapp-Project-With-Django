from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse
from datetime import date,datetime


data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web-gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

 
db= {
    "courses":[
        {
            "title": "Javascript kursu",
            "description": "Javascript kursu aciklamasi",
            "imageUrl":"1.jpg",
            "slug":"javascript-kursu",
            "date": datetime.now,
            "isActive":True,
            "isUpdated" : True
        },
        {
            "title": "Python kursu",
            "description": "Python kursu aciklamasi",
            "imageUrl":"2.jpg",
            "slug":"python-kursu",
             "date": datetime.now,
            "isActive":False,
            "isUpdated" : False
        },
        {
            "title": "Web geliştirme kursu",
            "description": "Web geliştirme  kursu aciklamasi",
            "imageUrl":"3.jpg",
            "slug":"web-gelistirme -kursu",
             "date": datetime.now,
            "isActive":True,
            "isUpdated" : True
        }
    ],
    "categories": [
        { "id":1 ,"name": "programlama" ,"slug":"programlama"},
        { "id":2 ,"name": "web geliştirme", "slug":"web-gelistirme" },
        { "id":3 ,"name": "mobil uygulamalar", "slug":"mobil-uygulamalar" }
        ]
}

def index(request):
    kurslar=[course for course in db["courses"] if course["isActive"]==True]
    kategoriler=db["categories"]
    
    
    return render(request,'courses/index.html',{
        'categories': kategoriler,
        'courses': kurslar
    })


def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfasi")


def getCoursesByCategory(request,category_name):
    #kurslar=Course.objects.filter(category__slug=slug,isActive=True)
    #kategoriler=Category.objects.all()
    
    try:
        category_text=data[category_name]
        return render(request,'courses/kurslar.html', {
            'category' :category_name,
            'category_text':category_text
        })
    except:
        return HttpResponseNotFound("<h1>yanliş kategori seçimi </h1>")



def getCoursesByCategoryID(request,category_id):

    #1-2-3->
    category_list=list(data.keys())
    if((category_id)> len(category_list)):
        return HttpResponseNotFound("yanliş kategori seçimi")
    category_name= category_list[category_id - 1]

    redirect_url=reverse('courses_by_category',args=[category_name])
    return redirect(redirect_url)
