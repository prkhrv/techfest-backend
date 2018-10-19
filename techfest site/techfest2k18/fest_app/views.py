from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy

#Forms
from fest_app.forms import CustomUserCreationForm
from Events.forms import WaterRocketryForm,RoboSoccerForm,karyanitiForm,MindFizzForm,CodeWarForm,WebDesigningForm,TechnicalQuizForm,PosterAndPresentationForm,IndustrialCaseStudyForm,RoboRaceForm,StartUpMasterForm,GuessTheBondForm,JustaMinuteForm,PosterMakingForm,CosmeticForm
from django.contrib.auth.forms import UserCreationForm

# decorators
from django.contrib.auth.decorators import login_required

# models
from Events.models import RoboSoccer,WaterRocketry,karyaniti,MindFizz,CodeWar,WebDesigning,TechnicalQuiz,PosterAndPresentation,IndustrialCaseStudy,RoboRace,StartUpMaster,GuessTheBond,JustaMinute,PosterMaking,Cosmetic


# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')

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
    event_name = "START UP MASTERS"
    #event_description
    event_description = "Here is the description"
    # ********************************************************
    form = StartUpMasterForm()
    abc = request.user
    try:
        var1 = StartUpMaster.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except StartUpMaster.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = StartUpMasterForm(request.POST)
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
