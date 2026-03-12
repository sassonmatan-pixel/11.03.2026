"""Write a program that asks the user to enter the following information:

name
email
phone number
job title
After receiving the input:

Create a dictionary that stores this information
Print the dictionary
Print a formatted business card
Example input:

Enter name: Dana Levi
Enter email: dana@gmail.com
Enter phone: 0501234567
Enter job title: Data Analyst
Possible output:

{'name': 'Dana Levi', 'email': 'dana@gmail.com', 'phone': '0501234567', 'job_title': 'Data Analyst'}

--- Business Card ---
Name: Dana Levi
Email: dana@gmail.com
Phone: 0501234567
Job Title: Data Analyst"""


def take_input() -> tuple[str, str, str, str]:
    """
    This function takes input from the user and converts it into a tuple
    :return: tuple[name, email, phone, job_title]
    """
    input_name = input("Enter name: ")
    input_email = input("Enter email: ")
    input_phone_number = input("Enter phone number: ")
    input_job_title = input("Enter job title: ")
    return input_name, input_email, input_phone_number, input_job_title

def dict_input(name, email, phone, job_title) -> dict:
    """
    This function get tuple and converts it into a dictionary
    :param name:
    :param email:
    :param phone:
    :param job_title:
    :return: dictionary
    """
    user_dict = {
        'name': name,
        'email': email,
        'phone': phone,
        'job_title': job_title
    }
    return user_dict


def business_card(user_dict: dict) -> None:
    """
    This function creates a business card from the input dictionary
    :param user_dict: is the dictionary
    :return: None
    """
    print("\n--- Business Card ---")
    for key, value in user_dict.items():
        print(f"{key}: {value}")

details_user = take_input()
create_dict_details_user = dict_input(details_user[0], details_user[1], details_user[2], details_user[3])
print(create_dict_details_user)
business_card(create_dict_details_user)
