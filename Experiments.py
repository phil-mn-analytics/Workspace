int_value = 4
print(int_value)
print(type(int_value))

print(' ----- ')

float_value = float(int_value)
print(float_value)
print(type(float_value))

print(' ----- ')

string_value = str(444044)
print(str(float_value),string_value)

print(' ----- ')

print(int(string_value)+int_value)

#  Operator     Name of Operation	Example	Description
#  +	        Addition	        x + y	x plus y
#  -	        Subtraction	        x - y	x minus y
#  *	        Multiplication	    x * y	x multiplied by y
#  **           Exponentiation	    x ** y	x raised to the power of y
#  /	        Division	        x / y	x divided by y
#  //           Floor Division	    x // y	x divided by y, returning integer
#  %	        Modulo	            x % y	The remainder of x divided by y


#  Operator	Example	Description
#  =	    x = 4	Assign 4 to x
#  +=	    x += 4	Add 4 to existing value of x
#  -=	    x -= 4	Subtract 4 from existing value of x
#  *=	    x *= 4	Multiply existing value by 4
#  /=	    x /= 4	Divide existing value by 4
#  %=	    x %= 4	Modulo existing value by 4

score = 60
 
if score >= 92:
   print('\nYour final grade is an A\n')
 
elif score >= 85:
   print('\nYour final grade is a B\n')
 
elif score >= 70:
   print('\nYour final grade is a C\n')
 
else:
   print('\nTalk with your instructor about your grade!')
   print('\nYou need to do better next time bub!\n')