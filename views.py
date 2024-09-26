from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.mail import EmailMessage

from django.shortcuts import render
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
global scaler








def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')
@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

def getPredictions(Gender,Ever_Married,Age,Graduated,Profession,Work_Experience,Spending_Score,Family_Size):
    model = pickle.load(open('DT.pkl', 'rb'))
    new_data = {'Gender': Gender,
            'Ever_Married': Ever_Married,
            'Age': Age,
            'Graduated': Graduated,
            'Profession':Profession,
            'Work_Experience': Work_Experience,
            'Spending_Score': Spending_Score,
            'Family_Size': Family_Size}
    new_df = pd.DataFrame([new_data])
    prediction = model.predict(new_df)
    return (prediction)


def result(request):
    Email = str(request.GET['Email'])
    Gender = str(request.GET['Gender'])
    Ever_Married = str(request.GET[ 'Ever_Married'])
    Age = float(request.GET[ 'Age'])
    Graduated = str(request.GET[ 'Graduated'])
    Profession = str(request.GET[ 'Profession'])
    Work_Experience = float(request.GET[ 'Work_Experience'])
    Spending_Score = str(request.GET[ 'Spending_Score'])
    Family_Size = float(request.GET[ 'Family_Size'])
    
    result = getPredictions(Gender,Ever_Married,Age,Graduated,Profession,Work_Experience,Spending_Score,Family_Size)
    if result[0]=='A':
        res= 'A'
        subject = 'CUSTOMER SEGMENTATION'
        message ="The primary goal of customer segmentation is to identify and understand specific subsets of customers to enhance marketing strategies, sales efforts, and product development. This approach leads to more personalized customer experiences, increased customer satisfaction, and improved loyalty."
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [Email]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        try:
        # Send the email
            email.attach_file('upload/A.docx')
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='B':
        res= 'B'
        subject = 'CUSTOMER SEGMENTATION'
        message ="The primary goal of customer segmentation is to identify and understand specific subsets of customers to enhance marketing strategies, sales efforts, and product development. This approach leads to more personalized customer experiences, increased customer satisfaction, and improved loyalty."
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [Email]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        try:
        # Send the email
            email.attach_file('upload/B.docx')
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    elif result[0]=='C':
        res= 'C'
        subject = 'CUSTOMER SEGMENTATION'
        message ="The primary goal of customer segmentation is to identify and understand specific subsets of customers to enhance marketing strategies, sales efforts, and product development. This approach leads to more personalized customer experiences, increased customer satisfaction, and improved loyalty."
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [Email]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        try:
        # Send the email
            email.attach_file('upload/C.docx')
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        res= 'D'
        subject = 'CUSTOMER SEGMENTATION'
        message ="The primary goal of customer segmentation is to identify and understand specific subsets of customers to enhance marketing strategies, sales efforts, and product development. This approach leads to more personalized customer experiences, increased customer satisfaction, and improved loyalty."
        from_email = 'praveenjana6@gmail.com'  # Update with your email
        recipient_list = [Email]  # Update with the recipient's email
        email=EmailMessage(subject, message, from_email, recipient_list)
        try:
        # Send the email
            email.attach_file('upload/D.docx')
            email.send()
        except Exception as e:
         # Handle exceptions here, you can log the error or take appropriate action
            return HttpResponse(f"An error occurred: {e}", status=500)
    return render(request, 'result.html', {'result': res})