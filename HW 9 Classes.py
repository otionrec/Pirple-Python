#Homework Assignment #9: Classes

'''
The setters, getters and is_driving attributes are futile in this code: was only required by HW assignment
Also, the auto-hauling function solves the Need Maintenance attribute so never mind
'''

import time
import sys
from termcolor import colored, cprint
import json
import os
#import pickle

# define vehicle class - parent class
class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    '''
    #setters
    def setMake(self, make):
        self.make = make        

    def setModel(self, model):
        self.model = model      

    def setYear(self, year):
        self.year = year      

    def setWeight(self, weight):
        self.weight = weight     

    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False    
    '''
    
    '''
    #getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight
    '''

    def makedict(self):
        return {'company': self.make, 'model': self.model, 'year': self.year, 'weight': self.weight, 'nm': self.needsMaintenance, 'tsm': self.tripsSinceMaintenance, 'is_driving': False}

# Defining Cars class - inherited from vehicle class
class Cars(Vehicle):
    def __init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance, isDriving):
        Vehicle.__init__(self, make, model, year, weight, needsMaintenance, tripsSinceMaintenance)
        #self.drive_times = drive_times
        self.isDriving = isDriving
    def driving(self):
        self.isDriving = True                 
    
    def stop(self):
        self.isDriving = False

if not os.path.exists('save.json'):
    carOne = {'company': 'Tesla', 'model': 'Model 3', 'year': 2018, 'weight': 1033, 'nm': None, 'tsm': 0, 'is_driving': False}
    carTwo = {'company': 'Tesla', 'model': 'Model S', 'year': 2019, 'weight': 1019, 'nm': None, 'tsm': 0, 'is_driving': False}
    carThree = {'company': 'Tesla', 'model': 'Model X', 'year': 2020, 'weight': 1023, 'nm': None, 'tsm': 0, 'is_driving': False}
    with open('save.json', 'w') as json_file:
          json.dump([carOne, carTwo, carThree], json_file)
else:
    carOne, carTwo, carThree = json.load(open('save.json'))

# creating three instances from Cars class
carOne = Cars(*list(carOne.values()))
carTwo = Cars(*list(carTwo.values()))
carThree = Cars(*list(carThree.values()))

# Function to print car attributes         
def print_car_specs(car1, car2, car3):
    print("\n")
    title = "TESLA, Inc."
    cprint(title.center(140), 'cyan', attrs=['bold'])
    print("========================"*6)
    print('Make: ', car1.make, '     Model: ', car1.model, '     Year: ', car1.year, '     Weight: ', car1.weight,
     '     Trips Since Maintenance: ', car1.tripsSinceMaintenance, '     Needs Maintenance: ', car1.needsMaintenance)
    print("========================"*6, "\n")
    print("========================"*6)
    print('Make: ', car2.make, '     Model: ', car2.model, '     Year: ', car2.year, '     Weight: ', car2.weight,
     '     Trips Since Maintenance: ', car2.tripsSinceMaintenance, '     Needs Maintenance: ', car2.needsMaintenance)
    print("========================"*6, "\n")
    print("========================"*6)
    print('Make: ', car3.make, '     Model: ', car3.model, '     Year: ', car3.year, '     Weight: ', car3.weight,
     '     Trips Since Maintenance: ', car3.tripsSinceMaintenance, '     Needs Maintenance: ', car3.needsMaintenance)
    print("========================"*6, "\n")
    return True


# function to caution on overhauling
def over_haul(car):
    textb = colored('\nCaution! Your car will overhaul on the 100th turn, process anyway?: ', 'yellow')
    ans1 = input(textb)
    print('\n')
    if ans1.casefold() == 'yes'.casefold():
        print('\n')
        textd = colored(' Autonomous-Servicing in progress.....', 'magenta')
        def blink_once():
            sys.stdout.write('\r'+textd)
            time.sleep(0.5)                        
            sys.stdout.write('\r ')
            time.sleep(0.5)

        def blink(number):
            for x in range(number):
                blink_once()

        blink(5)  

        car.tripsSinceMaintenance = (car.tripsSinceMaintenance + car.drive_times) - 100
        car.needsMaintenance = False
        print_car_specs(carOne, carTwo, carThree)
        Choose()
    elif ans1.casefold() == 'no'.casefold():
        drive(car)
    else:
        print("Requires a 'Yes' or 'No' input\n")
        over_haul(car)

# Function to move car a number of times
def drive(car):
        
    texta = colored("\nHow many times do you want to drive the Car: ", 'green')       
    nice = input(texta)


    def resolve(nice):

        try:
            return int(nice)
        except ValueError:
            return nice

    peace = resolve(nice)

    if isinstance(peace, int):        
        car.drive_times = peace
        if car.drive_times <= 100 and car.drive_times >= 0:
            if car.tripsSinceMaintenance + car.drive_times <= 99:
                car.driving()  
                car.tripsSinceMaintenance = car.tripsSinceMaintenance + car.drive_times
                car.needsMaintenance = False
                print_car_specs(carOne, carTwo, carThree)
                Choose()
                
            elif car.tripsSinceMaintenance + car.drive_times > 99:
                car.stop()
                
                car.needsMaintenance = True
                
                over_haul(car)

        elif car.drive_times > 100:
            def cant_do():
                texte = colored("""\nCan't drive the car that number of times without overhauling.
                \n\nMust be positive number less than 100 turns. 'back' for Main Menu: """, 'red')

                peace = input(texte)
                car.drive_times = peace.replace("'", "")
                                            
                if isinstance(car.drive_times, int):

                    if car.drive_times >= 0 and car.drive_times <= 100:
                        if car.tripsSinceMaintenance + car.drive_times < 100:
                            car.tripsSinceMaintenance = car.tripsSinceMaintenance + car.drive_times
                            print_car_specs(carOne, carTwo, carThree)
                            Choose()
                        elif car.tripsSinceMaintenance + car.drive_times >= 100:
                            over_haul(car)
                        
                    else:
                        cant_do()

                elif isinstance(car.drive_times, str):

                    if car.drive_times == 'back':
                        Choose()

                    elif car.drive_times == 'exit':
                        save()
                        exit()

                    else:
                        print('\nTry Again')
                        drive(car)   

        cant_do()

    else:
        car.drive_times = nice
        if car.drive_times == 'back':
            Choose()
        
        elif car.drive_times == 'exit':
            save()
            exit()

        else:
            cprint('\nKindly input a number', 'yellow')
            drive(car) 

# function to save to a json file
def save():
    with open('save.json', 'w') as json_file:
          json.dump([carOne.makedict(), carTwo.makedict(), carThree.makedict()], json_file)

# Function to show car models
def Choose():

    # Displaying car attributes
    print_car_specs(carOne, carTwo, carThree)

    while True:
        textc = colored("Select a Tesla car Model or 'exit': ", 'green')
        models = input(textc)
        if models.casefold().replace(" ", "") == 'Model 3'.casefold().replace(" ", ""):
            drive(carOne)
        elif models.casefold().replace(" ", "") == 'Model S'.casefold().replace(" ", ""):
            drive(carTwo)
        elif models.casefold().replace(" ", "") == 'Model X'.casefold().replace(" ", ""):
            drive(carThree)
        elif models.casefold().replace(" ", "") == 'exit'.casefold().replace(" ", ""):
            save()
            exit()
        else:
            print('Try again!')
            continue
        return True

# Initializing the program
Choose()
