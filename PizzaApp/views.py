from django.shortcuts import render

#Code From here

def index_page(request):
    return render(request,'pizza/index.html',{})