import math
# golomb code function for compression
def golomb_encode(n, m):
    """Encodes an integer n using Golomb coding with divisor m."""
    # Calculate quotient and remainder
    q = n // m  
    r = n % m   

    # Unary code for the quotient
    unary_code = '1' * q + '0'
    
    # Calculate the number of bits needed for the binary representation of the remainder
    b = math.ceil(math.log2(m))
    if (1 << b) - m > r:
        b -= 1

    # Binary code for the remainder
    binary_code = format(r, f'0{b}b')
    
    return unary_code + binary_code

# print("compression")
# print()

# test on numbers
# test 1
# m = 5  
# number_to_encode = 21
# encoded = golomb_encode(number_to_encode, m)
# print("test 1")
# print()
# print(f"Original number: {number_to_encode}")
# print(f"Encoded: {encoded}")

# test 2
# m = 4  
# numbers_to_encode = [10, 15, 23, 34, 45, 56, 78, 100, 150, 200]
# encoded_data = [golomb_encode(number, m) for number in numbers_to_encode]
# # Print results
# print()
# print("test 2")
# print()
# print("Original numbers:", numbers_to_encode)
# print("Encoded data:", encoded_data)


# golomb code function for decompression
def golomb_decode(encoded, m):
    """Decodes a Golomb-encoded string with divisor m."""
    #Decode the unary code to get the quotient
    q = 0
    i = 0
    while i < len(encoded) and encoded[i] == '1':
        q += 1
        i += 1
    
    #Move '0' at end of the unary code
    i += 1

    #Decode the binary code to get the remainder
    #Calculate the number of bits required for the binary part
    b = math.ceil(math.log2(m))
    if (1 << b) - m > 0:
        b -= 1
    
    #Read the binary part and convert it to an integer
    r = int(encoded[i:i + b], 2) #remainder
    
    #Compute the original number
    decoded_number = q * m + r
    return decoded_number

# print()
# print("Decompression")
# print()
# # test on numbers       
# # test 1
# test1 =golomb_decode('1111001',5)
# print("decompression for a number")
# print()
# print(test1)

# # test on array of numbers
# # test 2
# test2 = [golomb_decode(encoded, m) for encoded in encoded_data]

# # Print results
# print("decompression for an array of numbers")
# print()
# print("Encoded data:", encoded_data)
# print("Decoded numbers:", test2)