from django.shortcuts import render, redirect
from MyApp.models import Users, Member, Contact


# Create your views here.
def index(request):
    if request.method == 'POST':
        message = Contact(name=request.POST['name'], email=request.POST['email'], subject=request.POST['subject'],
                          message=request.POST['message'])

        message.save()
        return redirect('/')

    else:
        return render(request, 'index.html')


def blog(request):
    return render(request, 'blog.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def portfolio(request):
    return render(request, 'portfolio-details.html')


def sampleinner(request):
    return render(request, 'sample-inner-page.html')


def login(request):
    return render(request, 'login.html')


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Member.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'adminhome.html', {'member': member})
        else:
            return render(request, "login.html")
    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        members = Member(Username=request.POST['username'], Email=request.POST['email'],
                         Password=request.POST['password'])
        members.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')
