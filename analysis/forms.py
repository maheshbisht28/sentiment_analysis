from django import forms

class MyForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    a = forms.CharField(max_length=1000)

class MyForms(forms.Form): #Note that it is not inheriting from forms.ModelForm
    a = forms.CharField(max_length=1000)
    b = forms.CharField(max_length=1000)
    c = forms.CharField(max_length=1000)
    d = forms.CharField(max_length=1000)
    e = forms.CharField(max_length=1000)
    f = forms.CharField(max_length=1000)
    g = forms.CharField(max_length=1000)
    h = forms.CharField(max_length=1000)
    i = forms.CharField(max_length=1000)
    j = forms.CharField(max_length=1000)



class Myhash(forms.Form): #Note that it is not inheriting from forms.ModelForm
    h = forms.CharField(max_length=100)

