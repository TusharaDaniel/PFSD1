from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def viewposts(request):
    return render(request, 'usermodule/viewposts.html')
def languages(request):
    return render(request,'languages/telugu.html')

def bollywood(request):
    return render(request,'languages/hindi.html')

def hollywood(request):
    return render(request,'languages/english.html')

def tamilhits(request):
    return render(request,'languages/tamil.html')

def hiphop(request):
    return render(request,'languages/hiphop.html')