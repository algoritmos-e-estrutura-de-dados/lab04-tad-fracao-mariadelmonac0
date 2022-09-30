import math

class Fracao:     
    numerador = 1
    denominador = 1 
   
    def __init__(self, numerador, denomionador): 
        self.numerador = numerador
        self.denominador = denomionador
        


    def add(self, fracao):  
        num = (self.numerador * fracao.denominador) + (fracao.numerador * self.denominador) 
        den = self.denominador * fracao.denominador
        return Fracao(num, den) 

    def sub(self, fracao):
        num = (self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def mult(self, fracao):
        num = self.numerador * fracao.numerador
        den = self.denominador * fracao.denominador
        return Fracao(num, den)

    def simplify(self):
        commom_divisor =  math.gcd(self.numerador, self.denominador)
        numerador = self.numerador/ commom_divisor
        denominador = self.denominador/ commom_divisor
        return Fracao(numerador, denominador)
    
    def solve(self):
        return self.numerador/self.denominador


    def __str__(self): 
        return f"{int(self.numerador)}/{int(self.denominador)}"

    

fracao1 =  Fracao(15, 30) 
fracao2 =  Fracao(5, 30) 
fracao3 = fracao1.add(fracao2) 
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mult(fracao2)


print(f"fracao1: {fracao1.simplify()}")
print(f"fracao2: {fracao2.simplify()}")
print(f"fracao2: {fracao3}")
print(f"fracao2: {fracao4}")
print(f"fracao2: {fracao5}")




