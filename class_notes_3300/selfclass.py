class Cat:
    
    def __init__(self, m=10, h=10, e=10):
        self.mood = m
        self.hunger = h
        self.energy = e

    def meow(self):
        self.print('Meow!')

    def feed(self):
        self.mood = min(10, self.mood + 1)
        self.hunger = max(1, self.hunger - 1)

    def sleep(self):
        self.energy = min(10, self.energy + 1)
        self.hunger = min(10, self.hunger + 1)

    def play(self):
        self.mood = min(10, self.mood + 1)
        self.hunger = min(10, self.hunger + 1)
        self.energy = max(1, self.energy - 1)

    def time_pass(self):
        self.mood = max(1, self.mood - 1)
        self.hunger = min(10, self.hunger + 1)
