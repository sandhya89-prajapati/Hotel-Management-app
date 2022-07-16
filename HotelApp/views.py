from django.shortcuts import  render , redirect
from django.http import HttpResponse
from datetime import datetime , timedelta
from django.core.mail import send_mail
from ManagementApp.models import RoomType , Room ,RoomBooking , ContactData , Suscribe ,OrderFood ,OrderDrink ,BuyFitnessPack , Drink , Food ,FitnessPack



def homepage(request):
    return render(request,'website/homepage.html')

def services(request):
    return render(request,'website/services.html')

def aboutus(request):
    if request.method == 'POST':
        email = request.POST['email']
        eobj = Suscribe(email=email)
        eobj.save()
    return render(request,'website/aboutus.html')

def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        cobj = ContactData(name=name,email=email,subject=subject,message=message)
        cobj.save()
    return render(request,'website/contactus.html')

def restroBar(request):
    fobj = Food.objects.all()
    dobj = Drink.objects.all()
    return render(request,'website/restroBar.html',{'fobj':fobj,'dobj':dobj})

def fitness(request):
    obj = FitnessPack.objects.all()
    curren = datetime.today().strftime('%Y-%m-%d')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        cdate = request.POST['cdate']
        fitobj = FitnessPack.objects.get(name = request.POST['pack'])
        dateobj = datetime.strptime(cdate, "%Y-%m-%d")
        newdate = dateobj + timedelta(fitobj.duration)
        fobj = BuyFitnessPack(email=email,name=name,packtype=fitobj,expdate=newdate.strftime('%Y-%m-%d'),status='Paid')
        fobj.save()
        mailMessage = ' Name :'+str(name)+', Email :'+str(email)+', Pack :'+str(fitobj)+', Buy Date :'+str(cdate)+', Pack Expiry Date :'+str(newdate.strftime('%Y-%m-%d'))+', Pack Price :'+str(fitobj.price)+', Status : Paid'
        send_mail('Royal Hotel Fitness Pack :','Pack Deatils :- {}'.format(mailMessage),'Userid',[email])
        return redirect('/fitness/')
    return render(request,'website/fitness.html',{'obj':obj,'date':curren})

def hotelrooms(request):
    robj = RoomType.objects.all()
    return render(request,'website/hotelrooms.html',{'robj':robj})


date = ''
datein = ''
dateout = ''
adu = ''
chil = ''
roomobj = ''
def checkavail(request):
    robj = RoomType.objects.all()
    if request.method == 'POST':
        checkin = request.POST['checkin']
        checkout = request.POST['checkout']
        adult = request.POST['adult']
        children = request.POST['children']
        room = request.POST['rtype']
        currentdate = datetime.today().strftime('%Y-%m-%d')

        global date , datein , dateout , adu , chil
        date = currentdate
        datein = checkin
        dateout = checkout
        adu = adult
        chil = children

        chin = datetime.strptime(checkin, "%Y-%m-%d")
        chout = datetime.strptime(checkout, "%Y-%m-%d")
        cur = datetime.strptime(currentdate, "%Y-%m-%d")
        rtobj = RoomType.objects.get(roomName = room)
        if chin >= cur and chout >= chin:
            print('valid')
            for i in Room.objects.filter(roomtype = rtobj.id):
                if checkin in i.bookings and checkout in i.bookings:
                    continue
                else:
                    global roomobj
                    roomobj = i
                    return render(request,'website/hotelrooms.html',{'obj':i,'robj':robj,'checkin':checkin,'checkout':checkout})
            return render(request,'website/hotelrooms.html',{'ack':'No bookings Available','robj':robj})
        else :
            print('invalid')
    return render(request,'website/hotelrooms.html',{'robj':robj,'ack':''})


def HRpayment(request):
    return render(request,'website/HRpayment.html')

def roombooking(request,id):
    global date , datein , dateout , adu , chil ,roomobj
    current = date
    din = datein
    dout = dateout
    adult = adu
    children = chil
    roomob = roomobj
    if request.method == 'POST':
        bookie = request.POST['bookie']
        aadhar = request.POST['aadhar']
        email = request.POST['email']
        mob = request.POST['mob']
        bookingdate = request.POST['date']
        roomid = Room.objects.get(hotelRoomid = id)
        checkin = request.POST['cindate']
        checkout = request.POST['coutdate']
        adults = request.POST['adult']
        children = request.POST['children']
        roomtype = RoomType.objects.get(roomName = roomid.roomtype.roomName)
        bookingmode = request.POST['pay']
        bookingamount = request.POST['bookamt']
        remainigamount=0
        status = ''

        datecount = 0
        import datetime
        qobj = Room.objects.filter(hotelRoomid = id)
        nvar = roomid.bookings
        start = datetime.datetime.strptime(checkin, "%Y-%m-%d")
        end = datetime.datetime.strptime(checkout, "%Y-%m-%d")
        date_array = (start + datetime.timedelta(days=x) for x in range(0, (end-start).days+1))
        for date_object in date_array:
            nvar = nvar + str(date_object.strftime("%Y-%m-%d"))+','
            datecount = datecount + 1
        #print(nvar)
        qobj.update(bookings = nvar)

        if not(int(bookingamount)<0) and roomtype.roomprice * datecount > int(bookingamount):
            remainigamount = roomtype.roomprice * datecount - int(bookingamount)
            status = 'Booked'
        elif roomtype.roomprice * datecount == int(bookingamount):
            remainigamount = 0
            status = 'Paid'

        #print(bookie,aadhar,bookingdate,checkin,checkout,adults,children,bookingmode,bookingamount,remainigamount,status)

        obj=RoomBooking(bookie=bookie,aadhar=aadhar,email=email,mob=mob,bookingdate=bookingdate,roomid=roomid,checkin=checkin,checkout=checkout,adults=adults,children=children,roomtype=roomtype,bookingmode=bookingmode,bookingamount=bookingamount,remainigamount=remainigamount,status=status)
        obj.save()
        mailMessage = 'Bookie :'+str(bookie)+', Aadhar :'+str(aadhar)+', Email :'+str(email)+', Mobile :'+str(mob)+', Room id :'+str(roomid)+', Booking Date :'+str(bookingdate)+', Check In :'+str(checkin)+', Check Out :'+str(checkout)+', Adults :'+str(adults)+', Children :'+str(children)+', Room Type :'+str(roomtype)+', Booking Mode :'+str(bookingmode)+', Booking Amount :'+str(bookingamount)+', Balance :'+str(remainigamount)+', Status :'+str(status)
        send_mail('Royal Hotel - Room Booking Service :-',' Booking :- {}'.format(mailMessage),'Userid',[email])
        return redirect('/checkavail/')
    return render(request,'website/roombooking.html',{'adu':adult,'chil':children,'date':current,'datein':din,'dateout':dout,'roomobj':roomob,'id':id})


def orderfood(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        qty = request.POST['qty']
        email = request.POST['email']
        foodtype = Food.objects.get(name = request.POST['fid'])
        desc = 'no description'
        status = 'Ordered'

        obj = OrderFood(name=name,mob=mob,email=email,foodtype=foodtype,qty=qty,desc=desc,status=status)
        obj.save()
        mailMessage = "Name :{} , Mobile :{} , Email :{} ,Food :{} , Quantity :{} , Status :{} , Price :{} ".format(name,mob,email,foodtype,qty,'Paid',int(foodtype.price)*int(qty))
        send_mail('Royal Hotel - Food Service','Invoice :- {}'.format(mailMessage),'Userid',[email])
        return redirect('/restroBar/')
    return render(request,'website/restroBar.html')

def orderdrink(request):
    if request.method == 'POST':
        name = request.POST['name']
        mob = request.POST['mob']
        qty = request.POST['qty']
        email = request.POST['email']
        drinktype = Drink.objects.get(name = request.POST['did'])
        desc = 'no description'
        status = 'Ordered'

        obj = OrderDrink(name=name,mob=mob,email=email,drinktype=drinktype,qty=qty,desc=desc,status=status)
        obj.save()
        mailMessage = "Name :{} , Mobile :{} , Email :{} ,Drink :{} , Quantity :{} , Status :{} , Price :{} ".format(name,mob,email,drinktype,qty,'Paid',int(drinktype.price)*int(qty))
        send_mail('Royal Hotel - Food Service','Invoice :- {}'.format(mailMessage),'Userid',[email])
        return redirect('/restroBar/')
    return render(request,'website/restroBar.html')

