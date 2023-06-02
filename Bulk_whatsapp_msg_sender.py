ascii_art = '''
   ▄████████    ▄█   ▄█▄   ▄▄▄▄███▄▄▄▄   
  ███    ███   ███ ▄███▀ ▄██▀▀▀███▀▀▀██▄ 
  ███    ███   ███▐██▀   ███   ███   ███ 
  ███    ███  ▄█████▀    ███   ███   ███ 
▀███████████ ▀▀█████▄    ███   ███   ███ 
  ███    ███   ███▐██▄   ███   ███   ███ 
  ███    ███   ███ ▀███▄ ███   ███   ███ 
  ███    █▀    ███   ▀█▀  ▀█   ███   █▀  
               ▀                         
'''

print(ascii_art)

# Author: Annaveri_Kannaiyan

import pywhatkit
import time
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import pandas as pd

# Ask user for message type (common or personalized)
print("Would you prefer to send common messages or personalized messages to everyone?")
message_type = input("Enter 'C' for common message or 'P' for personalized message: ")

if message_type.upper() == 'C':
    # Common message
    numbers_file_path = input("Enter the path to the numbers file: ")
    message_file_path = input("Enter the path to the message file: ")
    chromedriver_path = input("Enter the path to the chromedriver: ")

    # Read sender numbers from a text file
    with open(numbers_file_path, 'r') as file:
        sender_numbers = [line.strip() for line in file]

    # Read message from a text file
    with open(message_file_path, 'r', encoding='utf-8') as file:
        message = file.read()

    # Set chromedriver path
    pywhatkit.chromedriver_path = chromedriver_path

    # Calculate the delay between messages
    delay = 4  # 4 seconds delay between each message

    # Iterate through sender numbers and send messages
    for number in sender_numbers:
        try:
            # Validate the phone number
            parsed_number = phonenumbers.parse(number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                print(f"Invalid number: {number}")
                continue

            # Use pywhatkit to send the message
            pywhatkit.sendwhatmsg_instantly(number, message)

            # Print success message if the message is sent successfully
            print(f"Message sent to {number} - Successful")

        except Exception as e:
            # Print error message if there is an exception (network issues, etc.)
            print(f"Message sent to {number} - Unsuccessful. Error: {str(e)}")

        # Wait for the specified delay before sending the next message
        time.sleep(delay)

elif message_type.upper() == 'P':
    # Personalized message
    excel_file_path = input("Enter the path to the Excel file: ")
    chromedriver_path = input("Enter the path to the chromedriver: ")
    country_code = input("Enter the country code: ")
    personalized_message = input("Enter the personalized message for all recipients: ")

    # Read data from the Excel file
    df = pd.read_excel(excel_file_path)

    # Set chromedriver path
    pywhatkit.chromedriver_path = chromedriver_path

    # Calculate the delay between messages
    delay = 4  # 4 seconds delay between each message

    # Iterate through rows in the DataFrame
    for _, row in df.iterrows():
        number = country_code + str(row['Number'])
        name = row['Name']
        main_message = row['Message']
        message = f"{personalized_message} {name}\n{main_message}"

        try:
            # Validate the phone number
            parsed_number = phonenumbers.parse(number, None)
            if not phonenumbers.is_valid_number(parsed_number):
                print(f"Invalid number: {number}")
                continue

            # Use pywhatkit to send the message
            pywhatkit.sendwhatmsg_instantly(number, message)

            # Print success message if the message is sent successfully
            print(f"Message sent to {number} - Successful")

        except Exception as e:
            # Print error message if there is an exception (network issues, etc.)
            print(f"Message sent to {number} - Unsuccessful. Error: {str(e)}")

        # Wait for the specified delay before sending the next message
        time.sleep(delay)

else:
    print("Invalid message type. Please enter 'C' for common message or 'P' for personalized message.")
