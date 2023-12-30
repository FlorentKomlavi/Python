print('Welcome to the tip calculator')
total_bill = float(input('What is your total bill?\n'))
tip = int(input('What percentage tip would you like to give: \n'))
num_people = int(input('How many people to split the bill?\n'))
# convert tip into decimal.
tip = tip / 100
# Calculate bill plus tip.
total_to_split = total_bill * (1+tip)
print(f'The total bill is ${total_to_split:^.2f}')
# Calculate what each person has to pay.
each_part = total_to_split / num_people
print(f'Each person should pay: ${each_part:^.2f}')