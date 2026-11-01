## Codesaga Day 57
## First-Class Functions & Higher-Order Functions


#-------------------------------
# 1. Flexible Number Processing
#-------------------------------
def processing(operation, number):
    return operation(number)


def double(number):
    return 2 * number


def square(number):
    return number * number


def negative(number):
    return -number


print(processing(double, 8))
print(processing(square, 9))
print(processing(negative, 9333))

#-----------------------------
# 2. Notification System
#-----------------------------
def notification_system(notification_behavior):
    return notification_behavior()


def normal():
    print("hello this is me. nice to meet you!!")


def urgent():
    print("This is an urgent notification!")


notification_system(normal)
notification_system(urgent)


#-----------------------------
# 3. Custom Data Filter
#-----------------------------
def data_filter(rule, numbers):
    result = []

    for num in numbers:
        if rule(num):
            result.append(num)

    return result


def even(number):
    return number % 2 == 0


def positive(number):
    return number > 0


numbers = [1, -2, 3, 4, -5, 6]

print(data_filter(even, numbers))
print(data_filter(positive, numbers))


#-----------------------------
# 4. Function Factory
#-----------------------------
def choose_time(hour):

    def greeting():
        if hour < 12:
            return "Good morning"
        return "Good evening"

    return greeting


morning = choose_time(9)
evening = choose_time(18)

print(morning())
print(evening())


#-----------------------------
# 5. Operation Registry
#-----------------------------
def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def invalid_operation(a, b):
    return "Invalid operation"


operations = {
    "add": add,
    "multiply": multiply
}

choice = "add"
operation = operations.get(choice, invalid_operation)

print(operation(5, 3))