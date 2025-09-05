from django.shortcuts import render

#use celery 
from myapp.tasks import add,sub
'''
# Enqueue task using delay()
def index(request): 
    # use of delay function
    result1 = add.delay(10,200) # run in backgroud, u can chk in CELERY bash prompt 1+2=3 ,3 will show on bash after 20 seconds
    result2 = sub.delay(20,80) # run in backgroud, u can chk in CELERY bash prompt 1+2=3 ,3 will show on bash after 20 seconds
    
    #result1 = add(1,2) # run in frontent wait for 20 seconds
    
    
    print('Task Result 1==',result1)
    print('Task Result 2==',result2)
    
    return render(request,'home.html',{'result1':result1,'result2':result2})
'''

def index(request): 
    # use of async task 
    result1 = add.apply_async(args=[10,200]) # run in backgroud, u can chk in CELERY bash prompt 1+2=3 ,3 will show on bash after 20 seconds
    result2 = sub.apply_async(args=[40,500])
    print('Task Result 1==',result1)
    print('Task Result 2==',result2)
    
    return render(request,'home.html',{'result1':result1,'result2':result2})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')