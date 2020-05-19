from abc import ABC, abstractmethod
class living_things(ABC):
    @abstractmethod
    def set_voice(self, voice):
        pass
    @abstractmethod
    def get_voice(self):
        return None

class animals(ABC):#animals is base class
    def __init__(self, num=50):
        self.num = num
    def eats(self): #method overriding is implemented ('eats' method is there in derived class of animals) 
        print("animals eat")
    def get_num(self, number):
        self.num = number
    def __add__(self, p): #Operator Overloading for polymorphism
        return self.num+p.num
    def __gt__(self, p):
        if(self.num > p.num):
            return True
        else :
            return False
    def __lt__(self, p):
        if(self.num > p.num):
            return False
        else :
            return True
    def __sub__(self, p):
        return (self.num-p.num)
        
class herb(animals): #derived class from animal
    def __init__(self, num=50):
        self.num = num
    def intestine(self, size=None): #method overloading implemented.
        if(size == None):
            print("large size intestine")
        else:
            print("size of intestine is", size)
    def eats(self):
        print("eat plants")
    def number(self):
        return self.num
    def get_num(self, number):
        self.num = number
    def __add__(self, p): #Operator Overloading for polymorphism
        return self.num+p.num
    
        
class carni(animals): #derived class from animal
    def __init__(self, num=50):
        self.num = num
    def intestine(self, size=None): #method overloading implemented.
        if(size == None):
            print("small size intestine")
        else:
            print("size of intestine is", size)
    def eats(self):
        print("eat animals")
    def number(self):
        return self.num
    def get_num(self, number):
        self.num = number
    def __add__(self, p):
        return self.num+p.num
    
class equus(herb): #class derived from herb 
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        herb().eats()
        print("eats channa")
        
class horse(equus):#class derived from equus
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        equus().eats()
    def feature(self):
        print("Horse are muscular")

class zebra(equus):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        equus().eats()
    def feature(self):
        print("Have stripes")

class donkey(equus):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        equus().eats()
    def feature(self):
        print("Used for carrying load")

class panthera(carni):#class derived from carni
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        carni().eats()
        print("Eats deers")

class lion(panthera): #class derived from panthera
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        panthera().eats()
    def feature(self):
        print("King of Jungle")

class leopard(panthera):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number    
    def eats(self):
        panthera().eats()
    def feature(self):
        print("Run Fast")

class cat(panthera, herb):
    def __init__(self, num=50):
        self.num = num
    def get_num(self, number):
        self.num = number
    def eats(self):
        panthera().eats()
        herb().eats()
    def feature(self):
        print("Domastic animal")
    


a = animals()
b = animals()
e = herb()
d = carni()
d.intestine(154)
b.get_num(100)
a.eats()
c = e+d
e.get_num(120)
if(e>d):
    print("TRUE")
else:
    print("FALSE")
print(c)
print()

z = cat()
z.get_num(122)
print(z+a)