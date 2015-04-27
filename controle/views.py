from django.shortcuts import render
#from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest


# Create your views here.
def hello(request):
	return render(request,'index.html',{})