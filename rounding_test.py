#Rounding
def rounding(length, sign_bit, number):
    excess = length - 7
    n = 1

    while(n == 1):
        print(" 1. C - Ceiling\n 2. F - Floor\n 3. Z - Round to Zero\n 4. N - Round to Nearest (Ties to Even)")
        r_type = str(input("Enter rounding type: "))

        if(r_type == 'C' or r_type == 'c'):
            #if number is positive
            if(sign_bit == '0'):
                number = number/(10**excess)
                number += 1
            #if number is negative
            elif(sign_bit == '1'):
                number = int(number/(10**excess))
            #break out of loop
            n = 0

        elif(r_type == 'F' or r_type == 'f'):
            #if number is positive
            if(sign_bit == '0'):
                number = int(number/(10**excess))
            #if number is negative
            elif(sign_bit == '1'):
                number = int(number/(10**excess))
                number -= 1
            #break out of loop
            n = 0

        elif(r_type == 'Z' or r_type == 'z'):
            number = int(number/(10**excess))
            #break out of loop
            n = 0

        elif(r_type == 'N' or r_type == 'n'):
            #if number is positive
            if(sign_bit == '0'):
                #if last digit is greater than 5
                if(number[-1] > 5):
                    number = int(number/(10**excess))
                    number += 1
                #if last digit is less than 5
                elif(number[-1] < 5):
                    number = int(number/(10**excess))
                #if last digit is 5
                elif(number[-1] == 5):
                    number = int(number/(10**excess))
                #break out of loop
                n = 0
            
            #if number is negative
            if(sign_bit == '1'):
                #if last digit is greater than 5
                if(number[-1] > 5):
                    number = int(number/10)
                    number -= 1
                #if last digit is less than 5
                elif(number[-1] < 5):
                    number = int(number/10)
                #if last digit is 5
                elif(number[-1] == 5):
                    number = int(number/10)   
                #break out of loop
                n = 0     
        else:
            print("Invalid Input. Please Try Again.")
    
    return number

# FUNCTION: get sign bit
def get_sign_bit(number):
    if number < 0:
        return "1"
    else:
        return "0"
    
#MAIN FUNC
def decimal_32_floating_point_converter():
    # input number
    number = int(input("Enter a number: "))

    # get sign bit
    sign_bit = get_sign_bit(number)

    #get length of the number
    if(sign_bit == '1'):
        length = len(str(number)) - 1
    else:
        length = len(str(number))
    
    if(length > 7):
        number = rounding(length, sign_bit, number)
        print("Rounded number: " + str(number))
    else:
        print("Number is already normalized") 

def main():
    decimal_32_floating_point_converter()

if __name__ == "__main__":
    main()

