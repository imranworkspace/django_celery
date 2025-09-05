from django.shortcuts import render
#use celery 
from myapp.tasks import add,sub
from celery.result import AsyncResult

# Addition value of task exection
def index(request): 
    # use of async task 
    result = add.delay(10,200) # run in backgroud, u can chk in CELERY bash prompt 1+2=3 ,3 will show on bash after 20 seconds
    return render(request,'home.html',{'result':result})

def check_result(request,task_id):
    # retrive task id 
    result = AsyncResult(task_id)
    
    # celery methods
    print('Ready: ',result.ready())
    print('Successful: ',result.successful())
    print('Failed: ',result.failed())    
    return render(request,'result.html',{'result':result})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')