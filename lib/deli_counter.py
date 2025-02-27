def line(katz_deli):
    list_customers = []
    if katz_deli:
        for index, name in enumerate(katz_deli, 1):
            list_customers.append(f"{index}. {name}")
        print("The line is currently: " + " ".join(list_customers)) 

    else:
        print("The line is currently empty.")
        
def take_a_number(katz_deli, customer_name):
    if len(katz_deli) == 0:
        katz_deli.append(customer_name)
        print(f"Welcome, {customer_name}. You are number {len(katz_deli)} in line.")
    
    else:
        katz_deli.append(customer_name)
        print(f"Welcome, {customer_name}. You are number {len(katz_deli)} in line.")
    

def now_serving(katz_deli):
    if (len(katz_deli) == 0 ):
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {katz_deli[0]}.")
        del katz_deli[0]