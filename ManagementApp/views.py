from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
from ManagementApp.models import UserProfile , Room , RoomBooking , RoomType , Food , FitnessPack , Drink , ContactData ,Suscribe ,OrderFood ,OrderDrink ,BuyFitnessPack
from .forms import UserProfileForm , UserForm
from datetime import datetime
import calendar


# Create your views here.

@login_required
def managementPage(request):
    obj = Room.objects.all()
    return render(request,'managementApp/managementPage.html',{'obj':obj})

@login_required
def managementPagetwo(request,id):
    obj = Room.objects.all()
    nobj = Room.objects.get(hotelRoomid=id)
    lis = nobj.bookings.split(',')
    print(lis)
    nlis = ''
    for i in lis:
        if i[5:7] == datetime.now().strftime("%m") and i[0:4] == datetime.now().strftime("%Y"):
            nlis = nlis + str(i[8:])+','
    return render(request,'managementApp/managementPagetwo.html',{'obj':obj,'nobj':nobj,'nlis':nlis})

def signin(request):
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        selecteduser = authenticate(username = username,password = password)
        if selecteduser:
            if selecteduser.is_active:
                login(request,selecteduser)
                udata = UserProfile.objects.get(user__username=request.user)
                return redirect('/managementApp/managementPage/')
            else:
                return HttpResponse("<h1>User deactivated</h1>")
        else:
            return redirect('/managementApp/signup/')
    else:
        return render(request,'managementApp/signin.html')

def signup(request):
    uform = UserForm()
    upform = UserProfileForm()
    if request.method == 'POST':
        user=UserForm(request.POST)
        pro=UserProfileForm(request.POST)
        if user.is_valid() and pro.is_valid():
            usersaved=user.save()
            usersaved.set_password(usersaved.password)
            usersaved.save()
            prosaved=pro.save(commit=False)
            prosaved.user=usersaved
            prosaved.save()
            return redirect('/managementApp/signin/')
    return render(request,'managementApp/signup.html',{'uform':uform,'upform':upform})

@login_required
def signout(request):
    logout(request)
    return redirect('/managementApp/signup/')

@login_required
def viewfood(request):
    obj = Food.objects.all()
    print(obj)
    return render(request,'managementApp/viewfood.html',{'obj':obj})

@login_required
def deletefood(request,id):
    obj = Food.objects.get(id = id)
    obj.delete()
    return redirect('/managementApp/restro/')

@login_required
def viewdrink(request):
    obj = Drink.objects.all()
    print(obj)
    return render(request,'managementApp/viewdrink.html',{'obj':obj})

@login_required
def deletedrink(request,id):
    obj = Drink.objects.get(id = id)
    obj.delete()
    return redirect('/managementApp/viewbar/')


@login_required
def viewfitnessplan(request):
    obj = FitnessPack.objects.all()
    print(obj)
    return render(request,'managementApp/viewfitness.html',{'obj':obj})

@login_required
def deletefitnessplan(request,id):
    obj = FitnessPack.objects.get(id = id)
    obj.delete()
    return redirect('/managementApp/viewfitness/')


@login_required
def viewroom(request):
    obj = RoomType.objects.all()
    print(obj)
    return render(request,'managementApp/viewroom.html',{'obj':obj})

@login_required
def deleteroom(request,id):
    obj = RoomType.objects.get(id = id)
    obj.delete()
    return redirect('/managementApp/viewroom/')

@login_required
def order(request):
    rb = RoomBooking.objects.all()
    food = OrderFood.objects.all()
    drink = OrderDrink.objects.all()
    pack = BuyFitnessPack.objects.all()
    return render(request,'managementApp/records.html',{'rb':rb,'food':food,'drink':drink,'pack':pack})

@login_required
def addnew(request):
    rtobj =  RoomType.objects.all()
    return render(request,'managementApp/addnew.html',{'obj':rtobj})

@login_required
def addroomtype(request):
    if request.method =='POST':
        roomName = request.POST['roomName']
        roomimg = request.FILES['roomimg']
        totalrooms = request.POST['totalrooms']
        roomsize = request.POST['roomsize']
        roomview = request.POST['roomview']
        roomoccupancy = request.POST['roomoccupancy']
        roomprice = request.POST['roomprice']
        roomdesc = request.POST['roomdesc']
        obj = RoomType(roomName=roomName,roomimg=roomimg,totalrooms=totalrooms,roomsize=roomsize,roomview=roomview,roomoccupancy=roomoccupancy,roomprice=roomprice,roomdesc=roomdesc)
        obj.save()
        return redirect('/managementApp/viewRooms/')

@login_required
def addroom(request):
    if request.method =='POST':
        hotelRoomid = request.POST['hotelRoomid']
        roomtype = RoomType.objects.get(roomName=request.POST['roomtype'])
        bookings = request.POST['bookings']
        obj = Room(hotelRoomid=hotelRoomid,roomtype=roomtype,bookings=bookings)
        obj.save()
        return redirect('/managementApp/managementPage/')

@login_required
def addfood(request):
    if request.method =='POST':
        name = request.POST['name']
        img =request.FILES['img']
        price = request.POST['price']
        cat = request.POST['cat']
        desc= request.POST['desc']
        obj = Food(name=name,img=img,price=price,cat=cat,desc=desc)
        obj.save()
        return redirect('/managementApp/restro/')

@login_required
def adddrink(request):
    if request.method =='POST':
        name = request.POST['name']
        img =request.FILES['img']
        price = request.POST['price']
        cat = request.POST['cat']
        desc= request.POST['desc']
        obj = Drink(name=name,img=img,price=price,cat=cat,desc=desc)
        obj.save()
        return redirect('/managementApp/viewbar/')

@login_required
def addfitness(request):
    if request.method =='POST':
        name = request.POST['name']
        img =request.FILES['img']
        price = request.POST['price']
        duration = request.POST['duration']
        desc= request.POST['desc']
        obj = FitnessPack(name=name,img=img,price=price,duration=duration,desc=desc)
        obj.save()
        return redirect('/managementApp/viewfitness/')

@login_required
def updateRoomStatus(request,id):
    obj = RoomBooking.objects.filter(id = id)
    obj.update(status = 'Checked Out')
    return redirect('/managementApp/order/')
