from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request , 'home.html')

def author(request):
	return render(request , 'author.html')

def book(request):
	return render(request , 'book.html')

def review(request):
	return render(request , 'review.html')

def what_next(request):
	return render(request, 'next.html')