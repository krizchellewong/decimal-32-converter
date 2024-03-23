# FUNCTION: check if number is finite
def check_number(number, exponent):
    if exponent > 90 or exponent < -101:
        return False
    return True


# FUNCTION: get sign bit
def get_sign_bit(number):
    if number < 0:
        return "1"
    else:
        return "0"


# FUNCTION: convert to binary
def int_to_binary(number):
    # [2:] slices the string to remove the '0b' prefix
    # bin returns a string
    return bin(number)[2:]


# FUNCTION: normalize number so it's 7 numbers long
def normalize(number, exponent):
    add_exp = 0
    while number >= 10 ** 7:
        number /= 10
        add_exp += 1
    while number < 10 ** 6 and number != 0 and number % 1 != 0 and int(number) != 7:
        number *= 10
        add_exp -= 1
    
    return number, exponent + add_exp

# FUNCTION: rounding
def rounding(length, sign_bit, number):
    #calculate how many excess numbers
    excess = length - 7
    n = 1

    #TEMP FIX: if number is > 7 whole digits, adjust to 7 digits w/ decimal
    if(number % 1 == 0):
        number = number / (10**excess)

    #remove any irrelevant decimal digits
    if((len(str(number)) - 1) != length) and (number % 1 != 0):
        index =  length + 1
        number = float(str(number)[:index])

    #loop until user inputs a valid rounding type
    while(n == 1):
        print(" 1. C - Ceiling\n 2. F - Floor\n 3. Z - Round to Zero\n 4. N - Round to Nearest (Ties to Even)")
        r_type = str(input("Enter rounding type: "))

        #Ceiling
        if(r_type == 'C' or r_type == 'c'):
            #if number is positive
            if(sign_bit == '0'):
                number = int(number)
                number += 1
            #if number is negative
            elif(sign_bit == '1'):
                number = int(number)
            #break out of loop
            n = 0

        #Floor
        elif(r_type == 'F' or r_type == 'f'):
            #if number is positive
            if(sign_bit == '0'):
                number = int(number)
            #if number is negative
            elif(sign_bit == '1'):
                number = int(number)
                number -= 1
            #break out of loop
            n = 0

        #Round to Zero/Truncate
        elif(r_type == 'Z' or r_type == 'z'):
            number = int(number)
            #break out of loop
            n = 0

        #Round to Nearest (Ties to Even)
        elif(r_type == 'N' or r_type == 'n'):
            number = round(float(number))
            n = 0
        else:
            print("Invalid Input. Please Try Again.")
    
    return number

# FUNCTION: get e'
def get_e_prime(exponent):
    return exponent + 101


# FUNCTION: get combination field
def get_combi_field(msd, e_prime):
    # call convert to binary function
    msd_binary = int_to_binary(msd).zfill(4)
    print("MSD: " + msd_binary)
    # if most sig. digit < 8 
    if msd < 8:
        # get first two digits of e'
        # append last three digits of MSD
        combi_field = e_prime[:2] + msd_binary[-3:]
    # if most sig. digit >= 0
    else:
        # add 11 to the front of the combi field
        # append first two digits of e'
        # append least significant bit of MSD
        combi_field = "11" + e_prime[:2] + msd_binary[-1]
    return combi_field


# FUNCTION: convert to packed bcd 
def convert_to_densely_packed_bcd(number):
    packed_bcd = []
    densely_packed_bcd = ""

    for digit in str(number):
        binary_digit = bin(int(digit))[2:].zfill(4)  # Convert each digit to binary
        packed_bcd.append(binary_digit)
    print("Packed BCD: " + str(packed_bcd))
    a = packed_bcd[0][0]
    e = packed_bcd[1][0]
    i = packed_bcd[2][0]

    # concatenate a, e, i
    aei = a + e + i
    print("aei: " + aei)

    # densely_packed_bcd format = pqr stu v wxy
    # if there are no 1s in aei
    if aei.count("1") == 0:
        v = "0"
        # copy every digit in packed_bcd aside from the first
        for binary_digit in packed_bcd:
            # if index of binary_digit is 2
            if packed_bcd.index(binary_digit) == 2:
                densely_packed_bcd += v
            densely_packed_bcd += binary_digit[1:]
    else:
        r = packed_bcd[0][3]
        u = packed_bcd[1][3]
        y = packed_bcd[2][3]
        v = "1"
        if aei.count("1") == 1:
            # count position of 1 (right-most digit is index 0)
            position = aei[::-1].index("1")
            # convert position to binary
            wx = int_to_binary(position).zfill(2)
            # find indexes of the two 0s in aei
            first_zero = aei.index("0")
            second_zero = aei[first_zero + 1:].index("0") + first_zero + 1
            print("first zero: " + str(first_zero))
            print("second zero: " + str(second_zero))
            # st is always the middle binary digits fg
            if first_zero == 0:
                pq = packed_bcd[first_zero][1:3]
                st = packed_bcd[second_zero][1:3]
            else:
                pq = packed_bcd[second_zero][1:3]
                st = packed_bcd[first_zero][1:3]
            densely_packed_bcd = pq + r + st + u + v + wx + y

        elif aei.count("1") == 2:
            wx = "11"
            # count position of 0 (right-most digit is index 0)
            position = aei[::-1].index("0")
            st = int_to_binary(position).zfill(2)
            # find position of 1
            position = aei.index("0")
            pq = packed_bcd[position][1:3]

            densely_packed_bcd = pq + r + st + u + v + wx + y

        elif aei.count("1") == 3:
            pq = "00"
            st = "11"
            wx = "11"
            densely_packed_bcd = pq + r + st + u + v + wx + y

    print("Densely Packed BCD: " + densely_packed_bcd)
    return densely_packed_bcd


def decimal_32_floating_point_converter():
    # input number with exponent
    number = float(input("Enter a number: "))
    exponent = int(input("Enter an exponent (base-10): "))

    # if the number is a normal case
    if check_number(number, exponent):
        # get sign bit
        sign_bit = get_sign_bit(number)
        # get absolute value of number
        number = abs(number)

        #check length of number
        #whole or with .0
        if(number % 1 == 0):
            number = int(number)
            length = len(str(number))
        else:
            length = len(str(number)) - 1

        # if number is floating point
        if number % 1 != 0:
            number, exponent = normalize(number, exponent)
        else:
            number = int(number)

        # TODO: check if number of digits > 7
        # if yes, ask for preferred rounding method
        if(length > 7):
            number = rounding(length, sign_bit, number)

        # make number a string
        number_str = str(number)

        # pad 0s until there are 7 whole digits
        number_str = number_str.zfill(7)
        print("Normalized number: " + number_str)
        print("Exponent: " + str(exponent))

        # get most significant digit
        msd = int(number_str[0])

        # call get e' function
        e_prime = get_e_prime(exponent)

        # convert e' to binary
        e_prime = int_to_binary(e_prime).zfill(8)
        print("E': " + e_prime)

        # get combination field
        combi_field = get_combi_field(msd, e_prime)

        # get exponent continuation
        exp_cont = e_prime[2:]

        coefficient_cont = ""
        # for every three digits, convert to packed bcd
        for i in range(1, len(number_str), 3):
            sliced = number_str[i:i + 3]
            print("Sliced: " + sliced)
            coefficient_cont += ' ' + convert_to_densely_packed_bcd(sliced)

        return sign_bit + ' ' + combi_field + ' ' + exp_cont + coefficient_cont

    else:
        return "Number is infinite"


def hex_converter(bin_val):
    bin_val = bin_val.replace(" ", "")
    hex_val = ""

    while len(bin_val) > 0:
        select_4 = bin_val[:4]
        if select_4 == "0000":
            hex_val += "0"
        elif select_4 == "0001":
            hex_val += "1"
        elif select_4 == "0010":
            hex_val += "2"
        elif select_4 == "0011":
            hex_val += "3"
        elif select_4 == "0100":
            hex_val += "4"
        elif select_4 == "0101":
            hex_val += "5"
        elif select_4 == "0110":
            hex_val += "6"
        elif select_4 == "0111":
            hex_val += "7"
        elif select_4 == "1000":
            hex_val += "8"
        elif select_4 == "1001":
            hex_val += "9"
        elif select_4 == "1010":
            hex_val += "A"
        elif select_4 == "1011":
            hex_val += "B"
        elif select_4 == "1100":
            hex_val += "C"
        elif select_4 == "1101":
            hex_val += "D"
        elif select_4 == "1110":
            hex_val += "E"
        elif select_4 == "1111":
            hex_val += "F"

        bin_val = bin_val[4:]
    return hex_val


# MAIN
def main():
    # TODO: loop until user wants to exit
    result = decimal_32_floating_point_converter()
    print("Result: " + result)

    # TODO: convert result to hex and print
    hex_val = hex_converter(result)
    print("Hex: " + hex_val + "\n")

    # TODO: option to output result as a text file
    choice = input("Would you like to save the result to a text file? (Y/Any key): ")
    if choice == 'Y' or choice == 'y':
        f = open("result.txt", "w")
        f.write("Binary: " + result + "\n")
        f.write("Hex: " + hex_val)
        f.close()
        print("Result saved to result.txt")

if __name__ == "__main__":
    main()
