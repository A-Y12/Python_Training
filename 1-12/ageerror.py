class InvalidAgeError(Exception):
    pass


age = int(input("Enter your age: "))
if age<18:
    raise InvalidAgeError("Your age is too young")

