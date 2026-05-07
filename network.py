'''
Network  support team= IT service Desk Help System
currently writing
A menu -drivem IT Service Desk Application for Netwrok support Team 
which allow staff to  submit ticket,check their status,
view open/unresolved ticket, update status and platform for reporting, 
tracking, and resolving issues related to IT services

'''

def submit_ticket():
    print("Submitting a new ticket....")
    print("\n Select Ticket Urgency")
    print("1. Low urgency")
    print("2 Medium urgency")
    print("High urgency")

    urgency_choice=input("Enter urgency level")
    if urgency_choice=="1":
        urgency="Low urgency (minor issues,no impact on operations)"
    elif urgency_choice=="2":
        urgency="Medium urgency(moderate issue, partial impact)"
    elif urgency_choice=="3":
        urgency="High urgency (critical issues, system down)"
    else:
        urgency="unknown urgency"
    print(f"\nTicket submitted with:{urgency}")

def check_status():
    print("Checking ticket status...")

def view_open_ticket():
    print("viewing open ticket...")

def exit_program():
    print("Exiting system..")
    return False 

menu_options={
    "1":submit_ticket,
    "2":check_status,
    "3":view_open_ticket,
    "4":exit_program
}
def main():
    running=True
    while running:
        print("\n===IT Service Desk====")
        print("1. Submit  a New Ticket")
        print("2.Check Ticket Status")
        print("3.View Open Tickets")
        print("4.Exit")
        choice=input("Select an option: ").strip()
        action=menu_options.get(choice)
        if action:
            result=action()
            if result is False:
                running=False
        else:
            print("Invalid choice, please try again")

if __name__=="__main__":
    main()