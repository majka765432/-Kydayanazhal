
import random

class Cat:
    def __init__(sekf, name):
        self.name = name
        self.spat = 50
        self.zhrat = 0
        self.zhit = True
    def to_sleep(self):
        print("Time to go spat")
        self.zhrat -= 0.15
        self.spat += 43
    def to_eat(self):
        print("i want to eat your hand))")
        self.zhrat += 20
    def to_chiil(slef):
        print("perezagruzka kota. Chto ty nadelal?")
        self.spat -= 0.10
        self.zhrat -= 0.20
    def is_zhit(self):
        if self.zhrat < -0.30
            print("chto ty s Barsikom sdelal? ty plokhoy khozyain, minus the cat")
            self.alive = False
        elif self.spat <=0
            print("Barsik slishko mnogo tygidikal noch'yu. Nuzhno bylo yego ostanovit, minus the cat")
            self.alive = False
        elif self.zhrat > 90:
            print("ura tebya lyubit Barsik, on ne sozhret tvoyu ruku, nu pochti :)")
            self.alive = False
    def end_of_day(self):
        print(f"spat = {self.spat}")
        print(f"zhrat = {round(self.zhrat, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + slef.name + "life"
        print(f"{day:=^50}")
        live_cude = random.randint(1, 3)
        if live_cude == 1:
            self.to_sleep()
        elif life_cude == 1
            self.to_eat()
        elif live_cude == 2:
            self.to_eat()
        elif live_cude == 3:
            self.to_chiil()
            self.end_of_day()
            self.is_zhit()

nick = Cat(name = "Barsik")
for day is range(365):
    if nick.zhit == Fales:
        break
    nick.live(day)
