# ============================================
# LESSON 07 — Object-Oriented Programming
# ============================================
# OOP in Python is similar to Java/PHP, with a few differences:
#   - Use "self" instead of "this"
#   - Constructor is __init__() instead of the class name
#   - No access modifiers (public/private) — use _ prefix by convention
#
#   Java:              Python:
#   class Dog {        class Dog:
#     String name;         def __init__(self, name):
#     Dog(String n) {          self.name = name
#       this.name = n;     def bark(self):
#     }                        print(f"{self.name} says Woof!")
#   }
# ============================================

# --- TASK 1 ---
# Create a class called Person with:
#   - __init__ that takes name and age
#   - A method called introduce() that prints: "Hi, I'm <name> and I'm <age> years old."
# Create 2 Person objects and call introduce() on each.

# YOUR CODE HERE:
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")


# Create 2 Person objects and call introduce() on each.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person1.introduce()
person2.introduce()

# --- TASK 2 ---
# Create a class called BankAccount with:
#   - __init__ that takes owner name and sets balance to 0
#   - deposit(amount) method — adds to balance
#   - withdraw(amount) method — subtracts, but print "Insufficient funds" if not enough
#   - get_balance() method — returns current balance
# Test it with a few deposits and withdrawals.


# YOUR CODE HERE:
class BankAccount:
    def __init__(self, owner) -> None:
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance


# Test the BankAccount class
account = BankAccount("Alice")
account.deposit(100)
print(f"Balance after deposit: {account.get_balance()}")  # Should print 100
account.withdraw(30)
print(f"Balance after withdrawal: {account.get_balance()}")  # Should print 70
account.withdraw(100)  # Should print "Insufficient funds"

# --- TASK 3: Inheritance ---
# Create a base class called Animal with a speak() method that prints "..."
# Create two subclasses: Dog and Cat
#   - Dog.speak() prints "Woof!"
#   - Cat.speak() prints "Meow!"
# Create objects of each and call speak().
# Hint: use super().__init__() to call the parent constructor.


# YOUR CODE HERE:
class Animal:
    def __init__(self):
        pass

    def speak(self):
        print("...")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Woof!")


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def speak(self):
        print("Meow!")


# Create objects of each and call speak().
dog = Dog()
cat = Cat()
dog.speak()  # Should print "Woof!"
cat.speak()  # Should print "Meow!"
