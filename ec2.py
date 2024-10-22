import random
import string


#Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
num_of_ec2_instances = int(input('How many Ec2 Instances would you like?'))

#Generate random characters and numbers that will be included in the unique name.
departments= ('Marketing', 'Accounting', 'Finops')
Department = input('What Department are you making this EC2 Instance for? ')
def generate_unique_name(department):
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    digits = ''.join(random.choices(string.digits, k=4))
    return f"{department}_{letters}{digits}"
if Department in departments:
    unique_name = generate_unique_name(Department)
    print(f'Unique EC2 instance name: {unique_name}')
else:
    print('Invalid Department. Please select from Marketing, Accounting, or Finops.')
