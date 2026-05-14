# Python IT Service Desk System – Final Project

from datetime import datetime
import random

# =========================
# GLOBAL DATA STRUCTURES
# =========================

tickets = {}


PRIORITY_LEVELS = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

STATUS_OPEN = "Open"
STATUS_INPROGESS= "In-progress"
STATUS_CLOSED= "closed"


# =========================
# UTILITY FUNCTIONS
# =========================


def get_current_time():
    """Return formatted current date and time."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")



def generate_ticket_id(existing_ids):
    """Generate unique random ticket ID."""

    while True:
        #generated 
        ticket_id = random.randint(1000, 9999)

        if ticket_id not in existing_ids:
            return ticket_id



def display_ticket(ticket):
    """Display ticket information neatly."""

    print("\n-----------------------------")
    print(f"Ticket ID   : {ticket['ticket_id']}")
    print(f"Description : {ticket['description']}")
    print(f"Priority    : {ticket['priority']}")
    print(f"Status      : {ticket['status']}")
    print(f"Created At  : {ticket['created_at']}")

    if ticket['closed_at']:
        print(f"Resolved At : {ticket['closed_at']}")

    print("-----------------------------")



def classify_urgency():
    """Allow user to select urgency level."""

    print("\nSelect Ticket Urgency")
    print("1. Low - Minor issue")
    print("2. Medium - Partial impact")
    print("3. High - Critical issue / system down")

    while True:
        choice = input("Enter urgency choice (1-3): ").strip()

        if choice == "1":
            return "Low"

        elif choice == "2":
            return "Medium"

        elif choice == "3":
            return "High"

        else:
            print("Invalid choice. Please try again.")


# =========================
# MAIN SYSTEM FUNCTIONS
# =========================


def submit_ticket():
    """Create and store a new ticket."""

    print("\n=== Submit New Ticket ===")

    description = input("Enter issue description: ").strip()

    if description == "":
        print("Description cannot be empty.")
        return

    priority = classify_urgency()

    ticket_id = generate_ticket_id(tickets.keys())

    ticket = {
        "ticket_id": ticket_id,
        "description": description,
        "status": STATUS_OPEN,
        "priority": priority,
        "created_at": get_current_time(),
        "resolved_at": None
    }

    tickets[ticket_id] = ticket

    

    print("\nTicket submitted successfully.")

    print("Ticket ID :", ticket["ticket_id"])
    print("Status    :", ticket["status"])
    print("Priority  :", ticket["priority"])
    print("Description :", ticket["description"])


def check_ticket_status():
    """Check ticket details using ticket ID."""

    print("\n=== Check Ticket Status ===")

    try:
        ticket_id = int(input("Enter Ticket ID: "))

    except ValueError:
        print("Invalid input. Ticket ID must be numeric.")
        return

    ticket = tickets.get(ticket_id)

    if ticket:
        display_ticket(ticket)

    else:
        print("Ticket not found.")



def display_open_tickets():
    """Display all unresolved tickets."""

    print("\n=== Open Tickets ===")

    found = False

    for ticket in tickets.values():

        if ticket["status"] == STATUS_OPEN:
            display_ticket(ticket)
            found = True

    if not found:
        print("No open tickets available.")



def r_ticket():
    """Mark a ticket as resolved."""

    print("\n=== Resolve Ticket ===")

    try:
        ticket_id = int(input("Enter Ticket ID to resolve: "))

    except ValueError:
        print("Invalid input. Ticket ID must be numeric.")
        return

    ticket = tickets.get(ticket_id)

    if not ticket:
        print("Ticket not found.")
        return

    if ticket["status"] == STATUS_RESOLVED:
        print("Ticket is already resolved.")
        return

    ticket["status"] = STATUS_RESOLVED
    ticket["resolved_at"] = get_current_time()

    print("Ticket resolved successfully.")



def process_highest_priority_ticket():
    """Display highest priority open ticket."""

    print("=== Highest Priority Ticket ===")

    open_tickets = []

    for ticket in tickets.values():

        if ticket["status"] == STATUS_OPEN:
            open_tickets.append(ticket)

    if not open_tickets:
        print("No open tickets available.")
        return

    highest_ticket = min(
        open_tickets,
        key=lambda ticket: PRIORITY_LEVELS[ticket["priority"]]
    )

    print("Processing highest priority open ticket:")
    display_ticket(highest_ticket)


# =========================
# MENU FUNCTION
# =========================


def display_menu():
    """Display system menu."""

    print("\n=================================")
    print(" IT SERVICE DESK MANAGEMENT")
    print("=================================")
    print("1. Submit a New Ticket")
    print("2. Check Ticket Status")
    print("3. Display Open Tickets")
    print("4. Resolve Ticket")
    print("5. Process Highest Priority Ticket")
    print("6. Exit")


# =========================
# MAIN PROGRAM LOOP
# =========================


def main():
    """Run IT Service Desk system."""

    while True:

        display_menu()

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            submit_ticket()

        elif choice == "2":
            check_ticket_status()

        elif choice == "3":
            display_open_tickets()

        elif choice == "4":
            resolve_ticket()

        elif choice == "5":
            process_highest_priority_ticket()

        elif choice == "6":
            print("\nExiting IT Service Desk System...")
            print("Thank you.")
            break

        else:
            print("Invalid menu choice. Please try again.")


# =========================
# PROGRAM START
# =========================

if __name__ == "__main__":
    main()
