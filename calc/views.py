from django.shortcuts import render
from .classes import gam
# Create your views here.

print('page load')
def home(request):
    #global gam
    #gam = game()
    return render(request,'home.html')

def calculate(request):
    req_values = (request.GET)
    if req_values:
        team = req_values['Teams']
        house = req_values['contrat2']
        calls = req_values['contrat1']
        extra_tricks = req_values['levees']
        typee = req_values['contrat3']
        print('game type1', gam)
        score = gam.calc(house, calls, extra_tricks,typee)
        gam.last_score = score
        #print(req_values['contrat1'], calls)
        if team == 'Team1':
            gam.Team_1_score(score)
        elif team == 'Team2':
            gam.Team_2_score(score)
        
        print('score',score)
        print('Team1',gam.Team_1)
        print('Team2',gam.Team_2)
        gam.current_team = team
        print('game type2', gam)
    return render(request,'home.html',{'Team1':gam.Team_1, 'Team2':gam.Team_2})

def new_game(request):
    global gam
    del gam
    #gam = game()
    print('gam')
    return render(request,'home.html')

def undo(request):
    #team = req_values['Teams']
    global gam
    if gam.current_team == "Team1":
        gam.Team_1 = gam.Team_1 - gam.last_score
    
    else:
        gam.Team_2 = gam.Team_2 - gam.last_score
    print(gam.current_team)
    return render(request,'home.html', {'Team1':gam.Team_1, 'Team2':gam.Team_2})