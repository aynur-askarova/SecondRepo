name=input('Input your name: ')
age=int(input('Input your age: '))
favourite_number=int(input('Input your favourite number: '))
age_in_10_years=age+10
square_of_favourite_number=favourite_number**2
if favourite_number%2==0:
    odd_or_even='even'
else:
    odd_or_even='odd'
print(f"Hi {name}! In 10 years you'll be {age_in_10_years}. Your favourite number squared is {square_of_favourite_number}, and it's {odd_or_even}.")
'''When we get input from the user, it gives us a string, this is a rule for python programming languages. Another rule is that we can only do mathematical operations with numbers, so we need to convert this input to an integer or float. We can do this by using the int() or float() functions.'''