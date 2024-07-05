from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,HttpResponseNotFound
from django.urls import reverse

data = {
    "programlama" : "programlama kategorisine ait kurslar",
    "web-gelistirme" : "web-gelistirme kategorisine ait kurslar",
    "mobil" : "mobil kategorisine ait kurslar",
}

def kurslar(request):
    return HttpResponse('kurs listesi')

def details(request,slug):
    return HttpResponse(f"{slug} detay sayfasi")


def getCoursesByCategory(request, category_name):

    try:
        category_text=data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanliş kategori seçimi")


def getCoursesByCategoryID(request,category_id):

    #1-2-3->
    category_list=list(data.keys())
    if((category_id)> len(category_list)):
        return HttpResponseNotFound("yanliş kategori seçimi")
    category_name= category_list[category_id - 1]

    redirect_url=reverse('courses_by_category',args=[category_name])

    #return HttpResponseRedirect('/kurs/kategori/programlama')
    return redirect(redirect_url)
