from django.shortcuts import render,redirect
from django.views import generic
from django.urls import reverse_lazy

#Forms
from fest_app.forms import CustomUserCreationForm
from Events.forms import WaterRocketryForm,RoboSoccerForm,karyanitiForm,MindFizzForm,CodeWarForm,WebDesigningForm,TechnicalQuizForm,PosterAndPresentationForm,IndustrialCaseStudyForm,RoboRaceForm,PUBGForm,GuessTheBondForm,JustaMinuteForm,PosterMakingForm,CosmeticForm,ECELLForm,PhotographyForm
from django.contrib.auth.forms import UserCreationForm

# decorators
from django.contrib.auth.decorators import login_required

# models
from Events.models import RoboSoccer,WaterRocketry,karyaniti,MindFizz,CodeWar,WebDesigning,TechnicalQuiz,PosterAndPresentation,IndustrialCaseStudy,RoboRace,PUBG,GuessTheBond,JustaMinute,PosterMaking,Cosmetic,ECELL,Photography

#excel sheets
import csv

#HttpResponse
from django.http import HttpResponse
#mailing
from django.core.mail import send_mail

# Create your views here.
#devpage
def dev(request):
    return render(request,'about.html')
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
@login_required
def me01(request):
    #event_name
    event_name = "WATER ROCKETRY"
    #event_description
    event_description = "This is oldest and most educational way to learn about aerodynamics"
    #event_rules
    rules =['In 1st round top ten will be selected',
            'In 2nd round top 3 will be selected',
            '1.5 liters cylindrical shape bottle are allowed',
            'In bottle 45-50 pressure will be maintain by using electrical compressor',
            'Every team must have a pair of safety glasses',
            'MAX TEAM SIZE ALLOWED: 4 ']
    #JudgingCriteria
    judge = ['All conflict and final judgement will be given by concerning faculty ']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'At campus ground'
    #contact
    contact = ['vyom rajan singh- 9650327581',
                'vishal-7417511487']

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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#2
@login_required
def me02(request):
    #event_name
    event_name = "ROBO WAR"
    #event_description
    event_description = "Robo War is an Annual Robo Fight competition in which some most fearsome Robots Clash-On With each other."
    #rules
    rules = ['Participants should carry their I-cards.',
             'There will be one to one fight of bots.',
             'There will be a time of 5 minutes for first 2 rounds.',
             'If bot remains immobilized, then it will be declared loser',
             'Immobilize means: a. No motion within 30 seconds b. Motion if at least 1 inch c. If bot gets flip over',
             'Bot must not damage arena. If it does so it will be given only one warning, for the next time it will be disqualified.',
             'Bot can be disqualified in the beginning if felt unsafe.',
             'Weight limit if the bot is 30 kg.',
             'If the bot gets out of arena it will be eliminated and the competitor will be the winner of the round itself.',
             'If all the four tyres are in air, then or pin for 20 seconds then 10 points will give to the opposite team (5 points for 10 sec).',
             'If the bot keeps another bot in air for 20 secs (all the four tyres) for 20 secs, then the former gets 20 points',
             'Bots can use weapons to immobilize another bot.',
             'If any bot escapes the pin within 5 secs it will get 5 points',
             'If both the bots fall out of arena, both will be eliminated.',
             'Their will be 3 mins during whole match for technical issues',
             'If both the bots get engaged then there will be a restart for them. The time will be paused during that motion']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'At campus ground'
    #contact
    contact = ['MAYANK PRATAP SINGH(7827479788)']

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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#3
@login_required
def mba01(request):

    #event_name
    event_name = "KARYANITI"
    #event_description
    event_description = "It is a fun game, it consist of four rounds Round will be disclosed at the time of the Event only."
    #event_rules
    rules = ['MAX TEAM SIZE ALLOWED: 4']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'At campus ground'
    #contact
    contact = ['MONICA SINGH']
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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#4
@login_required
def ece01(request):

    #event_name
    event_name = "MIND FIZZ"
    #event_description
    event_description = "MIND FIZZ is a brain teasing event which well test the Thinking and Coordination Skills of the Participants through some fun and interactive activities"
    #event_rules
    rules = ['Mind Fizz has total three rounds.',
             'In ROUND 1 (BRAIN TEASER) Questions will be asked related to common sense, puzzles and riddles.All 4 members can contribute and solve questions.',
             'In ROUND 2 (LET ME KNOW) Questions will be asked related to music, songs, dialogues and movie names. Only 2 members can contribute in this round',
             'In ROUND 3 (FUN N PLAY) some Fun Game will be conducted between the participants.All 4 members can contribute in this round'
             ]
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B-Block'
    #contact
    contact = ['SUSHIL (9818311575)']
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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#5
@login_required
def cse01(request):

    #event_name
    event_name = "CODE WAR"
    #event_description
    event_description = "Code War is the Ultimate coding contest,It will test logical and Programming skills of the partcipants to the Mind Bewildering Level"
    #event_rules
    rules = ['Contestants should bring their own pen or pencils to the contest room. Blank sheets of paper will be supplied.',
            'Referees will be assigned to observe teams throughout the contest and report any problems and/or violations of the rules to the Contest Committee.',
            'Contestants may write their programs in whichever language they prefer.',
            'Individuals may not seek hints and/or ask for leads during the contest. They may, however, submit questions about procedure and/or clarification, in writing, to the Contest Committee who will ensure that all individuals receive the same information as deemed necessary.',
            'Each problem will have a specified point value. The more difficult the problem, the more points a correct solution will receive.',
            'A program may still be wrong even if it passes all the test input cases. Every effort will be made to design test cases that will minimize the chance of missing an incorrect program.',
            'A correct program will be awarded the full points, an incorrect one zero! In the event of a tie, we’ll discuss this at the time.',
            'The Contest Committee will tally the scores for each team and publish a complete list. Winners will be decided on the ranks of individuals and prizes will be distributed accordingly (certificates).',
            'Swags and Stickers will be given to all the participants',
            'MAX TEAM SIZE ALLOWED : 2']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'D-Block'
    #contact
    contact = ['Ashish (8077907960)',
               'Raksha Kak',
               'Prakhar Varshney(9818311267)']
    #mail_ids
    mail_ids = list(CodeWar.objects.values_list('email',flat=True))
    #mail_subject
    mail_subject = 'Greetings! From Code War Team, Here some details for the Event'
    #mail_message
    message = 'Event Location :- Plot 19, NIET D Block, 2nd Floor CL-1 and CL-2 \n Event Timings :- 2 PM To 5 PM \n For any Queries Contact :- Prakhar Varshney - 9818311267 \n'
    # ********************************************************
    form = CodeWarForm()
    abc = request.user
    try:
        var1 = CodeWar.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except CodeWar.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        send_mail(mail_subject,
        message,
        'developers.noida@gmail.com',
        mail_ids)
        return redirect('/success/')
    return render(request,'finish.html')

#6
@login_required
def it01(request):
    #event_name
    event_name = "WEB DESIGNING"
    #event_description
    event_description = "It is a theme based web designing event in which participants will be provided with a theme and they will have to design a web page related to that theme. Theme for the design will be disclosed at that point of time. There will be only one round of 3 hours. Participants are request to bring there own laptop installed with required tools of web development."
    #event_rules
    rules = ['Pre-designed template will not be allowed',
            'MAX TEAM SIZE ALLOWED : 4']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018-10am-1pm'
    #Venue
    venue = 'D-Block'
    #contact
    contact = ['Anish (8630170224)',
               'Shiv Bhole Singh',]
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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#7
@login_required
def mca01(request):
    #event_name
    event_name = "TECHNICAL QUIZ"
    #event_description
    event_description = "TECHNICAL QUIZ is a MCQ type technical quiz Event, which will test the technical knowledge through some mind puzzling questions"
    #event_rules
    rules = ['MAX TEAM SIZE ALLOWED : 2']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'Dept. Of MCA A Block, Room 406 A'
    #contact
    contact = ['Ashi Bansal',
               'Kekashri Joshi',
               'Mayur Agarwal']
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
    return render(request,'register2.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#8
@login_required
def mca02(request):
    #event_name
    event_name = "E-POSTER MAKING & PRESENTATIONS"
    #event_description
    event_description = " "
    #event_rules
    rules = ['MAX TEAM SIZE ALLOWED : 1']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'Dept. Of MCA A Block, Room 401 A'
    #contact
    contact = ['Ashi Bansal',
               'Kekashri Joshi',
               'Mayur Agarwal']
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
    return render(request,'register1.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})


#9
@login_required
def ch01(request):
    #event_name
    event_name = "INDUSTRIAL CASE STUDY"
    #event_description
    event_description = "Participants will be presented with a Case study related to Industries.The participants will have to answer questions related to the same,also time will be noted when the answer sheets are handed in.So the time taken by the participants is also counted."
    #event_rules
    rules = ['TIME ALLOTED MAX (25MIN)',
            'MAX TEAM SIZE ALLOWED : 2']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B Block'
    #contact
    contact = ['Sumegha 9997302244']
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
    return render(request,'register2.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#10
@login_required
def en01(request):
    #event_name
    event_name = "ROBO RACE"
    #event_description
    event_description = "Design a manually controlled ROBOT that has capability to cover maximum distance in shortest possible Time, challenging the hurdles and be one of the best opponents. Think your robot can overcome any Obstacle big or small, in the least of time. If so get it on the track and let the game begin. And bear in mind that maximizing RPM does not make you winner but winners are those who have good presence of mind, sharpness and practice."
    #event_rules
    rules = ['Team Size 1-4','Can be wireless or wired','Timing 7 min each team',
    'Maximum weight must not exceed 7 kg.',
    'Maximum power supply cannot exceed more than 12v.',
    'Readymade toys cars are not allowed.',
    'Bluetooth technology for wireless communication should be greater than 2.0.',
    'Students using R.F Module should try to make their communication non interfering',
    'This is a racing event so fastest and most balanced robot will win.',
    'The robot should not damage the arena.',
    'The robot must not leave behind any of its parts during the run; else it will result in negative marking',
    'Unethical behavior could lead to disqualification',
    "Judge's decision will be considered final",
    '5 hand touches are allowed with penalty of 10 seconds for each hand touch.']
    #JudgingCriteria
    judge = ['Participants who will touch the finish line first , after crossing each point of arena , will be the winner',
            'Participants must follow the path of arena track',
    	     'Each crossing point will have equal weightage for once only']
    #Schedule
    schedule  = 'from 10:00 a.m.'
    #Venue
    venue = 'at campus ground'
    #contact
    contact = ['Sumant Raja - 8377891122',
                'Shivam Tiwary – 9643917535']
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
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#11
@login_required
def en02(request):
    #event_name
    event_name = "PUBG"
    #event_description
    event_description = "The Way to become the college PUBG champ is HERE."
    #event_rules
    rules = ['Registration open until  all slots are occupied',
            'The event is a knockout type fixture.',
            'It is a Solo Erangel – Classic type',
            'Top 3 of the final round will be awarded as a winner',
            'Charging port will not be provided.',
            'No hacks allowed, if any individual found will be disqualified.',
            'Manage your own internet connection, any lags and bugs will not be management concern',
            'All compatible devices will be allowed. ( laptop, mobile phone and tablets)',
            ]
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B Block'
    #contact
    contact = ['SHARMISTHA (EN V)']
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
    return render(request,'register1.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#12
@login_required
def civ01(request):
    #event_name
    event_name = "GUESS THE BOND?"
    #event_description
    event_description = "“Words are a pretext , it is the inner bond that draws one person to another,not word”. A brick bond is the pattern in which bricks are laid. It applied to both brick walls and brick paving for  patios and paths as well as concrete block and other types of masonary construction"
    #event_rules
    rules = ['Use of mobile phones is prohibited.',
            'Participents can either participate individually or in a team of 2 members.',
            'The bond that is gonna be prepared by the participents is gonna be decided by the chit system at that point of time.',
            'All the materials necessary will be given to the participents during the event.',
            'A maximum amount of 15 bricks will be provided.',
            'The time limit for preparing the bond is maximum 15 minutes.']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty',]
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B Block'
    #contact
    contact = ['Sm. Rais Iqbal(V C)(9818632565 )',
               'Syed Mohammad Adil( V C ) (7065626698)']
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
    return render(request,'register2.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#13
@login_required
def bt01(request):
    #event_name
    event_name = "JUST A MINUTE"
    #event_description
    event_description = "This is an on the spot speaking skills competition, to enhance the stage skills and communication skills in their technical field. It would be consisting of three rounds."
    #event_rules
    rules = ['Individual Event']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'E Block'
    #contact
    contact = ['']
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
    return render(request,'register1.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#14
@login_required
def bph01(request):
    #event_name
    event_name = "POSTER MAKING"
    #event_description
    event_description = ""
    #event_rules
    rules = ['N/A']
    #JudgingCriteria
    judge =['Appearance',
            'Texture and consistency',
            'Product presentation',
            'Product description']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B.pharma Block'
    #contact
    contact = ['']
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
    return render(request,'register2.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#15
@login_required
def bph02(request):
    #event_name
    event_name = "COSMETICS"
    #event_description
    event_description = "In this event Participants have to prepare COSMETICS"
    #event_rules
    rules = ['No prepared raw materials are to be bought or used.',
            'Materials for labeling and container for product is to be brought by the students.',
            'Chemicals will be provided by the department',
            'Time limit- 2hrs',
            'Participants are requested to chose preparation of any one of the following  cosmetical formulations:',
            '1.	Vanishing cream',
            '2.	Lipstick',
            '3.	Herbal face pack',
            '4.	Talcum powder',
            'No. of participants- 2']
    #JudgingCriteria
    judge =['Appearance',
            'Texture and consistency',
            'Product presentation',
            'Product description']
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'B.pharma Block'
    #contact
    contact = ['']
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
    return render(request,'register2.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})
#16
@login_required
def ecell(request):
    #event_name
    event_name = "An Idea For Future"
    #event_description
    event_description = "“An Idea for Future” -  an event where students across various branches can pitch their innovative ideas that could result in a viable start-up /business /innovation. An exquisite opportunity for all budding innovators to tap their skills, pitch their idea to the esteemed panel of judges and chance to win exciting prizes."
    #event_rules
    rules = ['Team size should be maximum 4.',
            'Pitch time should not exceed - 4 mins.',
            'Elevator Pitching (point- to – point pitching)',
            'All teams should report 10 minutes prior to confirm their registration.']
    #JudgingCriteria
    judge =['Decision of the panel will be final.']
    #Schedule
    schedule  = ' Note: The schedule of the event will be conveyed through email on 26th October, 2018. Make sure you check for the same.'
    #Venue
    venue = 'A-Block 5th Floor'
    #contact
    contact = ['Mohd. Usman Ovais (9811695339)',
                'Nazuk Endlay']
    # ********************************************************
    form = ECELLForm()
    abc = request.user
    try:
        var1 = ECELL.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except ECELL.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = ECELLForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register4.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})

#17
@login_required
def pixels(request):
    #event_name
    event_name = "Photography"
    #event_description
    event_description = "NIET MEGAPIXELS brings you the ultimate Photography contest,submit your finest click and win exciting prizes."
    #event_rules
    rules = ['The contests are open for online submissiononly,through the email',
            'Mention yourname,rollnumber,branch,and contact no.while submitting your photographs.',
            'Submissions will not be accepted once the deadline lapses',
            'You may submit only 2 photos shot by you in this event',
            'Photos clicked both through camera or mobile both are acceptable for this event',
            'Every image uploaded is subject to a moderation process before it becomes visible on the contest page.NIET Megapixels reserves right to assess and disregard any submitted photo at our discretion.',
            'Photos must be shot within the campus on the day of event',
            'ONLY BLACK AND WHITE PHOTOS ARE ELIGIBLE FOR THIS EVENT',
            'Photos that portray or otherwise include inappropriate and/ or offensive content,including provocative nudity,violence,human right and/or environmental violations,and/or other contents deemed to be contrary to the law,religious,cultural & moral traditions and practices of India,are strictly prohibited and will be immediately discarded.',
            'A participant who submits any such photos may be permanently banned,subjects to strict actions taken against him/her.']
    #JudgingCriteria
    judge =['All conflict and final judgement will be given by concerning faculty',]
    #Schedule
    schedule  = '27th October,2018'
    #Venue
    venue = 'E-mail for photo Submissions: megapixels.niet@gmail.com'
    #contact
    contact = ['Pranjal Agarwal CSE 3rd year(9838375046)',
                'Satyam Srivastava CSE 3rd year(9818234038)']

    # ********************************************************
    form = PhotographyForm()
    abc = request.user
    try:
        var1 = Photography.objects.filter(user = abc)
        var2 = var1.values_list('user',flat=True).get()
    except Photography.DoesNotExist:
        var2 = 0

    if(request.method=='POST'):
        form = PhotographyForm(request.POST)
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/success/')
    return render(request,'register1.html',{'var2':var2,'event_name':event_name,'event_description':event_description,'rules':rules,'judge':judge,'schedule':schedule,'venue':venue,'contact':contact,})


#*********************************************************************************
@login_required
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

        elif(token == 'ecell'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Ecell_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = ECELL.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year','team_name','member_1','member_2','member_3','member_4')
            for user in users:
                writer.writerow(user)
            return response

        elif(token == 'pixels'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Photography_participants.csv"'
            writer = csv.writer(response)
            writer.writerow(['First Name', 'Last Name', 'Email','Roll Number','Phone Number','Branch','Section','Year','Team Name','Member 1','Member 2',])
            users = Photography.objects.all().values_list('first_name', 'last_name', 'email', 'roll','phone','branch','section','year')
            for user in users:
                writer.writerow(user)
            return response



        else:
            error = "Please Enter a Valid Token"
            return render(request,'download.html',{'error':error,})

    return render(request,'download.html')

# *****************************************************
