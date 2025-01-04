from django.shortcuts import render ,HttpResponse, redirect
from webapp.models import Prediction
from webapp.models import Registration
from webapp.forms import LoginForm
from webapp.forms import RegForm
from webapp.models import Feedback
from .models import Login
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from webapp.models import User


# To load Machine Learning Model in WebApp
import joblib
import os
from django.conf import settings

# Create your views here.

from django.shortcuts import render,redirect

def index(request):
    if request.method== "POST":
        name =request.POST.get("name")
        email =request.POST.get("email")
        desc =request.POST.get("desc")
        feedback_model=Feedback(name=name,email=email,desc=desc)
        feedback_model.save()
    return render(request,"index.html")

    
    
  
def user_form(request):
    prediction_message = ""  # Initialize with a default value
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        sex = int(request.POST.get("sex"))
        chest_pain_type = int(request.POST.get("chest_pain_type"))
        resting_ecg = int(request.POST.get("resting_ecg"))
        exercise_angina = int(request.POST.get("exercise_angina"))
        st_slope = int(request.POST.get("st_slope"))
        fasting_bs = int(request.POST.get("fasting_bs"))
        oldpeak = float(request.POST.get("oldpeak"))
        max_heart_rate = int(request.POST.get("max_heart_rate"))

        # Load the model
        model_path = os.path.join(settings.BASE_DIR, 'webapp', 'ml_model', 'svm_model.pkl')
        model = joblib.load(model_path)

        # Prepare data for prediction
        input_data = [[age, sex, chest_pain_type, resting_ecg, exercise_angina, st_slope, fasting_bs, oldpeak, max_heart_rate]]
        prediction = model.predict(input_data)[0]

        # Convert prediction to a user-friendly message
        if prediction == 1:
            prediction_message = "Heart Disease Detected"
        else:
            prediction_message = "No Heart Disease"

        # Save prediction to database
        prediction_instance = Prediction(
            name=name,
            age=age,
            sex=sex,
            chest_pain_type=chest_pain_type,
            resting_ecg=resting_ecg,
            exercise_angina=exercise_angina,
            st_slope=st_slope,
            fasting_bs=fasting_bs,
            oldpeak=oldpeak,
            max_heart_rate=max_heart_rate,
            prediction_result=prediction  # Save the result in the database
        )
        
        prediction_instance.save()
    return render(request, "user_form.html", {"prediction_message": prediction_message})
def about_us(request):
   return render(request,'about_us.html')
def doctor_ai(request):
   return render(request,'doctor_ai.html')
def registration_page(request):
    reg_form=RegForm()
    context={
        'form': reg_form
    }
    if request.method =="POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        reg_model=Registration(first_name=first_name,last_name=last_name,email=email,password=pass1,confirm_password=confirm_password)
        reg_model.save()

        if pass1!=confirm_password:
          return HttpResponse("Passwords do not match")
        if User.objects.filter(email=email).exists():
          return HttpResponse("Email already registered") 
        else:  
            my_user=User.objects.create_user( email=email, password=pass1)
            my_user.save()
            return redirect("login")
    return render(request,"registration.html")
from django.contrib import messages
def login_view(request):
    stu_form = LoginForm()
    context = {
        'form': stu_form
    }
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password")

        
        my_model = Login(email=email, password=pass1)
        my_model.save()

       
        user = authenticate(request, email=email, password=pass1)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid email or password.")
            return redirect('login')

    return render(request, "user_login.html", context)
def logout_view(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")