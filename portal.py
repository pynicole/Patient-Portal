# Patient Portal Code Sample
# By Nicole Rodgers

# Open file
file = open("patients.txt", "r")
# Create list
patient_names = []
# Add each file item to list
for line in file:
	patient_names.append(line)

# Menu
print('\t-=-=Menu=-=-')
print('\t1. Add a new patient.')
print('\t2. Delete a patient.')
print('\t3. Display all the patients.')
print('\t4. Quit the system.')

# While the program is running
while True:
	# Ask for user input
    choice=int(input('\tPlease enter your choice:'))
    
    # Add new patient
    if choice==1:
        name=input('Please enter the name of the new patient:')
        patient_names.append(name)
        print('New record added.')
    
    # Remove existing patient
    if choice==2:
        name=input('Please enter the name of the patient to delete:')
        if name in patient_names:
            patient_names.remove(name)
            print('Record deleted.')
        else:
            print('No such patient.')
    
    # Display all patients
    if choice==3:
        print(patient_names)
    
    # Exit program
    if choice==4:
        break

file.close()
