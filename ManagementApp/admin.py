from django.contrib import admin
from .models import UserProfile , Room , RoomBooking , RoomType , ContactData , Suscribe , BuyFitnessPack , FitnessPack , Drink , OrderDrink , Food , OrderFood
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(RoomBooking)
admin.site.register(RoomType)
admin.site.register(Room)
admin.site.register(ContactData)
admin.site.register(Suscribe)
admin.site.register(BuyFitnessPack)
admin.site.register(FitnessPack)
admin.site.register(Drink)
admin.site.register(OrderDrink)
admin.site.register(Food)
admin.site.register(OrderFood)
