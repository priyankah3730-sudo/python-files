print("Ticket booking counter>>")
ticket=1
while ticket<=8:
    print(f"The seat number {ticket} alloted for you")
    ticket+=1
    if ticket>8:
        print("All seats are booked")