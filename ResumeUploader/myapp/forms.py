from django import forms
from .models import Resume

GENDER_CHOICES=[
    ('Male','Male'),
    ('Female','Female')
]

JOB_CITY_CHOICE = [
    ('Aurangabad','Aurangabad'),
    ('Banglore','Banglore'),
    ('Chennai','Chennai'),
    ('Delhi','Delhi'),
    ('Hydrabad','Hydrabad'),
    ('Mumbai','Mumbai'),
    ('Nashik','Nashik'),
    ('Pune','Pune'),
    ('Noida','Noida'),
    ('US','US')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='Prefered Job Location',choices=JOB_CITY_CHOICE,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resume
        fields = ['name', 'dob', 'gender', 'locality', 'city', 'pin', 'state', 'mobile', 'email', 'job_city',
                  'profile_image', 'my_file']
        labels = {'name':'Full Name :' , 'dob':'Date of Birth :' , 'gender':'Gender :','locality':'Locality :',
                  'city':'City :','pin':'Pin Code :','state':'State :','mobile':'Mobile No. :', 'email':'Email ID :',
                  'job_city':'Job City :', 'profile_image':'Profile Image :','my_file':'Document / CV :'
                  }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control','id':'datepicker'}),
            'locality':forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }