class animals:
    def eats(self):
        pass

class herb(animals):
    def intestine(self):
        print("large size intestine")
    def eats(self):
        print("eat plants")
    def teeth(self):
        print("cananes are less developed")
    def number(self):
        print("more in number")
        
class carni(animals):
    def intestine(self):
        print("small size intestine")
    def eats(self):
        print("eat animals")
    def teeth(self):
        print("cananes are more developed")
    def number(self):
        print("small in number")
        
class equus(herb):
    def eats(self):
        herb().eats()
        print("eats channa")
        
class horse(equus):
    def eats(self):
        equus().eats()
    def feature(self):
        print("Horse are muscular")

class zebra(equus):
    def eats(self):
        equus().eats()
    def feature(self):
        print("Have stripes")

class donkey(equus):
    def eats(self):
        equus().eats()
    def feature(self):
        print("Used for carrying load")

class oxen(herb):
    def eats(self):
        herb().eats()
        print("Eats leaves and grass")
        
class cow(oxen):
    def eats(self):
        oxen().eats()
    def feature(self):
        print("Gives milk with 4-5% at")

class buffolo(oxen):
    def eats(self):
        oxen().eats()
    def feature(self):
        print("Gives milk with 10% fats")

class bull(oxen):
    def eats(self):
        oxen().eats()
    def feature(self):
        print("are Hardworking")
        
class panthera(carni):
    def eats(self):
        carni().eats()
        print("Eats deers")

class lion(panthera):
    def eats(self):
        panthera().eats()
    def feature(self):
        print("King of Jungle")

class leopard(panthera):
    def eats(self):
        panthera().eats()
    def feature(self):
        print("Run Fast")

class cat(panthera, herb):
    def eats(self):
        panthera().eats()
        herb().eats()
    def feature(self):
        print("Domastic animal")
        
class canis(carni):
    def eats(self):
        carni().eats()
        print("leftovers of animals")

class dog(canis):
    def eats(self):
        canis().eats()
    def feature(self):
        print("are faithful")

class wolf(canis):
    def eats(self):
        canis().eats()
    def feature(self):
        print("are Cunning")

D = dog()
D.eats()
print()
C = cat()
C.eats()