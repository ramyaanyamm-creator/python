def xor(x, y):  
    ans = "" 
    for i in range(len(y)):  # Start from 0 to compare all bits 
        if x[i] == y[i]: 
            ans += '0' 
        else: 
            ans += '1' 
    return ans  # Fix the return statement (added a space) 
def divide(dividend, divisor):  
    a = len(divisor) 
    temp = dividend[0:a] 
    # Loop until all bits of the dividend have been processed 
    while a < len(dividend): 
        if temp[0] == '1': 
            temp = xor(divisor, temp) + dividend[a] 
        else: 
            temp = xor('0' * a, temp) + dividend[a] 
        a += 1 
        if temp[0] == '1': 
            temp = xor(divisor, temp) 
        else: 
            temp = xor('0' * a, temp) 
    return temp 
keys = ['1100000001111', '11000000000000101', '10001000000100001'] 
print("Choose the CRC")  
print("1. CRC - 12") 
print("2. CRC - 16")  
print("3. CRC - CCITT ") 
n = int(input())  # Get the user input for CRC type 
 
send = input("Enter the string of code word of binary data bits of 0's and 1's to be sent from the sender: ") 
 
rec = input("Enter the string of code word of binary data received at the receiver side: ") 
# Select the appropriate key based on user choice 
key = keys[n - 1] 
 
# Encoding on sender's side 
length = len(key) 
send1 = send + '0' * (length - 1)  # Append zeros to the message 
rem = divide(send1, key)  # Compute the remainder from the sender's data 
 
# Decoding on receiver's side 
ans = divide(rec, key)  # Compute the remainder from the receiver's data 
 
# Check for transmission errors based on the remainder 
if ans == '0' * (len(key) - 1):  
    print("No error") 
else: 
    print("Frame error") 
