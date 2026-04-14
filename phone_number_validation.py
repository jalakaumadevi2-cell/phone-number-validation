# Phone Number Validation System with +91 Support

def validate_phone_number(phone):
    
    # Case 1: Starts with +91
    if phone.startswith("+91"):
        number = phone[3:]  # Extract digits after +91
        
        if len(number) == 10 and number.isdigit() and number[0] in ['6', '7', '8', '9']:
            return "Valid"
        else:
            return "Invalid"
    
    # Case 2: Without +91
    elif len(phone) == 10 and phone.isdigit() and phone[0] in ['6', '7', '8', '9']:
        return "Valid"
    
    else:
        return "Invalid"

# Taking input
phone = input("Enter phone number: ")

# Checking validity
status = validate_phone_number(phone)

# Display result
print("Phone Number Status:", status)
