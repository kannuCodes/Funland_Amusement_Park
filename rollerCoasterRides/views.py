
import pickle

from django.http import JsonResponse
from django.shortcuts import render
import json
import os

def home(request):
    return render(request,'home.html') 

def index(request):
    bill = 0
    message ="Welcome to RollerCoaster Rides!!!"
    name = request.POST.get("name","").upper()
    age = int(request.POST.get("age") or 0)
    height = int(request.POST.get("height") or 0)
    seat = request.POST.get("seat","").upper()

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

    return render(request,"designnn.html",{"bill": bill,"message": message})    




def drop_tower(request):
    message = ""
    bill = None
    if request.method == "POST":
        age = int(request.POST.get("age"))
        weight = int(request.POST.get("weight"))
        harness_type = (request.POST.get("harness_type") or "").upper()  # example attribute for drop tower

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
            

    return render(request, "drop_tower.html", {"message": message, "bill": bill})


def bumper_cars(request):
    message = ""
    bill = None
    if request.method == "POST":
        name = request.POST.get("name","").upper()
        age = int(request.POST.get("age") or 0)
        num_laps = int(request.POST.get("laps")or 0)
        car_type = (request.POST.get("car_type") or "").upper()

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


    return render(request, "bumper_cars.html", {"message": message, "bill": bill})


def ferris_wheel(request):
    message = ""
    bill = None
    if request.method == "POST":
        age = int(request.POST.get("age") or 0)
        cabin_type = (request.POST.get("seat") or "").upper()
        num_rounds = int(request.POST.get("rounds") or 0)

        bill = 100
        if age < 12 and age >7:
            bill *= 0.5
            message = "Child discount applied!"
        if cabin_type == "VIP":
            bill += 50
        if num_rounds >11 and num_rounds<21:
            bill += 100

    return render(request, "ferris_wheel.html", {"message": message, "bill": bill})


def water_slides(request):
    message = ""
    bill = None
    if request.method == "POST":
        # num_slides = int(request.POST.get("slides"))
        age = int(request.POST.get("age") or 0)
        height = int(request.POST.get("age") or 0)
        slide_type = (request.POST.get("slide") or "").upper()

        bill = 120
        if age < 12:
            bill *= 0.5
            message = "Child discount applied!"

        if slide_type == "EXTREME":
            bill += 150     
    return render(request, "water_slides.html", {"message": message, "bill": bill})


def rain_dance(request):
    message = ""
    bill = None
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        ticket_type = (request.POST.get("ticket") or "").upper()
        dance_gear = (request.POST.get("gear") or "").upper()


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

    return render(request, "rain_dance.html", {"message": message, "bill": bill})

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