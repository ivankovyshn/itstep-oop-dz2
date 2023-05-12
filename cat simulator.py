import random


class Dog:
    def __init__(self, name):
        self.name = name
        self.interesting = 50
        self.hungry_level = 0
        self.active = True

    def to_walk(self):
        print('Time for walk')
        self.hungry_level += 0.12
        self.interesting -= 5

    def to_sleep(self):
        print('ZZZZZZ!')
        self.interesting += 3
        self.hungry_level += 0.05

    def to_play(self):
        print('Chill time!')
        self.interesting += 5
        self.hungry_level -= 0.1

    def is_active(self):
        if self.hungry_level < -0.5:
            print('You have to eat!')
            self.active = False
        elif self.interesting <= 0:
            print('So boring')
            self.active = False
        elif self.hungry_level > 5:
            print('Sorry my friend...')
            self.active = False

    def status(self):
        print(f'Interesting: {self.interesting}')
        print(f'Hungry_level: {round(self.hungry_level, 2)}')

    def live_a_day(self, day):
        day_str = f'Day {day} of {self.name} life'
        print(f"{day_str:=^50}")
        d5 = random.randint(1, 5)
        if d5 < 3:
            self.to_walk()
        elif d5 < 5:
            self.to_sleep()
        elif d5 == 5:
            self.to_play()
        self.status()
        self.is_active()


Pes_Patron = Dog(name='Pes_Patron')
for day in range(365):
    if Pes_Patron.active:
        Pes_Patron.live_a_day(day)
    else:
        break
