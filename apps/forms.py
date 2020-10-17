from django import forms
from apps.models import Book

# class BookForm(forms.Form):
# 	name=forms.CharField()
# 	isbn=forms.CharField()
# 	price=forms.CharField()

#easiest way than above method
class BookForm(forms.ModelForm):
	class Meta:
		model=Book
		fields=("name","isbn","price","author","cover",)
