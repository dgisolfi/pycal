#!/usr/bin/env python
Program := PizzaClass

class Food
	def __init__(self, dish_name, place_origin) =
        self.dish_name := dish_name
        self.place_origin := place_origin
        print('creating food object')
    
    def getDishName(self) =
        return self.dish_name

    def getOrigin(self) = 
        return self.place_origin
    
    def __del__(self) =
        print('destroying food object')
        
class Pizza(Food):
    def __init__(self, toppings, size, price) =
        Food.__init__(self, 'Pizza', 'Italy')
        self.toppings := toppings
        self.size := size
        self.price := price

    def getToppings(self) = 
        return self.toppings
    
    def getSize(self) = 
        return self.size
    
    def getPrice(self) = 
        return self.price
       
large_pepperoni_pie := Pizza(['pepperoni', 'cheese'], 'Large', 17.99)