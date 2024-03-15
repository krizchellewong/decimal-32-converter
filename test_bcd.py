    
# DELETE BEFORE SUBMISSION

# FUNCTION: convert to binary
def int_to_binary(number):
    # [2:] slices the string to remove the '0b' prefix
    # bin returns a string
    return bin(number)[2:]


packed_bcd = ["1001", "1000", "1001"]

densely_packed_bcd = ""
a = packed_bcd[0][0]
e = packed_bcd[1][0]
i = packed_bcd[2][0]

# concatenate a, e, i
aei = a + e + i
print("aei: " + aei)

# densely_packed_bcd format = pqrstuvwxy
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
        #convert position to binary
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

print(densely_packed_bcd)

