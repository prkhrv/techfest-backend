from django import forms
from .models import RoboSoccer,WaterRocketry,karyaniti,MindFizz,CodeWar,WebDesigning,TechnicalQuiz,PosterAndPresentation,IndustrialCaseStudy,RoboRace,StartUpMaster,GuessTheBond,JustaMinute,PosterMaking,Cosmetic


#1
class WaterRocketryForm(forms.ModelForm):
    class Meta():
        model = WaterRocketry
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2','member_3','member_4',)

#2
class RoboSoccerForm(forms.ModelForm):
    class Meta():
        model = RoboSoccer
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2','member_3','member_4',)

#3
class karyanitiForm(forms.ModelForm):
    class Meta():
        model = karyaniti
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2','member_3','member_4',)

#4
class MindFizzForm(forms.ModelForm):
    class Meta():
        model = MindFizz
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2','member_3','member_4',)

#5
class CodeWarForm(forms.ModelForm):
    class Meta():
        model = CodeWar
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)

#6
class WebDesigningForm(forms.ModelForm):
    class Meta():
        model = WebDesigning
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#7
class TechnicalQuizForm(forms.ModelForm):
    class Meta():
        model = TechnicalQuiz
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#8
class PosterAndPresentationForm(forms.ModelForm):
    class Meta():
        model = PosterAndPresentation
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year',)
#9
class IndustrialCaseStudyForm(forms.ModelForm):
    class Meta():
        model = IndustrialCaseStudy
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#10
class RoboRaceForm(forms.ModelForm):
    class Meta():
        model = RoboRace
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2','member_3','member_4',)
#11
class StartUpMasterForm(forms.ModelForm):
    class Meta():
        model = StartUpMaster
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#12
class GuessTheBondForm(forms.ModelForm):
    class Meta():
        model = GuessTheBond
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#13
class JustaMinuteForm(forms.ModelForm):
    class Meta():
        model = JustaMinute
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year',)

#14
class PosterMakingForm(forms.ModelForm):
    class Meta():
        model = PosterMaking
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
#15
class CosmeticForm(forms.ModelForm):
    class Meta():
        model = Cosmetic
        fields = ('user','first_name','last_name','email','roll','phone','branch','section','year','team_name','number_of_members','member_1','member_2',)
