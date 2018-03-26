from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import users
from .models import fileUploads
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

# Create your views here.
def index(request):
    return render(request,"index.html",{})

def register(request):
    try:
        if request.session.get('username',not None):
            if request.method == 'POST':
                username = request.POST.get('username','')
                email = request.POST.get('email','')
                password = request.POST.get('pwd','')
                obj = users()
                try:
                    chk_username = users.objects.get(username=username)
                    return render(request,'register.html',{'errMsg':'Username already exists: Try a diffrent one :)'})
                except:
                    obj.username = username
                    obj.email = email
                    obj.password = password
                    obj.save()
                    return render(request, 'register.html',{'errMsg': 'Registration successfull...'})
            else:
                return render(request, "register.html", {})
        else:
            return HttpResponseRedirect('/')
    except:
        return render(request, "register.html", {'errMsg':'Something went wrong !'})



def login(request):
    if request.method == 'POST':
        m = users.objects.get(username=request.POST['username'])
        if m.password == request.POST['pwd']:
            request.session['user_id'] = m.id
            request.session['username'] = m.username
            request.session['email'] = m.email
            return HttpResponseRedirect('/upload/')
        else:
            return render(request, "login.html", {'msg':'Username or Password Incorrect !'})
    else:
        return render(request, "login.html", {})



def upload(request):
    try:
        if request.session['username'] is not None:
            if request.method == 'POST' and request.FILES['file_name']:
                try:
                    myfile = request.FILES['file_name']
                    fs = FileSystemStorage()
                    filename = fs.save(myfile.name, myfile)
                    uname = request.POST.get('uname','')
                    obj = fileUploads()
                    obj.file_uploader = uname
                    obj.file_name = filename
                    obj.save()
                    

                    return render(request, "upload.html", {'msg': 'File uploaded successfully :)'})
                except:
                    return render(request, "upload.html", {'msg':'Something went wrong, retry !'})


            else:
                return render(request, "upload.html", {})
        else:
            return HttpResponseRedirect('/login/')
    except:
        return HttpResponseRedirect('/login/')


def log_out(request):
    try:
        del request.session['user_id']
        del request.session['username']
        del request.session['email']
        return HttpResponseRedirect('/')
    except:
        return HttpResponseRedirect('/')

def myUploads(request):
    if request.session['username'] is not None:
        username = request.session['username'];
        items = fileUploads.objects.filter(file_uploader=username)
        return render(request,"myUploads.html",{'items':items})
    else:
        return HttpResponseRedirect('/')
def aboutUs(request):
	return render(request,"about.html",{})
        
