
import pickle
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
import json
import os

def home(request):
    return render(request,'home.html') 

def index(request):
    bill = 0
    message ="Welcome to RollerCoaster Rides!!!"
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")

    if request.method == "POST":
        name = request.POST.get("name","").upper()
        age = int(request.POST.get("age") or 0)
        height = int(request.POST.get("height") or 0)
        seat = request.POST.get("seat","").upper()
    
        form_data = {
            "name": name, "age": age, "height": height, "seat": seat,
    "ride_id": request.POST.get("ride_id", "1"),
    "booking_date": request.POST.get("booking_date", ""),
    "time_slot": request.POST.get("time_slot", ""),
        }
        
        if age >18 and age < 70:
            bill = 300
            message += "You are an Adult ! "
        elif age >= 10 and age < 18:
            bill = 200
            message += "You are a child ! "
        else:
            bill = 0 
            
        if bill > 0:
            if height >= 120 :
                message += "Your height is as per the  eligibility"
                if seat == "S":
                    bill += 100
                elif seat == "L" : 
                    bill += 50
                else:
                    bill = bill
            else :
                message += "Height isn't as per the criteria "
        else :
            message += "Sorry , You are not eligible !" 
            
        
        # Stage 2: calculate final bill
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        # Stage 3: confirm (DB save in Phase 6)
        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True    

    return render(request, "designnn.html", {
        "bill": bill if stage in ("", "1") else None,
        "final_bill": final_bill,
        "message": message,
        "form_data": form_data,
        "booking_confirmed": booking_confirmed,
    })    

@login_required(login_url='register_login')
def drop_tower(request):
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")
    message = ""
    bill = None
    if request.method == "POST":
        age = int(request.POST.get("age"))
        weight = int(request.POST.get("weight"))
        harness_type = (request.POST.get("harness_type") or "").upper()  # example attribute for drop tower
        
        form_data = {"age": age, "weight": weight, "harness_type": harness_type}
        
        bill = 0
        if age < 15 and age > 9:
            bill = 75
            message = "Child discount applied!"
        elif age> 15 and age<65:
            bill = 150
        else:
            bill =0

        if bill>0:
            if weight > 90:
                bill += 50
                message = "Extra charges for over weight \n"

            if harness_type == "PREMIUM":
                bill += 50
                
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True        
            

    # return render(request, "drop_tower.html", {"message": message, "bill": bill})
    return render(request, "drop_tower.html", {
    "bill": bill,
    "final_bill": final_bill,
    "message": message,
    "form_data": form_data,
    "booking_confirmed": booking_confirmed,
    })

@login_required(login_url='register_login')
def bumper_cars(request):
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")
    message = ""
    bill = None
    if request.method == "POST":
        name = request.POST.get("name","").upper()
        age = int(request.POST.get("age") or 0)
        num_laps = int(request.POST.get("laps")or 0)
        car_type = (request.POST.get("car_type") or "").upper()
        
        form_data = {"name": name, "age": age, "num_laps": num_laps, "car_type": car_type}

        if age>7 and age <14:
            bill = 100

        else:
            bill = 150

        if bill>0:
            if car_type == "ELECTRIC" :
                bill +=50
            elif car_type == "GAS"  : 
                bill = bill

        if bill  >0:
            if num_laps > 10 and num_laps<21:
                bill += 100
                
                
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True       
    # return render(request, "bumper_cars.html", {"message": message, "bill": bill})
    return render(request, "bumper_cars.html", {
    "bill": bill,
    "final_bill": final_bill,
    "message": message,
    "form_data": form_data,
    "booking_confirmed": booking_confirmed,
    })

@login_required(login_url='register_login')
def ferris_wheel(request):
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")
    message = ""
    bill = None
    if request.method == "POST":
        age = int(request.POST.get("age") or 0)
        cabin_type = (request.POST.get("seat") or "").upper()
        num_rounds = int(request.POST.get("rounds") or 0)
        
        form_data = {"age": age, "cabin_type": cabin_type, "num_rounds": num_rounds}

        bill = 100
        if age < 12 and age >7:
            bill *= 0.5
            message = "Child discount applied!"
        if cabin_type == "VIP":
            bill += 50
        if num_rounds >11 and num_rounds<21:
            bill += 100
            
            
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True   

    # return render(request, "ferris_wheel.html", {"message": message, "bill": bill})
    return render(request, "ferris_wheel.html", {
    "bill": bill,
    "final_bill": final_bill,
    "message": message,
    "form_data": form_data,
    "booking_confirmed": booking_confirmed,
    })

@login_required(login_url='register_login')
def water_slides(request):
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")
    message = ""
    bill = None
    if request.method == "POST":
        # num_slides = int(request.POST.get("slides"))
        age = int(request.POST.get("age") or 0)
        height = int(request.POST.get("height") or 0)
        slide_type = (request.POST.get("slide") or "").upper()
        
        form_data = {"age": age, "height": height, "slide_type": slide_type}

        bill = 120
        if age < 12:
            bill *= 0.5
            message = "Child discount applied!"

        if slide_type == "EXTREME":
            bill += 150     
            
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True    
    # return render(request, "water_slides.html", {"message": message, "bill": bill})
    return render(request, "water_slides.html", {
    "bill": bill,
    "final_bill": final_bill,
    "message": message,
    "form_data": form_data,
    "booking_confirmed": booking_confirmed,
    })

@login_required(login_url='register_login')
def rain_dance(request):
    final_bill = None
    booking_confirmed = False
    form_data = {}
    stage = request.POST.get("stage", "")
    message = ""
    bill = None
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        ticket_type = (request.POST.get("ticket") or "").upper()
        dance_gear = (request.POST.get("gear") or "").upper()
        
        form_data = {"age": age, "ticket_type": ticket_type, "dance_gear": dance_gear}

        bill = 70
        if age < 14 :
            bill = 40
            message = "Child discount applied!"

            if dance_gear == "YES":
                bill += 30
        if dance_gear == "YES":
            bill += 50        

        if bill > 0:
            if ticket_type == "EVENING":
                bill += 20
            if ticket_type == "VIP":
                bill += 50    
        if stage == "2" and bill > 0:
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None

        if stage == "3":
            num_seats = int(request.POST.get("num_seats") or 1)
            final_bill = bill * num_seats
            form_data["num_seats"] = num_seats
            bill = None
            booking_confirmed = True        

    # return render(request, "rain_dance.html", {"message": message, "bill": bill})
    return render(request, "rain_dance.html", {
    "bill": bill,
    "final_bill": final_bill,
    "message": message,
    "form_data": form_data,
    "booking_confirmed": booking_confirmed,
    })

def load_chatbot_dataset():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    dataset_path = os.path.join(
        BASE_DIR,
        "Chatbot",
        "Chatbot_Dataset.json"
    )

    with open(dataset_path, "r" , encoding="utf-8") as f:
        chatbot_data = json.load(f)["qa_pairs"]

    return chatbot_data    
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chatbot_response(request):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    model_path = os.path.join(BASE_DIR,"Chatbot","chatbot_model.pkl")
    vectorizer_path = os.path.join(BASE_DIR,"Chatbot","vectorizer.pkl")

    with open(model_path,"rb") as f:
        model = pickle.load(f)

    with open(vectorizer_path,"rb") as f:
        vectorizer = pickle.load(f)

    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message")
        user_vector = vectorizer.transform([user_message])

        prediction = model.predict(user_vector)

        return JsonResponse({"reply":prediction[0]})     



def food_ordering(request):
    message = ""
    order_summary = None

    if request.method == "POST":
        items = []
        total = 0

        item_names = request.POST.getlist("item_name")
        item_prices = request.POST.getlist("item_prices")
        item_details = request.POST.getlist("item_details")

        for name , price , detail in zip(item_names , item_prices , item_details):
            price = float(price)
            total += price
            items.append({
                "name" : name,
                "price" : price,
                "details" : detail
            })

        if not items :
            message = "Your cart is empty!"
        else : 
            message = "Order placed successfully! "
            order_summary = {
                "items":items,
                "total":round(total , 2)
            }

        return render(request , "food_ordering.html",{
            "message":message,
            "order_summary" : order_summary,
        })    
    
    return render(request , "food_ordering.html",{
        "message":message,
        "order_summary":order_summary,
    })

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# from django.contrib.auth.models import User
from rollerCoasterRides.models import User
from django.contrib import messages

def register_login(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        # ── LOGIN ──
        if action == 'login':
            email    = request.POST.get('email', '').strip()
            password = request.POST.get('password', '')

            try:
                username = User.objects.get(email=email).username
            except User.DoesNotExist:
                username = None

            user = authenticate(request, username=username, password=password) if username else None

            if user is not None:
                login(request, user)
                return redirect('home')          # change to your home URL name
            else:
                messages.error(request, 'Invalid email or password.')
                return render(request, 'register_login.html', {
                    'active_tab': 'login'
                })

        # ── REGISTER ──
        elif action == 'register':
            name      = request.POST.get('name', '').strip()
            email     = request.POST.get('email', '').strip()
            password1 = request.POST.get('password1', '')
            password2 = request.POST.get('password2', '')

            if password1 != password2:
                messages.error(request, 'Passwords do not match.')
                return render(request, 'register_login.html', {
                    'active_tab': 'register'
                })

            if User.objects.filter(email=email).exists():
                messages.error(request, 'An account with this email already exists.')
                return render(request, 'register_login.html', {
                    'active_tab': 'register'
                })

            # Split full name into first/last (gracefully handles single names)
            parts = name.split(' ', 1)
            first_name = parts[0]
            last_name  = parts[1] if len(parts) > 1 else ''

            user = User.objects.create_user(
                username=email,       # use email as username — keeps it unique
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name,
            )
            login(request, user)
            return redirect('home')      # change to your home URL name

    # ── GET ──
    return render(request, 'register_login.html', {
        'active_tab': 'login'
    })