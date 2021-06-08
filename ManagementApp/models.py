from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=12)
    usertype = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class RoomType(models.Model):
    roomName = models.CharField(max_length=30)
    roomimg = models.ImageField(upload_to='productImg',blank='True')
    totalrooms = models.IntegerField()
    roomsize = models.IntegerField()
    roomview = models.CharField(max_length=30)
    roomoccupancy = models.IntegerField()
    roomprice = models.DecimalField(max_digits=6,decimal_places=2)
    roomdesc = models.CharField(max_length=200)

    def __str__(self):
        return self.roomName

class Room(models.Model):
    hotelRoomid = models.IntegerField()
    roomtype = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    bookings = models.CharField(max_length=4000)
    def __str__(self):
        return str(self.hotelRoomid)

class RoomBooking(models.Model):
    bookie = models.CharField(max_length=50)
    aadhar = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    bookingdate = models.DateField()
    roomid = models.ForeignKey(Room,on_delete=models.CASCADE)
    checkin = models.DateField()
    checkout = models.DateField()
    adults = models.IntegerField()
    children = models.IntegerField()
    roomtype = models.ForeignKey(RoomType,on_delete=models.CASCADE)
    bookingmode = models.CharField(max_length=20)
    bookingamount = models.DecimalField(max_digits=6,decimal_places=2)
    remainigamount = models.DecimalField(max_digits=6,decimal_places=2)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.aadhar

class Food(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImg',blank='True')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    cat = models.CharField(max_length=30)
    desc= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderFood(models.Model):
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    foodtype = models.ForeignKey(Food,on_delete=models.CASCADE)
    qty = models.IntegerField()
    desc = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImg',blank='True')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    cat = models.CharField(max_length=30)
    desc= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OrderDrink(models.Model):
    name = models.CharField(max_length=50)
    mob = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    drinktype = models.ForeignKey(Drink,on_delete=models.CASCADE)
    qty = models.IntegerField()
    desc = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class FitnessPack(models.Model):
    name = models.CharField(max_length=30)
    img = models.ImageField(upload_to='productImg',blank='True')
    price = models.DecimalField(max_digits=6,decimal_places=2)
    duration = models.IntegerField()
    desc = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class BuyFitnessPack(models.Model):
    email= models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    packtype = models.ForeignKey(FitnessPack,on_delete=models.CASCADE)
    expdate = models.DateField()
    status = models.CharField(max_length=50)
    def __str__(self):
        return self.email

class ContactData(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=80)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.email

class Suscribe(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.email
