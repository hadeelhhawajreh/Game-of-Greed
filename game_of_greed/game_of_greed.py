'''
Feature Tasks and Requirements
Today is all about tackling the highest risk and/or highest priority features - scoring, dice rolling and banking of points.
Define a GameLogic class in game_of_greed/game_logic.py file.
Handle calculating score for dice roll
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to rules of game.
Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.
Handle banking points
Define a Banker class
Add a shelf instance method
Input to shelf is the amount of points (integer) to add to shelf.
shelf should temporarily store unbanked points.
Add a bank instance method
bank should add any points on the shelf to total and reset shelf to 0.
bank output should be the amount of points added to total from shelf.
Add a clear_shelf instance method
clear_shelf should remove all unbanked points.
Implementation Notes
Review rules of game
Play game online
User Acceptance Tests
Create tests/test_game_logic.py file.

'''

from abc import ABC
from collections import Counter
import random
class GameLogic:
    @staticmethod
    def calculate_score(data):
        # return value->rules
        score=0
        conut=Counter(data)
        if len(conut.most_common())==6 and conut.most_common()[0][1]==1:
            score+=1500
            return score
        if len(conut.most_common())==3 and conut.most_common()[0][1]==2 and conut.most_common()[1][1]==2 and conut.most_common()[2][1]==2:
            score+=1500
            return score
        if len(data) == 1:
            if data[0]==1:
                score +=100
            if data[0]==5:
                score+=50
        if len(data)==2:
            score+=data.count(1)*100
            score+=data.count(5)*50
        if len(data)==3:
            if data.count(1)==3:
                score +=1000
            if data.count(2)==3:
                score +=200
            if data.count(3)==3:
                score+=300
            if data.count(4)==3:
                score+=400
            if data.count(5)==3:
                score+=500
            if data.count(6)==3:
                score+=600
            if data.count(1)==2:
                score+=200
            if data.count(1)==1:
                score+=100
            if data.count(5)==2:
                score+=100
            if data.count(5)==1:
                score+=50
        if len(data)==4:
            if data.count(1)==4:
                score +=2000
            if data.count(2)==4:
                score +=400
            if data.count(3)==4:
                score+=600
            if data.count(4)==4:
                score+=800
            if data.count(5)==4:
                score+=1000
            if data.count(6)==4:
                score+=1200
            if data.count(1)==3:
                score +=1000
            if data.count(2)==3:
                score +=200
            if data.count(3)==3:
                score+=300
            if data.count(4)==3:
                score+=400
            if data.count(5)==3:
                score+=500
            if data.count(6)==3:
                score+=600
            if data.count(1)==2:
                score+=200
            if data.count(1)==1:
                score+=100
            if data.count(5)==2:
                score+=100
            if data.count(5)==1:
                score+=50
        
        if len(data)==5:
            if data.count(1)==5:
                score +=3000
            if data.count(2)==5:
                score +=600
            if data.count(3)==5:
                score+=900
            if data.count(4)==5:
                score+=1200
            if data.count(5)==5:
                score+=1500
            if data.count(6)==5:
                score+=1800
            if data.count(1)==4:
                score +=2000
            if data.count(2)==4:
                score +=400
            if data.count(3)==4:
                score+=600
            if data.count(4)==4:
                score+=800
            if data.count(5)==4:
                score+=1000
            if data.count(6)==4:
                score+=1200
            if data.count(1)==3:
                score +=1000
            if data.count(2)==3:
                score +=200
            if data.count(3)==3:
                score+=300
            if data.count(4)==3:
                score+=400
            if data.count(5)==3:
                score+=500
            if data.count(6)==3:
                score+=600
            if data.count(1)==2:
                score+=200
            if data.count(1)==1:
                score+=100
            if data.count(5)==2:
                score+=100
            if data.count(5)==1:
                score+=50
        
        if len(data)==6:
            if data.count(1)==6:
                score +=4000
            if data.count(2)==6:
                score +=800
            if data.count(3)==6:
                score+=1200
            if data.count(4)==6:
                score+=1600
            if data.count(5)==6:
                score+=2000
            if data.count(6)==6:
                score+=2400
            if data.count(1)==5:
                score +=3000
            if data.count(2)==5:
                score +=600
            if data.count(3)==5:
                score+=900
            if data.count(4)==5:
                score+=1200
            if data.count(5)==5:
                score+=1500
            if data.count(6)==5:
                score+=1800
            if data.count(1)==4:
                score +=2000
            if data.count(2)==4:
                score +=400
            if data.count(3)==4:
                score+=600
            if data.count(4)==4:
                score+=800
            if data.count(5)==4:
                score+=1000
            if data.count(6)==4:
                score+=1200
            if data.count(1)==3:
                score +=1000
            if data.count(2)==3:
                score +=200
            if data.count(3)==3:
                score+=300
            if data.count(4)==3:
                score+=400
            if data.count(5)==3:
                score+=500
            if data.count(6)==3:
                score+=600
            if data.count(1)==2:
                score+=200
            if data.count(1)==1:
                score+=100
            if data.count(5)==2:
                score+=100
            if data.count(5)==1:
                score+=50
        return score


    @staticmethod
    def roll_dice(value):
        result = []
        i=1
        while i<= value:
            result.append(random.randint(1,6))
            tuple_result=tuple(result)
            i +=1
        return tuple_result  

        

class Banker:
   
    def __init__(self):
        self.balance=0
        self.shelved=0
    
    
    def shelf(self,value):
        self.shelved = value


    def bank(self):
        self.balance += self.shelved
        self.shelved = 0

    def clear_shelf(self):
        self.shelved=0


