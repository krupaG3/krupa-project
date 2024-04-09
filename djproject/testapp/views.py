from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def hydjobs(request):
    jobs_list=hydjobs.objects.order_by('date')
    my_dict={'jobs_list':jobs_list}
    return render(request,'hydjobs.html',context=my_dict)

def punejobs(request):
    return render(request,'punejobs.html')

def bnglrjobs(request):
    return render('request','bnglrjobs.html')

def chennaijobs(request):
    return render('request','chennaijobs.html')

