#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   Program: Run Length Encoding/Decoding
#   Daily Problem #: 29
#   Author: John Deisher
#   Date Started: 5/11/2019
#   Date Finished: 5/11/2019 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. 
The basic idea is to represent repeated successive characters as a single count and character. 
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. 
You can assume the string to be encoded have no digits and consists solely of alphabetic characters. 
You can assume the string to be decoded is valid.
"""

def run_length_encode(string_to_encode):

    encoded_string = ""

    if len(string_to_encode) > 0:
        encode_char = string_to_encode[0]
        string_to_encode = string_to_encode[1:]
        encode_value = 1
    else:
        return ''

    for char in string_to_encode:
        if encode_char == char:
            encode_value += 1
        else:
            #does not match
            encoded_string += str(encode_value) + str(encode_char)
            encode_value = 1
            encode_char = char

    encoded_string += str(encode_value) + str(encode_char)

    return encoded_string
    pass

def run_length_decode(string_to_decode):
    decoded_string = ""
    while len(string_to_decode) > 0:
        value = string_to_decode[0]
        char = string_to_decode[1]
        string_to_decode = string_to_decode[2:]

        for _ in range(int(value)):
            decoded_string += str(char)

    return decoded_string
    pass

def main():

    testCases = list()
    testCases.append("AAAABBBCCDAA")
    testCases.append("AAAABFFFIKKELDKUUUD")
    testCases.append("LLLLL")
    testCases.append("ABBEEEBBA")


    for test in testCases:
        if test == run_length_decode(run_length_encode(test)):
            print("\nTest of: {} Passed".format(str(test)))
            print("Encode: {}".format(run_length_encode(test)))
        else:
            print("\nTest of: {} : Failed".format(str(test)))
            print("Encode: {}".format(run_length_encode(str(test))))
            print("Decode: {}".format(run_length_decode(run_length_encode(test))))
    pass

if __name__ == '__main__':
    main()

"""

Test of: AAAABBBCCDAA Passed
Encode: 4A3B2C1D2A

Test of: AAAABFFFIKKELDKUUUD Passed
Encode: 4A1B3F1I2K1E1L1D1K3U1D

Test of: LLLLL Passed
Encode: 5L

Test of: ABBEEEBBA Passed
Encode: 1A2B3E2B1A
[Finished in 0.1s]
"""