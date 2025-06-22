def email_slicer():
    while True:
        email = input("Enter email (or 'quit' to exit): ")
        
        if email.lower() == 'quit':
            break
            
        if '@' in email:
            username, domain = email.split('@')
            print(f"Username: {username}\nDomain: {domain}\n")
        else:
            print("Invalid email format. Please include '@' character.\n")

email_slicer()
