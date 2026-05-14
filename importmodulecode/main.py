#python IT project Network Help System
#improt date module for generated  date and time
from datetime import datetime
# import random module for generating random digit for ticket_id
import random

#dictionary used to store all ticket
tickets={}

#ticket status
status_open="Open"
status_inprogress="in-progress"
status_closed="solved"

#function return formated current date and time
def get_current_datetime():
    return datetime.now().strftime("%d -%m- %Y  %H:%M:%S")

def get_ticket_id():
    ticket_id=input("Enter ticke id: ")
    #check for input validation where ticket must ne numeric
    if not ticket_id.isdigit():
        print("Ticket ID muts be numeric")
        return None #stop here in case
    return int(ticket_id)

#function generated ramdom and unique ticket id
def generate_ticket_id(already_ids):
    while True:
        #generated ticket id randomly from 1000 t0 9998
        ticket_id=random.randint(1000,9999) 

        # check whether ticket id is unique, it is then return ticket_id
        if ticket_id not in already_ids:
            return ticket_id

#function to display ticket information     
def display_ticket(ticket):
    print("\n------------------------")
    print(f" Ticket ID is:{ticket['ticket_id']}")
    print(f" Description is: {ticket['description']}")
    print(f" Priority is: {ticket['priority']}")
    print(f" Status is: {ticket['status']}")
    print(f"Created at : {ticket['created_at']}")
    #display closed time only if ticket is solved
    if ticket["closed_at"]:
        print(f"Closed at :{ticket['closed_at']}")

    print("--------------------------------")

#function to define priority of ticket
def classify_urgency():
    print("\n Select Ticket Urgency")
    print("1.Low - Minor issue")
    print("2.Medium - Partial Impact")
    print("3.High - Critical  issue/System Down")

    while True:
        choice=input("Enter urgency choice(1-3)").strip()
        if choice=="1":
            return "Low"
        elif choice=="2":
            return "Medium"
        elif choice=="3":
            return"High"
        else:
            print("Invalid choice. Please enter 1-3")

#create and store new ticket
def submit_ticket():
    print("\n=== Submit new Ticket===")
    description=input("Enter issue Description: ").strip()
    #validate for whether description is empty or not
    if description=="":
        print("Description cannot be empty")
        return
    #assign priority of  ticket urgency
    priority=classify_urgency()

    #call  generate_ticket_id for generated unique id for ticket
    ticket_id=generate_ticket_id(list(tickets.keys()))

    #create new ticket
    ticket={
        "ticket_id":ticket_id,
        "description":description,
        "priority":priority,
        "status":status_open,
        "created_at":get_current_datetime(),
        "closed_at":None,

    }
    #store ticket in tickets dictionary
    tickets[ticket_id]=ticket
    print("\n Ticket Submitted Successfully")

    #display created ticket
    display_ticket(ticket)

#check ticket status and detail suing ticket Id
def check_ticket_status():
    print("\n=== Check Ticket status=====")

    #get_ticket_id() function to get ticket id from use
    ticket_id=get_ticket_id()

    #return none  if ticket_id is invalid input
    if ticket_id is None:
        return
    #check ticket_id is exist
    if ticket_id in tickets:
        display_ticket(tickets[ticket_id])
    else:
        print("Ticket not found")

#display all unresolved tickets
def display_open_ticket():
    print("\n=== Open Ticket====")
    found=False
    #looping ticket
    for ticket in tickets.values():
        #display all open tickets
        if ticket["status"]==status_open:
            display_ticket(ticket)
            found=True

    #print is there is no open ticket
    if not found:
         print("No open tickets available")

 #solve ticket issue - change open ticket to in-progress    
def inprogress_ticket():
    print("\n==In-*rogress ticket==")
    ticket_id=get_ticket_id()
    if ticket_id is None:
        return
    if ticket_id in tickets:
        ticket=tickets[ticket_id]
        print("\n Current Ticket Details")
        display_ticket(ticket)
        #
        if ticket["status"].lower()!="Open":
            print("This ticket must be in opn status ")
            return
        
        confirm=input("\n Do you want to solve this ticket?(y/n)").strip().lower()
        if confirm in ["y","yes"]:
            ticket["status"]=status_inprogress
            print("Ticket has been marked as in-progress")
        else:
            print("Operation cancalled")  
    
    else:
        print("Ticket is not found")

#close ticket only if it status is in-progress
def closed_ticket():
    #get ticket id from user
    ticket_id=get_ticket_id()
    #return if ticket_id  doesnot exist
    if ticket_id is None:
        return
    #serch ticket_id in ticket dictionary
    if ticket_id in tickets:
        ticket=tickets[ticket_id]

        #ticked marked as close or solved only of it is in-progress status
        if ticket["status"] !=status_inprogress:
            print("Only in-progress tickets can be closed")
            return
        ticket["status"]=status_closed
        ticket["closed_at"]=get_current_datetime()
        print("Ticket CLOSED successfully.")
    else:
        print("Ticket not found")

#display menu system
def display_menu():
    print("\n===============================")
    print("1.Submit New Ticket")
    print("2.Check Ticket Status")
    print("3.Display Open Ticket")
    print("4.Resolve/In-progress  Ticket")
    print("5.Closed Ticket")
    print("6.Exit")

def main():
    while True:
        #this function display menu
        display_menu()
        #take menu choice form user
        choice=input("\n Enter your Chooce:").strip()
        if choice=="1":
            submit_ticket()
        elif choice=="2":
            check_ticket_status()
        elif choice=="3":
            display_open_ticket()
        elif choice=="4":
            inprogress_ticket()  
        elif choice=="5":
            closed_ticket()
        elif choice=="6":
            print("Existing Network support system")
            print("Thank You")
            break
        else:
            print("Oops!! Invalid menu choice.Please try again")
if __name__=="__main__":
    main()

