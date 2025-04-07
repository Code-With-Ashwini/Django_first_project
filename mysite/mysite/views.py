from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm

def aboutUs(request):
   output = 0
   if request.method == 'GET':
       output = request.GET.get('output')
   return render(request, "about.html", {'output':output})

def course(request):
    return HttpResponse("Welcome to Ducat Ghaziabad")

def CourseById(request, courseId):
    return HttpResponse(courseId)

def homePage(request):
    data = {
        'title':'Home Page',
        'bdata':'Welcome to Django Template Creation',
        'clist':["PHP", "Python", "Java", "C#"],
        'student_details':[
            {'name':'Aman', 'phone':2873587435},
            {'name':'Shubham', 'phone':35385345646}
        ],
        'numbers':[10, 20, 30, 40, 50]

    }
    return render(request, "index.html", data)

def contact(request):
    return render(request, "contact.html")  

def submitform(request):

    finalans=0
    data={}
    try:
        if request.method == "POST":
            n1 = (int)(request.POST['num1'])
            n2 = (int)(request.POST['num2'])
            finalans = n1 + n2
            data={
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            url='/about-us/?output={}'.format(finalans)
            return redirect(url)
    except:
        pass
    return render(request, "error.html")
   
def userForm(request):
   
    finalans = 0
    fn = usersForm()
    
    data = {'form':fn}
    try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            data={
                'form':fn,
                'output':finalans
            }
            url="/about-us/?output={}".format(finalans)
        return redirect(url)
    except:
        pass
    return render(request, 'userform.html', data)