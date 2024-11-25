class Jar:
    def __init__(self, capacity=12):
        if capacity<0:
            raise ValueError("Capacity cant be negative")
        self.capacity=capacity
        self.cookies=0

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n):
        if (self.cookies+n)>self.capacity:
            raise ValueError("Too much cookies")
        if n<0:
            raise ValueError("You can't give negative values")
        self.cookies=self.cookies+n

    def withdraw(self, n):
        if (self.cookies-n)<0:
            raise ValueError("Not enought cookies")
        if n<0:
            raise ValueError("You can't take negative values")
        self.cookies=self.cookies-n

