import csv


with open("address_book.csv", "w", newline="") as file:
    writer = csv.writer(file)

  
    writer.writerow(["Name", "Address", "Mobile", "Email"])

    
    for i in range(3):
        print("\nEnter details for person", i+1)

        name = input("Enter Name: ")
        address = input("Enter Address: ")
        mobile = input("Enter Mobile Number: ")
        email = input("Enter Email: ")

        writer.writerow([name, address, mobile, email])

print("\nData successfully stored in address_book.csv")