from .models.notice import Notice
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def important(request):
    notice1 = Notice.getNotice()
    return render(request,'important.html', {'notice_key': notice1})


def contact(request):
    return render(request,'contact.html')

'''def branch(request):
    return render(request,'branch.html')         

def fiter(request):
    return render(request,'fiter.html')

def computer(request):
    return render(request,'computer.html')

def eletrical(request):
    return render(request,'eletrical.html')    '''
