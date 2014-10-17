############################################
#                                          # 
#                   100pt                  #
#             Patient Diagnosis            #
############################################

# Create a program that tests if patients needs to be admitted to the hospital.
# Ask the user for their temperature, and if they have been sick in the last 24 hours.
# Additionally, ask if the user has recently travelled to West Africa.
# The program should continue to run until there are no patients left to diagnose (i.e. a while loop).

# Criteria for Diagnosis:
# - A temperature of over 105F
# - A temperature of over 102F and they have been sick in the last 24 hours
# - A temperature over 100, OR they've been sick in the last 24 hours, AND they've recently travelled to West Africa.

print 'How many patients are there'
userinput1 = raw_input()
userinput2 = raw_input().lower
for x in range(int(userinput1)):
    print 'What is your temperature?'
    userinput3 = int(raw_input())
    if userinput3>=105:
        print 'You need to see a doctor'
    else:
        print 'You will be fine'
    
    print 'Have you been sick in the last 24 hours?'
    userinput4 = raw_input()
    if userinput4 == 'yes':
        print 'You need to see a doctor'
    else:
        print 'You will be fine'
    
    print 'Have you recently travled to West Africa?'
    userinput5 = raw_input()
    if userinput5 == 'yes':
        print 'You need to see a doctor'
    else:
        print 'You are fine'
    if userinput3>=102 and userinput4 == 'yes':
        print 'We need to get you checked out'
    if userinput3>=102 and userinput4 == 'yes' and userinput5 == 'yes':
        print 'We need to get you to a hosbital'
    