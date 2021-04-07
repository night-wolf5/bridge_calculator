from django.db import models

# Create your models here.
class game():
    score = 0
    Team_1 = 0
    Team_2 = 0
    class rules:
        current_team = ''
        last_score = 0
        point_rules = {('N',1):90,
                        ('N',2):120,
                        ('N',3):400,
                        ('N',4):430,
                        ('N',5):460,
                        ('N',6):990,
                        ('N',7):1520,
                        ('S',1):80,
                        ('S',2):110,
                        ('S',3):140,
                        ('S',4):420,
                        ('S',5):450,
                        ('S',6):980,
                        ('S',7):1510,
                        ('H',1):80,
                        ('H',2):110,
                        ('H',3):140,
                        ('H',4):420,
                        ('H',5):450,
                        ('H',6):980,
                        ('H',7):1510,
                        ('D',1):70,
                        ('D',3):90,
                        ('D',2):110,
                        ('D',4):130,
                        ('D',5):400,
                        ('D',6):920,
                        ('D',7):1440,
                        ('C',1):70,
                        ('C',2):90,
                        ('C',3):110,
                        ('C',4):130,
                        ('C',5):400,
                        ('C',6):920,
                        ('C',7):1440}

        double_points = {('N',1):180,
                         ('N',2):490,
                         ('N',3):550,
                         ('N',4):610,
                         ('N',5):670,
                         ('N',6):1230,
                         ('N',7):1790,
                         ('S',1):160,
                         ('S',2):470,
                         ('S',3):530,
                         ('S',4):590,
                         ('S',5):650,
                         ('S',6):1210,
                         ('S',7):1770,
                         ('H',1):160,
                         ('H',2):470,
                         ('H',3):530,
                         ('H',4):590,
                         ('H',5):650,
                         ('H',6):1210,
                         ('H',7):1770,
                         ('D',1):140,
                         ('D',2):180,
                         ('D',3):470,
                         ('D',4):510,
                         ('D',5):550,
                         ('D',6):1090,
                         ('D',7):1360,
                         ('C',1):140,
                         ('C',2):180,
                         ('C',3):470,
                         ('C',4):410,
                         ('C',5):550,
                         ('C',6):1090,
                         ('C',7):1360}

        double_negative = {-1 : 100,
                           -2 : 300,
                           -3 : 500,
                           -4 : 800,
                           -5 : 1100,
                           -6 : 1400,
                           -7 : 1700}
    def calc(self,house, calls, extra_tricks, type):
        if extra_tricks == '':
            extra_tricks = 0
        extra_tricks = int(extra_tricks)
        calls = int(calls)
        if extra_tricks >= 0:
            if house == 'N' or 'S' or 'H':
                score = self.rules.point_rules[house, calls] + (extra_tricks * 30)
            elif house == 'D' or 'C':
                score = self.rules.point_rules[house, calls] + (extra_tricks * 20)
            
            if type == 'X1':
                score = self.rules.double_points[house, calls] + (extra_tricks * 100)
        elif extra_tricks < 0:
            score = (extra_tricks * 50)
            if type == 'X1':
                score = -(self.rules.double_negative[extra_tricks])

        return score
    
    def Team_1_score(self, score):
        self.Team_1 = self.Team_1 + score

    def Team_2_score(self, score):
        self.Team_2 = self.Team_2 + score