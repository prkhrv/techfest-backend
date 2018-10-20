from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy

#Forms
from fest_app.forms import CustomUserCreationForm
from Events.forms import WaterRocketryForm,RoboSoccerForm,karyanitiForm,MindFizzForm,CodeWarForm,WebDesigningForm,TechnicalQuizForm,PosterAndPresentationForm,IndustrialCaseStudyForm,RoboRaceForm,PUBGForm,GuessTheBondForm,JustaMinuteForm,PosterMakingForm,CosmeticForm
from django.contrib.auth.forms import UserCreationForm

# decorators
from django.contrib.auth.decorators import login_required

# models
from Events.models import RoboSoccer,WaterRocketry,karyaniti,MindFizz,CodeWar,WebDesigning,TechnicalQuiz,PosterAndPresentation,IndustrialCaseStudy,RoboRace,PUBG,GuessTheBond,JustaMinute,PosterMaking,Cosmetic

#excel sheets
import csv

#HttpResponse
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

@login_required
def events(request):
    return render(request,'events.html')    

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def success(request):
    return render(request,'success.html')
#1
def me01(request):
    #event_name
    event_name = "WATER ROCKETRY"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = WaterRocketryForm()
    abc = request.user
    try:
        var1 = WaterRocketry.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except WaterRocketry.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = WaterRocketryForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#2
def me02(request):
    #event_name
    event_name = "ROBO SOCCER"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = RoboSoccerForm()
    abc = request.user
    try:
        var1 = RoboSoccer.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except RoboSoccer.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = RoboSoccerForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#3
def mba01(request):

    #event_name
    event_name = "KARYANITI"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = karyanitiForm()
    abc = request.user
    try:
        var1 = karyaniti.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except karyaniti.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = karyanitiForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#4
def ece01(request):

    #event_name
    event_name = "MIND FIZZ"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = MindFizzForm()
    abc = request.user
    try:
        var1 = MindFizz.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except MindFizz.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = MindFizzForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#5
def cse01(request):

    #event_name
    event_name = "CODE WAR"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = CodeWarForm()
    abc = request.user
    try:
        var1 = CodeWar.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except CodeWar.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = CodeWarForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#6
def it01(request):
    #event_name
    event_name = "WEB DESIGNING"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = WebDesigningForm()
    abc = request.user
    try:
        var1 = WebDesigning.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except WebDesigning.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = WebDesigningForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#7
def mca01(request):
    #event_name
    event_name = "TECHNICAL QUIZ"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = TechnicalQuizForm()
    abc = request.user
    try:
        var1 = TechnicalQuiz.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except TechnicalQuiz.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = TechnicalQuizForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#8
def mca02(request):
    #event_name
    event_name = "E-POSTER MAKING & PRESENTATIONS"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = PosterAndPresentationForm()
    abc = request.user
    try:
        var1 = PosterAndPresentation.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except PosterAndPresentation.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = PosterAndPresentationForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})


#9
def ch01(request):
    #event_name
    event_name = "INDUSTRIAL CASE STUDY"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = IndustrialCaseStudyForm()
    abc = request.user
    try:
        var1 = IndustrialCaseStudy.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except IndustrialCaseStudy.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = IndustrialCaseStudyForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#10
def en01(request):
    #event_name
    event_name = "ROBO RACE"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = RoboRaceForm()
    abc = request.user
    try:
        var1 = RoboRace.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except RoboRace.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = RoboRaceForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#11
def en02(request):
    #event_name
    event_name = "PUBG"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = PUBGForm()
    abc = request.user
    try:
        var1 = PUBG.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except PUBG.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = PUBGForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#12
def civ01(request):
    #event_name
    event_name = "GUESS THE BOND?"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = GuessTheBondForm()
    abc = request.user
    try:
        var1 = GuessTheBond.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except GuessTheBond.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = GuessTheBondForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#13
def bt01(request):
    #event_name
    event_name = "JUST A MINUTE"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = JustaMinuteForm()
    abc = request.user
    try:
        var1 = JustaMinute.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except JustaMinute.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = JustaMinuteForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#14
def bph01(request):
    #event_name
    event_name = "POSTER MAKING"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = PosterMakingForm()
    abc = request.user
    try:
        var1 = PosterMaking.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except PosterMaking.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = PosterMakingForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

#15
def bph02(request):
    #event_name
    event_name = "COSMETICS"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = CosmeticForm()
    abc = request.user
    try:
        var1 = Cosmetic.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except Cosmetic.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = CosmeticForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,})

def excel(request):

    if(request.method=='POST'):
        token = request.POST.get('token')
        if(token == 'me01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="WaterRocketry_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2','Member 3','Member 4',])

            users = WaterRocketry.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response
        elif(token == 'me02'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="RoboSoccer_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2','Member 3','Member 4',])
            users = RoboSoccer.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response
        elif(token == 'mba01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="karyaniti_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2','Member 3','Member 4',])
            users = karyaniti.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response
        elif(token == 'ece01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="MindFizz_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2','Member 3','Member 4',])
            users = MindFizz.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response
        elif(token == 'cse01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="CodeWar_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = CodeWar.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'it01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="WebDesigning_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = WebDesigning.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'mca01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="TechnicalQuiz_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = TechnicalQuiz.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'mca02'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="PosterAndPresentation_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year',])
            users = PosterAndPresentation.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'ch01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="IndustrialCaseStudy_participant.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = IndustrialCaseStudy.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response
        elif(token == 'en01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="RoboRace_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2','Member 3','Member 4',])
            users = RoboRace.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'en02'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="PUBG_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year',])
            users = PUBG.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'civ01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="GuessTheBond_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = GuessTheBond.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'bt01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="JustaMinute_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year',])
            users = JustaMinute.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'bph01'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="PosterMaking_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = PosterMaking.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'bph02'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Cosmetic_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = Cosmetic.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2')
            for user in users:
                writer.writerow(user)
            return response

        else:
            error = "Please Enter a Valid Token"
            return render(request,'download.html',{'error':error,})

    return render(request,'download.html')

# *****************************************************
