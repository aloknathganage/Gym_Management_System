from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .models import *
# Create your views here.
@csrf_protect
def home(request):
    return render(request,'login.html')
    
@csrf_protect
def Index(request):
    return render(request,'index.html')

@csrf_protect
def Login(request):
    error=''
    print('before if')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        print('in if')
        if user.is_staff:
            login(request,user)
            print('after  auth')
            return render(request,'index')
        else:
            
            error='yes'
    return render(request, 'login.html')

def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def Add_member(request):
    if request.method == 'POST':
        n = request.POST['name']
        c = request.POST['contact']
        e = request.POST['emailid']
        a = request.POST['age']
        g = request.POST['gender']
        p = request.POST['plan']
        joindate = request.POST['joindate']
        expiredate = request.POST['expdate']
        initialamount = request.POST['initialamount']
        # plan = Plan.objects.filter(name=p).first()
        member= Member.objects.create( name=n, contact=c,emailid=e, age=a,gender=g,plan=p, joindate=joindate, expiredate = expiredate, initialamount = initialamount)
        member.save()
        # return redirect(request,'view_member.html')
    return render(request,'add_member.html')

def View_member(request):
    mem = Member.objects.all()
    return render(request, 'view_member.html',{'mem': mem})
def Delete_Member(request,pid):
    member = Member.objects.get(id=pid)
    member.delete()
    return redirect('view_member')

def Add_plan(request):
    if request.method == 'POST':
        n = request.POST['name']
        a = request.POST['amount']
        d = request.POST['duration']
        p=Plan.objects.create( name=n, amount=a, duration=d)
        p.save()
        # return redirect(request,'view_plan.html')
    return render(request, 'add_plan.html')

def View_plan(request):
    plan=Plan.objects.all()
    return render(request,'view_plan.html',{'plan':plan})

def Delete_plan(request,pid):
    plan = Plan.objects.get(id=pid)
    plan.delete()
    return redirect('view_plan')

def Add_equipment(request):
    if not request.user.is_staff:
        return redirect('login')
    if request.method == 'POST':
        n = request.POST['name']
        p = request.POST['price']
        u = request.POST['unit']
        d = request.POST['date']
        desc = request.POST['desc']
        e=Equipment.objects.create( name=n, price=p, unit=u, date=d, description=desc)
        e.save()
    return render(request,'add_equipment.html')







































