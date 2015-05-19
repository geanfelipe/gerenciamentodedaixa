# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse,request, HttpResponseRedirect, HttpRequest


def hello(request):
	return render(request,'index.html',{})

def caixa(request):
	return render(request,'caixa.html',{})