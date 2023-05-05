import re
from datetime import datetime
import sys
attempts = 0
order_id_generate = 0
class Implementation:
    def __init__(self):
        self.first_choice = 0
        self.selection = 0
        self.order_type_option = 0
        self.mode_of_delivery = 0
        self.print_statics_choice = 0
        self.current_user = 0
        self.total = 0
        self.user_accounts_list = []
        self.dine_in_orders_list = []
        self.pick_up_orders_list = []
        self.delivery_orders_list = []
    def program_startup_instructions(self):
        try:
            self.first_choice = int(input("Please select one to proceed \n"
                                          "1. Sign Up \n"
                                          "2. Sign In \n"
                                          "3. Exit \n"))
        except ValueError:
            print("please input correct input")
    def instructions_for_order_statics(self):
        try:
            self.selection = int(input('1 Ordering (Dine in, Click and collect, Delivery)\n'
                                       '2 Summary of Transactions\n'
                                       '3 Reset Password \n'
                                       '4  Logout\n'))
        except ValueError:
            print("Please enter the correct numerical input")
    def order_types_instruction(self):
        try:
            self.order_type_option = int(input('Please enter 1 for dine in\n'
                                               'Please enter 2 to order online\n'
                                               'Please enter 3 exit \n'))
        except ValueError:    
            print("Please enter the correct numerical format")
    def delivery_instructions(self):
        try:
            self.mode_of_delivery = int(input("Enter 1 for Self Pickup \n"
                                              "Enter 2 for Home Delivery \n"
                                              "Enter 3 to go to previous \n"))
        except ValueError:
            print("Please enter the correct numerical format")
    def instruction_print_statics(self):
        try:
            self.print_statics_choice = int(input("Please enter the option to Print the Statistics \n"
                                              "1. All Dines in Orders \n"
                                              "2. All Pick up Orders \n"
                                              "3. All Deliveries \n"
                                              "4. All Orders (Ascending Order \n"
                                              "5. Total Amount Spent on All Orders \n"
                                              "6. To go to Previous Menu"))
        except ValueError:
            print("Please enter the correct numerical format")

    def start_program(self):
    # """method to start the program"""
    # is_stop = True
        while True:
            self.sign_up_in_implement()

    def sign_up_in_implement(self):
    # """performs customer sign_up and sign_in using methods from customer class"""
        self.program_startup_instructions()
        # details = self.sign_up()
        # customer = Customer(name="hari", mobile_no="0987654321", d_o_b="12/12/2000", password="hari@321")
        customer = Customer()
        if self.first_choice == 1:
            # sign_up
            customer.sign_up(self.user_accounts_list)
        elif self.first_choice == 2:
            # sign_in
            self.current_user = customer.sign_in(self.user_accounts_list)
            # taking user back if number is not in any user
        
            if self.current_user == -1:
                return
            else:
                self.implement_selection_menu()
            # implementing order and statics men
        elif self.first_choice == 3:
            # return False
            sys.exit()
        else:
            print("Wrong input")                

    def implement_selection_menu(self):
        # """implements the selection menu for ordering and printing statics"""
        while True:
            self.instructions_for_order_statics()
            if self.selection == 1:
                # implementing orders
                self.implement_orders()
            elif self.selection == 2:
                # implementing summary of transactions
                self.print_statics()
            elif self.selection == 3:
                self.current_user.reset_password()
            elif self.selection == 4:
                self.sign_up_in_implement()
            else:
                print("Please enter the correct input define on the instruction")

    def implement_orders(self):
        # """implements dine_in order and online order"""
        while True:
            self.order_types_instruction()
            if self.order_type_option == 1:
                # implement dine in here
                dine_in = DineIn(owner=self.current_user.get_mobile_no())
                dine_in.processing_drinks()
                dine_in.save_order(self.dine_in_orders_list)
            elif self.order_type_option == 2:
                # implement order online here
                self.implement_online_orders()
            elif self.order_type_option == 3:
                break
            else:
                print("Please enter the correct input define on the instruction")

    def implement_online_orders(self):
        # """it implements methods from the pickup_order and delivery_order class"""
        while True:
            self.delivery_instructions()
            if self.mode_of_delivery == 1:
                # implementing the pickup order
                pick_up = PickUpOrder(owner=self.current_user.get_mobile_no())
                pick_up.order_processing()
                pick_up.calculate_total_amount()
                pick_up.save_order(self.pick_up_orders_list)
            elif self.mode_of_delivery == 2:
                # implementing delivery orders
                delivery_order = Delivery(owner=self.current_user.get_mobile_no())
                delivery_order.order_processing()
                if not delivery_order.check_address(self.current_user):
                    # self.implement_online_orders()
                    return
                delivery_order.calculate_total_amount()
                delivery_order.save_order(self.delivery_orders_list)
            elif self.mode_of_delivery == 3:
                break
            else:
                print("Please enter the correct input define on the instructions")

    def print_statics(self):
        # """method to manage the summary of the transactions  """
        all_orders_list = self.pick_up_orders_list + self.dine_in_orders_list + self.delivery_orders_list

        def print_items(order_list):
            # """takes list of orders and print the items required"""
            print("||   Order_ID   ||   Date  ||   Total_Amount   ||    Order_Type   ||")
            for order in order_list:
                print(f"||  S00{order.order_id}   "
                      f"||  {order.order_date}   "
                      f"||  {order.total_amount}  "
                      f"||  {order.order_type}")
                
        def sort_item(order_list):
            # """sort the list of the orders in ascending order"""
            sorted_order = sorted(order_list, key=lambda x: x.order_id)
            return sorted_order
        
        def total_amount_spent(all_order_list):
            # """gets the sum of al the order of the current user"""
            for order in all_order_list:
                self.total += order.total_amount
            print(f"The total amount that user spend on the order is {self.total}")

        
        def filter_order(self, order_list):
            # """filters the order by using the phone number"""
            new_order_list = []
            for order in order_list:
                if order.owner == self.current_user.get_mobile_no():
                    new_order_list.append(order)
            return new_order_list
        
        while True:
            self.instruction_print_statics()
            if self.print_statics_choice == 1:
                print_items(filter_order(self, self.dine_in_orders_list))
                # print_items(self.dine_in_orders_list)
            elif self.print_statics_choice == 2:
                print_items(filter_order(self, self.pick_up_orders_list))
            elif self.print_statics_choice == 3:
                print_items(filter_order(self, self.delivery_orders_list))
            elif self.print_statics_choice == 4:
                sort_item(all_orders_list)
                print_items(filter_order(self, all_orders_list))
            elif self.print_statics_choice == 5:
                total_amount_spent(filter_order(self, all_orders_list))
            elif self.print_statics_choice == 6:
                break
            else:
                print("Please enter the correct input according to the instructions ")
    
class Customer:
    def __init__(self, name='', mobile_no='', d_o_b='', conf_password='', address='', password=''):
        # required for sign_up
        self.__name = name
        self.__mobile_no = mobile_no
        self.__d_o_b = d_o_b
        self.__address = address
        self.__password = password
        self.__conf_password = conf_password
        # for checking attempts
        self.attempts = 0

     # encapsulation principles to access the protected variables
    def get_name(self):
        return self.__name
    def set_name(self, x):
        self.__name = x
    def get_mobile_no(self):
        return self.__mobile_no
    def set_mobile_no(self, x):
        self.__mobile_no = x
    def get_d_o_b(self):
        return self.__d_o_b
    def set_d_o_b(self, x):
        self.__d_o_b = x
    def get_address(self):
        return self.__address
    def set_address(self, x):
        self.__address = x
    def get_password(self):
        return self.__password
    def set_password(self, x):
        self.__password = x
    def set_conf_password(self, x):
        self.__conf_password = x
    def get_conf_password(self):
        return self.__conf_password
    
    def sign_up(self, user_accounts):
        # self.default_input_for_testing()
        self.sign_up_inputs()
        self.validate_user_attributes()
        if self.check_user(self.get_mobile_no(), user_accounts) is None:
            if self.age_validation():
                user_accounts.append(self)
                #print(self.get_d_o_b(), self.get_mobile_no())
                print("Your account is successfully created! Please sign_in now")
            else:
                print("user already exists please ue different number")
                return
            
    def default_input_for_testing(self):
        self.set_name("Babbage")
        # self.set_address("34 babbage street")
        self.set_mobile_no("0987654321")
        self.set_d_o_b("12/12/2000")
        self.set_password("babbage@321")
        self.set_conf_password("babbage@321")

    def sign_up_inputs(self):
        # """gets all the user input and insert into one single user account[list]"""
        self.set_name(input("Please enter your full name as shown : 'Vikram Kumar' ").lower())
        self.set_address(input("Please enter your address , press enter to skip !!"))
        self.set_mobile_no(input("Please enter your contact number starting with 0  :"))
        self.set_d_o_b(input("Please enter your date of birth in 'DD/MM/YYYY' format  : "))
        self.set_password(input("Please enter you password \n "
                            "Must contains alphabets, characters @ and & , also  ending with numbers 'Gina@123' : "))
        self.set_conf_password(input("Enter same password as above  :"))

    def validate_user_attributes(self):
        self.null_value_check()
        validation_methods = (self.contact_validation, self.date_validation, self.password_validation)
        setter_methods = (self.set_mobile_no, self.set_d_o_b, self.set_password)
        for n in range(len(validation_methods)):
            while not validation_methods[n]():
                user_input = input(f"Please enter the correct {validation_methods[n].__name__}")
                setter_methods[n](user_input)
        self.confirm_password()

    def confirm_password(self):
        while self.get_password() != self.get_conf_password():
            self.set_conf_password(input(
                "You confirmation password doesn't matched with previous one !! Please enter again !! "))
            
    def null_value_check(self):
        # """takes object as input checks if required attributes is empty """
        try:
            for attribute, value in vars(self).items():
                # print(attribute)
                self.attempts = 0
                while value == '':
                    if self.check_attempts():
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

    # contact validation needs improvements with regex
    def contact_validation(self):
        # """does contact validation with length, starting character and numerical value, returns true on success"""
        is_valid = re.match('^0[0-9]{9}$', self.get_mobile_no())
        return is_valid
    
    # date of birth validation
    def date_validation(self):
        # """date of birth validation comparing with dd/mm/yy year format, valid inputs returns true of success"""
        valid_dob = False
        try:
            formatted_dob = datetime.strptime(self.get_d_o_b(), '%d/%m/%Y').date()
            self.set_d_o_b(formatted_dob)
            valid_dob = True
        except ValueError:
            valid_dob = False

        return valid_dob
    
    def age_validation(self):
        this_year = datetime.now().year
        if this_year - self.get_d_o_b().year <= 21:
            print("Your age is less tha 21, You are not eligible for sign_up !!")
            return False
        return True
    
    def password_validation(self, new_pass=""):
        # """checks the password requirements and returns true on success """
        if new_pass == "":
            check_password_length = re.match('^[A-Za-z]+[&@]+[0-9]{2,10}$', self.get_password())
        else:
            check_password_length = re.match('^[A-Za-z]+[&@]+[0-9]{2,10}$', new_pass)
        return check_password_length
    
    def check_user(self, user_mobile_no, user_accounts):
        # """returns user if any attribute is matched"""
        for user in user_accounts:
            if user_mobile_no == user.get_mobile_no():
                # print(user)
                return user
            
    # def print_results(statements):
    #     """print formatted results"""
    #     print("|---------------Results------------------|")
    #     print("|                                        |")
    #     print(statements)
    #     print("|                                        |")
    #     print("|----------------------------------------|")

    def check_attempts(self):
        # """return true if attempts is greater than else return false"""
        if self.attempts > 2:
            print("You have used you all 3 attempts, please try again")
            return True
        return False
    
    def sign_in(self, user_accounts):
        # """takes input from user and validates with user credential entered while sign-up """
        user_mobile_no = input("Please enter your mobile_no as username")
        # checking the user
        user = self.check_user(user_mobile_no, user_accounts)
        # first step checking for user
        self.attempts = 0
        while user is not None:
            if self.check_attempts():
                self.reset_password(recover=True)
            # second for password
            user_password = input("Please enter your password for sign in ")
            if user.get_password() == user_password:
                print(f"Hello {user.get_name()} You are successfully logged in using {user_mobile_no} ")
                return user
            else:
                print("credentials doesn't match please try again")
                self.attempts += 1
        else:
            print(f"You have not Signed Up with this number {user_mobile_no}, Please sign in first")
            return -1
        
    def reset_password(self, recover=False):
        mob_number = input("Please enter your username (Mobile Number) : ")
        new_password = input("Please enter your new password : ")
        if mob_number == self.get_mobile_no():
            # checking dob for recovery
            if recover:
             self.check_d_o_b()
            # checking the new password
            if self.new_password_validation_check(new_password):
                self.set_password(new_password)
                print("Password successfully changed")
            else: 
                return
        else:
            print("User doesn't exist on the database")
            return
        
    def new_password_validation_check(self, new_pas):
        # """perform password validation check for new password to change"""
        # print(self.get_password())
        if new_pas != self.get_password():
            while not self.password_validation(new_pas):
                new_pas = input("Wrong password format Please enter your new password again")
            self.set_password(new_pas)
            return True
        else:
            print("You cannot use the same password as before!!")
            return False

    def check_d_o_b(self):
        """if recovery mode is true checks for the d_o_b"""
        d_o_b = input("Please enter your date of birth ")
        # print(self.__d_o_b)
        if self.get_d_o_b() != d_o_b:
            return 
        else:
            return True    
        

class PickUpOrder:
    def __init__(self, order_id="", order_type="Self_Pick_Up", order_date='', order_time='', owner=''):
        # super(Customer, self).__init__()
        self.order_id = order_id
        self.order_type = order_type
        self.order_date = order_date
        self.order_time = order_time
        self.owner = owner
# class items
        self.total_amount = 0
        self.__food_menu_choice = 0
        self.mode_of_delivery = ""
        #for all orders
        # list for saving the order_items
        self.total_order_items = []
        # user requirements details
        self.name_of_person = ''
# menu items
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

    def get_food_menu_choice(self):
        return self.__food_menu_choice
    
    def food_menu(self):
        # """takes the user input as selected menu within the defined items"""
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

    def delivery_instructions(self):
        self.mode_of_delivery = int(input("Enter 1 for Self Pickup \n"
                                          "Enter 2 for Home Delivery \n"
                                          "Enter 3 to go to previous \n"))
        
    # """function to print the details regarding all the orders"""
    def order_processing(self):
        # """calculates total_amount and build a list of total_order_items using food_menu"""
        while self.get_food_menu_choice() != 7:
            self.food_menu()
            if 0 < self.get_food_menu_choice() <= 6:
                item, price = self.build_variable("item", self.get_food_menu_choice())
                self.total_order_items.append(item)
                self.total_amount += price
            elif self.get_food_menu_choice() > 7:
                print("Wrong input please select again !!")

    def build_variable(self, item, item_number):
        # """build the variable from the string for the calculation"""
        built_item = eval(f"self.{item}_{item_number}")
        built_item_price = eval(f"self.{item}_price_{item_number}")
        return built_item, built_item_price
    
    def get_input(self):
        # """gets all the required details regarding order"""
        self.name_of_person = input("Please enter the name of person picking up :")
        self.get_order_date_and_time()

    def get_order_date_and_time(self):
    # """gets order_date and order_time"""
        self.order_time = input("Please input valid order time :")
        self.order_date = input("Please enter valid order date :")

    def calculate_total_amount(self):
        # """calculates the total amount"""
        self.get_input()
        print(f"Your total amount for the order is {self.total_amount}")

    def generate_order_id(self):
        # """generate order id for each order"""
        global order_id_generate
        order_id_generate += 1
        self.order_id = int(f"00{order_id_generate}")

    def save_order(self, orders):
        # """saves the order on the required list """
        # generate the order id
        self.generate_order_id()
        # order_list = [self.order_id, self.order_date, self.total_amount, self.order_type]
        orders.append(self)


class DineIn(PickUpOrder, Customer):
    def __init__(self, order_id='', order_type="Dine_In", order_date='', order_time='', owner=''):
        super().__init__(order_id, order_type, order_date, order_time)
        self.__drinks_menu_choice = 0
        self.owner = owner
        # menu_items
        self._drink_1 = "Coffee"
        self._drink_price_1 = 2
        self._drink_2 = "Cold_Drink"
        self._drink_price_2 = 4
        self._drink_3 = "Shake"
        self._drink_price_3 = 6
        # service charges
        self.__service_charge_rate = 15 / 100
        # user requirements details
        self.__number_of_person = 0

    def drinks_menu(self):
        # """takes user choice of the drink for processing"""
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
            self.drinks_menu()

    def processing_drinks(self):
        # """calculates total_amount and builds the list of the drink item selected"""
        # first processing orders
        self.order_processing()
        while self.__drinks_menu_choice != 4:
            self.drinks_menu()
            if 0 < self.__drinks_menu_choice < 4:
                # building the variable using function
                drink_name, drink_price = self.build_variable("_drink", self.__drinks_menu_choice)
                self.total_order_items.append(drink_name)
                self.total_amount += drink_price
            elif 4 < self.__drinks_menu_choice < 0:
                print("Please enter a valid input from the instruction")
        else:
            self.calculate_total_amount()

    def get_input(self):
        # """get all the inputs required to finalize the order"""
        self.get_order_date_and_time()
        self.name_of_person = int(input("Please enter the number of person you like to visit"))

    def calculate_total_amount(self):
        self.get_input()
        service_charge = round((self.total_amount * self.__service_charge_rate), 2)
        self.total_amount += service_charge
        print(f"Your total payable amount is: AUD {self.total_amount} including AUD {service_charge}for service charges ")

    
class Delivery(PickUpOrder):
    def __init__(self, order_id='', order_type='Delivery', order_date='', order_time='', owner =''):
        super().__init__(order_id, order_type, order_date, order_time)
        # super(Delivery, self).__init__()
        self.delivery_charges = 0
        self.distance_from_restaurant = ''
        self.user_choice = ""
        self.owner = owner

    def check_address(self, user):
        # """checks whether the user address and gets it if empty"""
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

    def get_input(self):
        # """gets required details  for the delivery order"""
        self.get_order_date_and_time()
        self.distance_from_restaurant = eval(input("Please enter the distance from the restaurant in kms"))

    def calculate_delivery_charges(self):
        # """calculates delivery charge according to the distance"""
        if self.distance_from_restaurant > 10:
            self.delivery_charges = 18
        elif self.distance_from_restaurant > 5:
            self.delivery_charges = 10
        elif self.distance_from_restaurant > 0:
            self.delivery_charges = 5
        else:
            print("please enter pick up details we cannot deliver")

    def calculate_total_amount(self):
        # """calculates the total amount for the order"""
        # check address
        # self.check_address(current_user)
        self.get_input()
        self.calculate_delivery_charges()
        self.total_amount += self.delivery_charges
        print(f"Your total payable amount is: AUD {self.total_amount} "
              f"with the additional AUD {self.delivery_charges} charges for deliver")
        

if __name__ == '__main__':
    implement = Implementation()
    implement.start_program()

