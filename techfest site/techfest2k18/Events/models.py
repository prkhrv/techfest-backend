from django.db import models
from fest_app.models import CustomUser

# Create your models here.

# 1
class WaterRocketry(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='ME01')
    event_name = models.CharField(max_length=20,default='WATER ROCKETRY')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    member_3 = models.CharField(max_length=20,default='',blank=True)
    member_4 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 2
class RoboSoccer(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='ME02')
    event_name = models.CharField(max_length=20,default='ROBO SOCCER')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=10,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    member_3 = models.CharField(max_length=20,default='',blank=True)
    member_4 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 3
class karyaniti(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='MBA01')
    event_name = models.CharField(max_length=20,default='KARYANITI')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    member_3 = models.CharField(max_length=20,default='',blank=True)
    member_4 = models.CharField(max_length=20,default='',blank=True)
    def __str__(self):
        return self.first_name


# 4
class MindFizz(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='ECE01')
    event_name = models.CharField(max_length=20,default='MIND FIZZ')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    member_3 = models.CharField(max_length=20,default='',blank=True)
    member_4 = models.CharField(max_length=20,default='',blank=True)
    def __str__(self):
        return self.first_name


# 5
class CodeWar(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='CSE01')
    event_name = models.CharField(max_length=20,default='CODE WAR')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    def __str__(self):
        return self.first_name


# 6
class WebDesigning(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='IT01')
    event_name = models.CharField(max_length=20,default='WEB DESIGNING')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 7
class TechnicalQuiz(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='MCA01')
    event_name = models.CharField(max_length=20,default='TECHNICAL QUIZ')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 8
class PosterAndPresentation(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='MCA02')
    event_name = models.CharField(max_length=40,default='POSTER & PRESENTATIONS')

    def __str__(self):
        return self.first_name


# 9
class IndustrialCaseStudy(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='CH01')
    event_name = models.CharField(max_length=30,default='INDUSTRIAL CASE STUDY')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 10
class RoboRace(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='EN01')
    event_name = models.CharField(max_length=20,default='ROBO RACE')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)
    member_3 = models.CharField(max_length=20,default='',blank=True)
    member_4 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name

# 11
class GuessTheBond(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='CIV01')
    event_name = models.CharField(max_length=30,default='GUESS THE BOND?')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 12
class JustaMinute(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='BT01')
    event_name = models.CharField(max_length=20,default='JUST A MINUTE')

    def __str__(self):
        return self.first_name


# 13
class PosterMaking(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='Bph01')
    event_name = models.CharField(max_length=20,default='POSTER MAKING')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name


# 14
class Cosmetic(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='Bph02')
    event_name = models.CharField(max_length=20,default='COSMETICS')
    team_name = models.CharField(max_length=20,default='')
    number_of_members = models.CharField(max_length=20,default='')
    member_1 = models.CharField(max_length=20,default='',blank=True)
    member_2 = models.CharField(max_length=20,default='',blank=True)

    def __str__(self):
        return self.first_name

# 15
class PUBG(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20,default='')
    last_name = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=40,default='')
    roll = models.CharField(max_length=10,default='')
    phone = models.CharField(max_length=10,default='')
    branch = models.CharField(max_length=10,default='')
    section = models.CharField(max_length=2,default='')
    year = models.CharField(max_length=10,default='')
    event_id = models.CharField(max_length=5,default='PUBG')
    event_name = models.CharField(max_length=30,default='PUBG')


    def __str__(self):
        return self.first_name
