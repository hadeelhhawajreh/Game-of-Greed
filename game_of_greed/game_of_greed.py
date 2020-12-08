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

    
class Game:
    def __init__(self,roller=None):
        self.roller=roller or GameLogic.roll_dice(roller)
    
    @staticmethod
    def quit(score):
        print(f'Total score is {score} points')
        print(f'Thanks for playing. You earned {score} points')


    @staticmethod
    def bank(dice_to_keep,remaining_dice,roll):
        if type(int(dice_to_keep)) == int:
                    if len(dice_to_keep) <= remaining_dice:
                        user_input = [int(i) for i in dice_to_keep.split(",")]
                        for i in user_input:
                            if not i in roll:
                                Game.cheater(roll)


                    else:
                        Game.cheater(roll)
        
        else:
            print('pleas enter valid input..')
                                
    @staticmethod
    def cheater(roll):
        print('Cheater!!! Or possibly made a typo...')
        print(roll)
        dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
        return dice_to_keep


    def play(self):
        print('Welcome to Game of Greed')
        res = input('Wanna play?')
        if res == 'n':
            print('OK. Maybe another time')
        elif res == 'y':
            play = True
            round = 1
            remaining_dice = 6
            score = 0

            while play:
                print(f'Starting round {round}')
                print(f'Rolling {remaining_dice} dice...')
                roll = self.roller(remaining_dice)
                # Game.print_roll(roll)
                print(','.join([str(i) for i in roll]))
                dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                if dice_to_keep == 'q':
                    Game.quit(score)
        
                else:
                    
                        
                    g = GameLogic()
                    unbank = g.calculate_score((int(dice_to_keep),))
                # if type(int(dice_to_keep)) == int:
                #     if len(dice_to_keep) <= remaining_dice:
                #         user_input = [int(i) for i in dice_to_keep.split(",")]
                #         for i in user_input:
                #             if not i in roll:
                #                 print('Cheater!!! Or possibly made a typo...')
                #                 print(roll)
                #                 dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                                
                #             else:
                #                 unbank = g.calculate_score((int(dice_to_keep),))
                #                 print(f'You have {unbank} unbanked points and {remaining_dice} dice remaining')
                #                 res = input(f'(r)oll again, (b)ank your points or (q)uit ')
                #                 if dice_to_keep == 'q':
                #                     unbank = 0
                #                 print(f'Total score is {score} points')
                #                 print(f'Thanks for playing. You earned {score} points')
                # else:
                #     print('pleas enter valid input..')

                    print(f'You have {unbank} unbanked points and {remaining_dice} dice remaining')
                    res = input(f'(r)oll again, (b)ank your points or (q)uit ')
                    if res == 'b':
                        score +=unbank 
                        print(f'You banked {unbank} points in round {round}')
                        print(f'Total score is {score} points')
                    round+=1
                    print(f'Starting round {round}')
                    print(f'Rolling {remaining_dice+1} dice...')
                    roll2 = self.roller(remaining_dice)
                    # Game.print_roll(roll)
                    print(','.join([str(i) for i in roll2]))
                    dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                    if dice_to_keep == 'q':
                        print(f'Total score is {score} points')
                        print(f'Thanks for playing. You earned {score} points')
                    else:
                        unbank = g.calculate_score((int(dice_to_keep),))
                        print(f'You have {unbank} unbanked points and {remaining_dice} dice remaining')
                        res=input('(r)oll again, (b)ank your points or (q)uit ')
                        if res == 'b':
                            score +=unbank 
                            print(f'You banked {unbank} points in round {round}')
                            print(f'Total score is {score} points')
                            round+=1
                            print(f'Starting round {round}')
                            print(f'Rolling {remaining_dice+1} dice...')
                            roll2 = self.roller(remaining_dice)
                            # Game.print_roll(roll)
                            print(','.join([str(i) for i in roll2]))
                            dice_to_keep = input('Enter dice to keep (no spaces), or (q)uit: ')
                            if dice_to_keep == 'q':
                                print(f'Total score is {score} points')
                                print(f'Thanks for playing. You earned {score} points')



