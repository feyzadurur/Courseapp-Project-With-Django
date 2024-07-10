from django import forms

from courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model=Course 
        fields=('title','description','imageUrl','slug')
        #fields='__all__'
        labels={
            'title':"Kurs Başlığı",
            'description' : "Açıklama"
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl":forms.TextInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"})
        }
        error_messages={
            "title": {
                "required":"Kurs başlığı girmelisiniz.",
                "max_length" : "Maksimum 50 karakter girmelisiniz."
            },
            "description": {
                "required":"Kurs açıklaması girmelisiniz.",
            }
        
        }
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model=Course 
        fields=('title','description','imageUrl','slug')
        #fields='__all__'
        labels={
            'title':"Kurs Başlığı",
            'description' : "Açıklama"
        }
        widgets={
            "title":forms.TextInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),
            "imageUrl":forms.TextInput(attrs={"class":"form-control"}),
            "slug":forms.TextInput(attrs={"class":"form-control"})
        }
        error_messages={
            "title": {
                "required":"Kurs başlığı girmelisiniz.",
                "max_length" : "Maksimum 50 karakter girmelisiniz."
            },
            "description": {
                "required":"Kurs açıklaması girmelisiniz.",
            }
        
        }