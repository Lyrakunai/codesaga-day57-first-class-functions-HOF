# Codesaga Day 57

#===============================================
# Mini Challenge: Smart Task Processing System
#===============================================

def smart_task_processing(rule, data):
    result = []

    for item in data:
        result.append(rule(item))

    return result


# Behavior 1: Support Ticket Classification
tickets_score = [4, 9, 2, 17, 22, 6, 110, 5, 1, 9]


def support_ticket_classifier(score):
    if score >= 8:
        return "URGENT"
    return "NORMAL"


# Behavior 2: Customer Message Formatting
customer_massages = [
    "your order has shipped",
    "your order conformed",
    "you won coupon"
]


def customer_massage_format(massages):
    return f"NOTICE: {massages}"


# Behavior 3: Inventory Status Labeling
product_stocks_count = {
    "pen": 10,
    "kids book": 7,
    "mobail": 0,
    "kids toys": 1,
    "pencil": 0
}


def inventory_status_labeler(product):
    name, stocks = product

    if stocks <= 0:
        return f"{name}: OUT OF STOCKS"

    return f"{name}: AVAILABLE"


# Calling the processing system after defining all behaviors
label_status = smart_task_processing(
    inventory_status_labeler,
    product_stocks_count.items()
)
print(label_status)

messages = smart_task_processing(
    customer_massage_format,
    customer_massages
)
print(messages)

classifier = smart_task_processing(
    support_ticket_classifier,
    tickets_score
)
print(classifier)
