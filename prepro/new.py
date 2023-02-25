
# Taking binary input from user
binary_num = input('Enter a binary number: ')

# Converting the binary input into decimal
dec_num = int(binary_num, 2)

# Converting the decimal number into hexadecimal
hex_num= hex(dec_num)
print('Hexadecimal representation of this binary number is :', hex_num)