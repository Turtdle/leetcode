import random
print("hello world")
print("I meant this")

class Dog():
    def __init__(self, breed : str):
        self.breed = breed
        self.weight = random.randrange(10,50)
    def __str__(self):
        return(f'Dog of breed {self.breed} and weight {self.weight}')
        
if __name__ == "__main__":
    dog1 = Dog("cool breed")
    dog2 = Dog("cooler breed")
    print(f'dog1 breed: {dog1.breed}')
    print(f'dog1 weight: {dog1.weight}')
    print(f'dog2 weight: {dog2.weight}')
    print(f'dog2 breed: {dog2.breed}')
    print(dog1)
    print(dog2)
