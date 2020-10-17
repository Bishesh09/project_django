from django.shortcuts import render,reverse,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from apps.models import Book
from apps.forms import BookForm


def home_view(request):
	context={"message":"this is dynamically created","message_list":["hello","welcome","greetings","bye bye"]}
	return render(request,'index.html',context)

def about_view(request):
	return HttpResponse("welcome to about")


def book_list_view(request):
	books=Book.objects.all()
	context={"books":books}
	return render(request,"apps/book_list.html",context)
	

def add_new_book(request):
	print(request.POST)
	form=BookForm(request.POST or None,request.FILES or None )
	if form.is_valid():
		# Book.objects.create(**form.cleaned_data)
		#use above code if no model is used in forms.py.if its used than we can use below method.
		form.save()
		return HttpResponseRedirect(reverse("apps:book_list"))


	return render(request,"apps/form.html",{"form":form})


def edit_book(request,book_id):
	book=get_object_or_404(Book,id=book_id)
	form=BookForm(request.POST or None, request.FILES or None,instance=book )
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse("apps:book_list"))
	
	return render(request,"apps/form.html",{"form":form})