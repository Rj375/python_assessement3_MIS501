import re
from datetime import datetime
import sys
attempts = 0
order_id_generate = 0
class Impliment: #it is a new class for initialization.
    def __init__(self): # it is a initial funtion.
        self.first_choice = 0
        self.selection = 0
        self.order_type_option = 0
        self.mode_of_delivery = 0
        self.printing_the_static_choice = 0
        self.current_user = 0
        self.total = 0
        self.user_accounts_list = []
        self.dine_in_orders_list = []
        self.pick_up_orders_list = []
        self.delivery_orders_list = []
    def instruction_to_program_startup(self): #it helps in program to startup.
        try: 
            self.first_choice = int(input("Please select one to proceed \n"
                                          "1. Sign Up \n"
                                          "2. Sign In \n"
                                          "3. Exit \n"))
        except ValueError:
            print("please input correct input")
    def instruction_to_order_statics(self): #it helps in order statistics.
        try:
            self.selection = int(input('1 Ordering (Dine in, Click and collect, Delivery)\n'
                                       '2 Summary of Transactions\n'
                                       '3 Reset Password \n'
                                       '4  Logout\n'))
        except ValueError:
            print("Please enter the correct numerical input")
    def instruction_to_order_types(self): #it helps in order types.
        try:
            self.order_type_option = int(input('Please enter 1 for dine in\n'
                                               'Please enter 2 to order online\n'
                                               'Please enter 3 exit \n'))
        except ValueError:    
            print("Please enter the correct numerical format")
    def instruction_to_delivery(self): #it helps in delivery.
        try:
            self.mode_of_delivery = int(input("Enter 1 for Self Pickup \n"
                                              "Enter 2 for Home Delivery \n"
                                              "Enter 3 to go to previous \n"))
        except ValueError:
            print("Please enter the correct numerical format")
    def instruction_to_printing_the_static(self): #it helps in printing the statics.
        try:
            self.printing_the_static_choice = int(input("Please enter the option to Print the Statistics \n"
                                              "1. All Dines in Orders \n"
                                              "2. All Pick up Orders \n"
                                              "3. All Deliveries \n"
                                              "4. All Orders (Ascending Order \n"
                                              "5. Total Amount Spent on All Orders \n"
                                              "6. To go to Previous Menu"))
        except ValueError:
            print("Please enter the correct numerical format")

    def start_the_program(self): #it starts the program.
        while True:
            self.instruction_to_sign_up()

    def instruction_to_sign_up(self): #it helps in customer signup.
        self.instruction_to_program_startup()
        customer = Customer()
        if self.first_choice == 1:
            customer.sign_up(self.user_accounts_list) #it helps in sign_up.
        elif self.first_choice == 2:
            self.current_user = customer.sign_in(self.user_accounts_list) #it helps in sign_in.
            if self.current_user == -1: #it takes  user back if number is not in any user.
                return
            else:
                self.selecting_menu()
        elif self.first_choice == 3:
            sys.exit()
        else:
            print("Wrong input")                

    def selecting_menu(self): #it helps in selecting the menu for ordering.
        while True:
            self.instruction_to_order_statics()
            if self.selection == 1:
                self.implimenting_the_order() #it implements orders.
            elif self.selection == 2:
                self.printing_the_static() #it implements printing_the_static.
            elif self.selection == 3:
                self.current_user.reseting_the_password() #it implements reseting_the_password.
            elif self.selection == 4:
                self.instruction_to_sign_up() #it implements instruction_to_sign_up.
            else:
                print("Please enter the correct input defined in instruction")

    def implimenting_the_order(self): #it helps in implementing orders.
        while True:
            self.instruction_to_order_types()
            if self.order_type_option == 1:
                dine_in = DiningIn(owner=self.current_user.get_mobile_number()) #it helps in implementing DiningIn.
                dine_in.processing_drinks()
                dine_in.saving_the_order(self.dine_in_orders_list)
            elif self.order_type_option == 2:
                self.implementing_the_online_order() #it helps in implementing the_online_order.
            elif self.order_type_option == 3: 
                break #it will break if option is equals to 3.
            else:
                print("Please enter the correct input defined in instruction")

    def implementing_the_online_order(self): #it helps to impliment online orders.
        while True:
            self.instruction_to_delivery()
            if self.mode_of_delivery == 1:
                pick_up = PickingUpTheOrder(owner=self.current_user.get_mobile_number()) #it helps to impliment PickingUpTheOrder.
                pick_up.processing_the_order()
                pick_up.calculating_the_total_amount()
                pick_up.saving_the_order(self.pick_up_orders_list)
            elif self.mode_of_delivery == 2:
                delivery_order = Delivery(owner=self.current_user.get_mobile_number()) #it helps to impliment Delivery.
                delivery_order.processing_the_order() #it helps to impliment the processing_the_order.
                if not delivery_order.checking_the_address(self.current_user): #it helps to impliment the checking_the_address.
                    return
                delivery_order.calculating_the_total_amount() #it helps to impliment calculating_the_total_amount.
                delivery_order.saving_the_order(self.delivery_orders_list) #it helps to impliment the saving_the_order.
            elif self.mode_of_delivery == 3:
                break
            else:
                print("Please enter the correct input define on the instructions")

    def printing_the_static(self): #it helps to print the static and manage the summary.
        all_orders_list = self.pick_up_orders_list + self.dine_in_orders_list + self.delivery_orders_list

        def printing_the_item(order_list): #it helps to print the items that are required.
            print("||   Order_ID   ||   Date  ||   Total_Amount   ||    Order_Type   ||")
            for order in order_list:
                print(f"||  S00{order.order_id}   "
                      f"||  {order.order_date}   "
                      f"||  {order.total_amount}  "
                      f"||  {order.order_type}")
                
        def sorting_the_item(order_list): #it helps to sort the order list in ascending order.
            sorted_order = sorted(order_list, key=lambda x: x.order_id)
            return sorted_order
        
        def calculate_the_total_amount_spent(all_order_list): #it helps to calculates total sum that are ordered.
            for order in all_order_list:
                self.total += order.total_amount
            print(f"The total amount that user spend on the order is {self.total}")

        
        def filtering_the_order(self, order_list): #it helps in orders by using the phone number.
            new_order_list = []
            for order in order_list:
                if order.owner == self.current_user.get_mobile_number():
                    new_order_list.append(order)
            return new_order_list
        
        while True:
            self.instruction_to_printing_the_static()
            #it prints the static according to the item chose.
            if self.printing_the_static_choice == 1:
                printing_the_item(filtering_the_order(self, self.dine_in_orders_list))
            elif self.printing_the_static_choice == 2:
                printing_the_item(filtering_the_order(self, self.pick_up_orders_list))
            elif self.printing_the_static_choice == 3:
                printing_the_item(filtering_the_order(self, self.delivery_orders_list))
            elif self.printing_the_static_choice == 4:
                sorting_the_item(all_orders_list)
                printing_the_item(filtering_the_order(self, all_orders_list))
            elif self.printing_the_static_choice == 5:
                calculate_the_total_amount_spent(filtering_the_order(self, all_orders_list))
            elif self.printing_the_static_choice == 6:
                break
            else:
                print("Please enter the correct input according to the instructions ")
    
class Customer: #it is a new class called Customer.
    #it all requires for sign_up process.
    def __init__(self, name='', mobile_number='', date_oF_birth='', confirm_password='', address='', password=''):
        self.__name = name
        self.__mobile_number = mobile_number
        self.__date_oF_birth = date_oF_birth
        self.__address = address
        self.__password = password
        self.__confirm_password = confirm_password
        
        self.attempts = 0 #it checks attempts.

     #encapsulation is used here.
    def get_name(self): #gets name.
        return self.__name
    def set_name(self, x): #sets name.
        self.__name = x
    def get_mobile_number(self): #gets mobile number.
        return self.__mobile_number
    def set_mobile_number(self, x): #sets mobile number.
        self.__mobile_number = x
    def get_date_oF_birth(self): #gets date oF birth.
        return self.__date_oF_birth
    def set_date_oF_birth(self, x): #sets date oF birth.
        self.__date_oF_birth = x
    def get_address(self): #gets address.
        return self.__address
    def set_address(self, x): #sets address.
        self.__address = x
    def get_password(self): #gets password.
        return self.__password
    def set_password(self, x): #sets password.
        self.__password = x
    def set_confirm_password(self, x): #gets confirm password.
        self.__confirm_password = x
    def get_confirm_password(self): #sets confirm password.
        return self.__confirm_password
    
    def sign_up(self, user_accounts): #it helps in user sign up.
        self.sign_up_inputs() #it helps to impliment sign_up_inputs.
        self.validating_the_user_attribute() #it helps to impliment validating_the_user_attribute.
        if self.check_user(self.get_mobile_number(), user_accounts) is None:
            if self.validating_the_age():
                user_accounts.append(self)
                print("Your account is successfully created! Please sign_in now")
            else:
                print("user already exists please ue different number")
                return
            
    def default_input_for_testing(self): #the inputs in this are used as default inputs as testing.
        self.set_name("Random")
        self.set_mobile_number("011111111")
        self.set_date_oF_birth("25/07/1996")
        self.set_password("random@123")
        self.set_confirm_password("random@123")

    def sign_up_inputs(self): #it gets information from inputs and append them in list.
        self.set_name(input("Please enter your full name as shown : 'Kanchan Ghimire' ").lower())
        self.set_address(input("Please enter your address , press enter to skip"))
        self.set_mobile_number(input("Please enter your contact number starting with 0  :"))
        self.set_date_oF_birth(input("Please enter your date of birth in 'DD/MM/YYYY' format  : "))
        self.set_password(input("Please enter you password \n "
                            "Must contains alphabets, characters @ and & , also  ending with numbers 'kanchan@123' : "))
        self.set_confirm_password(input("Please confirm your password  :"))

    def validating_the_user_attribute(self): #it helps in validating the user attribute.
        self.checking_the_null_value() #it helps to impliment the checking_the_null_value.
        validation_methods = (self.validating_the_contact, self.validating_the_date, self.validating_the_password)
        setter_methods = (self.set_mobile_number, self.set_date_oF_birth, self.set_password)
        for n in range(len(validation_methods)):
            while not validation_methods[n]():
                user_input = input(f"Please enter the correct {validation_methods[n].__name__}")
                setter_methods[n](user_input)
        self.confirm_password() #it helps to impliment confirm_password.

    def confirm_password(self): #it helps to make confirm password.
        while self.get_password() != self.get_confirm_password():
            self.set_confirm_password(input("You confirmation password doesn't matched with previous one !! Please enter again"))
            
    def checking_the_null_value(self): #it takes object as input and checks if is null or not.
        try:
            for attribute, value in vars(self).items():
                self.attempts = 0
                while value == '':
                    if self.checking_the_attempts():
                        raise StopIteration
                    if attribute[11:] == 'address':
                        break
                    else:
                        value = input(f"Please enter your {attribute[11:]} "
                                  f"This field is required for sign Up process")
                        setattr(self, attribute, value)
                        self.attempts += 1
        except StopIteration:
            self.sign_up_inputs()

    def validating_the_contact(self): #it helps to validate the contact by using regEx.
        is_valid = re.match('^0[0-9]{9}$', self.get_mobile_number())
        return is_valid
    
    def validating_the_date(self): #it helps to validate date of birth by using regEx.
        valid_dob = False
        try:
            formatted_dob = datetime.strptime(self.get_date_oF_birth(), '%d/%m/%Y').date()
            self.set_date_oF_birth(formatted_dob)
            valid_dob = True
        except ValueError:
            valid_dob = False

        return valid_dob
    
    def validating_the_age(self): #it helps to validate age of customer by using datetime.
        this_year = datetime.now().year
        if this_year - self.get_date_oF_birth().year <= 21:
            print("Your age is less tha 21, You are not eligible for sign_up !!")
            return False
        return True
    
    def validating_the_password(self, new_pass=""): #it helps to validate the password using regEx.
        if new_pass == "":
            check_password_length = re.match('^[A-Za-z]+[&@]+[0-9]{2,10}$', self.get_password())
        else:
            check_password_length = re.match('^[A-Za-z]+[&@]+[0-9]{2,10}$', new_pass)
        return check_password_length
    
    def check_user(self, user_mobile_number, user_accounts): #it returns user if any attribute is matched.
        for user in user_accounts:
            if user_mobile_number == user.get_mobile_number():
                return user

    def checking_the_attempts(self): #it helps to check the attempts.
        if self.attempts > 2:
            print("You have used you all 3 attempts, please try again")
            return True
        return False
    
    def sign_in(self, user_accounts): #it helps user to sign in by mobile number and password.
        user_mobile_number = input("Please enter your mobile_no as username")
        user = self.check_user(user_mobile_number, user_accounts)
        self.attempts = 0
        while user is not None:
            if self.checking_the_attempts(): #it helps to impliment checking_the_attempts.
                self.reseting_the_password(recover=True) #it helps to impliment reseting_the_password.
            user_password = input("Please enter your password for sign in ") # it is for second password.
            if user.get_password() == user_password:
                print(f"Hello {user.get_name()} You are successfully logged in using {user_mobile_number} ")
                return user
            else:
                print("credentials doesn't match please try again")
                self.attempts += 1
        else:
            print(f"You have not Signed Up with this number {user_mobile_number}, Please sign in first")
            return -1
        
    def reseting_the_password(self, recover=False): #it helps in reseting the password.
        new_mobile_number = input("Please enter your username (Mobile Number) : ")
        new_password = input("Please enter your new password : ")
        if new_mobile_number == self.get_mobile_number():
            if recover:
             self.checking_the_date_oF_birth() #it helps to impliment checking_the_date_oF_birth.
            if self.new_password_checking(new_password):
                self.set_password(new_password) #it helps to impliment new_password_checking.
                print("Password successfully changed")
            else: 
                return
        else:
            print("User doesn't exist on the database")
            return
        
    def new_password_checking(self, new_pas): #it helps in validating the new password.
        if new_pas != self.get_password():
            while not self.validating_the_password(new_pas):
                new_pas = input("Wrong password format Please enter your new password again")
            self.set_password(new_pas)
            return True
        else:
            print("You cannot use the same password as before!!")
            return False

    def checking_the_date_oF_birth(self): #it checks for date_of_birth if recovery mode is on.
        date_oF_birth = input("Please enter your date of birth ")
        if self.get_date_oF_birth() != date_oF_birth:
            return 
        else:
            return True    
        

class PickingUpTheOrder: #it is a new class called PickingUpTheOrder.
    def __init__(self, order_id="", order_type="Self_Pick_Up", order_date='', order_time='', owner=''):
        self.order_id = order_id
        self.order_type = order_type
        self.order_date = order_date
        self.order_time = order_time
        self.owner = owner
#these are the class items.
        self.total_amount = 0
        self.__food_menu_choice = 0
        self.mode_of_delivery = ""
        self.total_order_items = [] #it saves ordered items.
        self.name_of_person = ''
#these are the menu items.
        self.item_1 = "Noodles"
        self.item_price_1 = 2
        self.item_2 = "Sandwich"
        self.item_price_2 = 4
        self.item_3 = "Dumplings"
        self.item_price_3 = 6
        self.item_4 = "Muffins"
        self.item_price_4 = 8
        self.item_5 = "Pasta"
        self.item_price_5 = 10
        self.item_6 = "Pizza"
        self.item_price_6 = 20

    def get_the_food_menu_choice(self): #it helps in getting the food menu choice.
        return self.__food_menu_choice
    
    def food_menu(self): #it helps in taking the selected user's inputs as shown in the items.
        try:
            def print_menu(): 
                print("--------------------⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽------------------------|\n"
                      "-------------------| Food Menu |-----------------------|\n"
                        "--------------------⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺------------------------|") 
                for val in range(1, 8):
                    if val == 7:
                        print("Enter 7 for checkout")
                    else:
                        item, price = self.build_variable("item", val)
                        print(f"Enter {val} for {item} ------> Price AUD {price}")
            self.__food_menu_choice = int(input(print_menu()))
        except ValueError:
            print("Please read the instructions and enter a correct value")
            self.food_menu()

    def instruction_to_delivery(self): #it helps to guide for delivery.
        self.mode_of_delivery = int(input("Enter 1 for Self Pickup \n"
                                          "Enter 2 for Home Delivery \n"
                                          "Enter 3 to go to previous \n"))
        
    def processing_the_order(self): #it helps in processing the order and print the details.
        while self.get_the_food_menu_choice() != 7:
            self.food_menu() #it helps to impliment food_menu.
            if 0 < self.get_the_food_menu_choice() <= 6:
                item, price = self.build_variable("item", self.get_the_food_menu_choice())
                self.total_order_items.append(item)
                self.total_amount += price
            elif self.get_the_food_menu_choice() > 7:
                print("Wrong input please select again !!")

    def build_variable(self, item, item_number): #it helps to build the variable from the string for the calculation.
        built_item = eval(f"self.{item}_{item_number}")
        built_item_price = eval(f"self.{item}_price_{item_number}")
        return built_item, built_item_price
    
    def get_input(self): #it helps to get all the required details regarding order.
        self.name_of_person = input("Please enter the name of person picking up :")
        self.get_order_date_and_time() #it helps to impliment get_order_date_and_time.

    def get_order_date_and_time(self): #it helps to get order date and order time.
        self.order_time = input("Please input valid order time :")
        self.order_date = input("Please enter valid order date :")

    def calculating_the_total_amount(self): #it helps to calculate the total amount.
        self.get_input() #it helps to impliment get_input.
        print(f"Your total amount for the order is {self.total_amount}")

    def generating_the_order_id(self): #it helps to generate order id for each order.
        global order_id_generate
        order_id_generate += 1
        self.order_id = int(f"00{order_id_generate}")

    def saving_the_order(self, orders): #it helps to save the order on the required list.
        self.generating_the_order_id() #it helps to impliment generating_the_order_id.
        orders.append(self)


class DiningIn(PickingUpTheOrder, Customer): #it is a new class called DiningIn.
    def __init__(self, order_id='', order_type="Dine_In", order_date='', order_time='', owner=''):
        super().__init__(order_id, order_type, order_date, order_time)
        self.__drinks_menu_choice = 0
        self.owner = owner
        #these all are the menu_items.
        self._drink_1 = "Coffee"
        self._drink_price_1 = 2
        self._drink_2 = "Cold_Drink"
        self._drink_price_2 = 4
        self._drink_3 = "Shake"
        self._drink_price_3 = 6

        self.__service_charge_rate = 15 / 100 #it is a service charge.

        
        self.__number_of_person = 0 #it is user requirements detail.

    def drinks_menu(self): #it helps in taking the user choice of the drink for processing.
        try:
            self.__drinks_menu_choice = int( input(f"--------------------⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽⎽------------------------|\n"
                                                   f"-------------------| Drinks Menu |-----------------------|\n" 
                                                   f"--------------------⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺⎺------------------------|\n"
                                                   f"Enter 1 for {self._drink_1} ------> Price AUD {self._drink_price_1} \n" 
                                                   f"Enter 2 for {self._drink_2} ------> Price AUD {self._drink_price_2} \n" 
                                                   f"Enter 3 for {self._drink_3} ------> Price AUD {self._drink_price_3} \n" 
                                                   f"Enter 4 for Checkout"))
        except ValueError:
            print("Please enter the correct value ")
            self.drinks_menu() #it helps to impliment drinks menu.

    def processing_drinks(self): #it helps to calculate total amount and builds the list of the drink item selected.
        self.processing_the_order() #it helps to impliment processing_the_order.
        while self.__drinks_menu_choice != 4:
            self.drinks_menu() #it helps to impliment drinks_menu.
            if 0 < self.__drinks_menu_choice < 4:
                drink_name, drink_price = self.build_variable("_drink", self.__drinks_menu_choice)
                self.total_order_items.append(drink_name)
                self.total_amount += drink_price
            elif 4 < self.__drinks_menu_choice < 0:
                print("Please enter a valid input from the instruction")
        else:
            self.calculating_the_total_amount()

    def get_input(self): #it helps to get all the inputs required to finalize the order.
        self.get_order_date_and_time() #it helps to impliment get_order_date_and_time.
        self.name_of_person = int(input("Please enter the number of person you like to visit"))

    def calculating_the_total_amount(self): #it helps in calculating the total amount.
        self.get_input() #it helps to implimentget_input.
        service_charge = round((self.total_amount * self.__service_charge_rate), 2)
        self.total_amount += service_charge
        print(f"Your total payable amount is: AUD {self.total_amount} including AUD {service_charge}for service charges ")

    
class Delivery(PickingUpTheOrder): #it is a new class called Delivery.
    def __init__(self, order_id='', order_type='Delivery', order_date='', order_time='', owner =''):
        super().__init__(order_id, order_type, order_date, order_time)
        self.delivery_charges = 0
        self.distance_from_restaurant = ''
        self.user_choice = ""
        self.owner = owner

    def checking_the_address(self, user): #it helps to check whether the user address is empty or not.
        while user.get_address() == "":
            self.user_choice = input("You have not mentioned your address, while signing up \n"
                                     "Please enter 'Y' if you like to enter your password \n"
                                     "Enter 'N' if you like to select other mode of password ").lower()
            if self.user_choice == "n":
                return False
            elif self.user_choice == "y":
                user.set_address(input("Enter Your address ! \n"))
                return True
            else:
                print("Wrong input please try again ")

    def get_input(self): #it helps to get required details for the delivery order.
        self.get_order_date_and_time() #it helps to impliment get_order_date_and_time.
        self.distance_from_restaurant = eval(input("Please enter the distance from the restaurant in kms"))

    def calculating_the_delivery_charge(self): #it helps to calculate delivery charge according to the distance.
        if self.distance_from_restaurant > 10:
            self.delivery_charges = 18
        elif self.distance_from_restaurant > 5:
            self.delivery_charges = 10
        elif self.distance_from_restaurant > 0:
            self.delivery_charges = 5
        else:
            print("please enter pick up details we cannot deliver")

    def calculating_the_total_amount(self): #it helps to calculate the total amount for the order.
        self.get_input() #it helps to impliment get_input.
        self.calculating_the_delivery_charge() #it helps to impliment calculating_the_delivery_charge.
        self.total_amount += self.delivery_charges
        print(f"Your total payable amount is: AUD {self.total_amount} "
              f"with the additional AUD {self.delivery_charges} charges for deliver")
        

if __name__ == '__main__':
    implement = Impliment()
    implement.start_the_program()

