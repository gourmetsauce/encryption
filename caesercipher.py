uc_upper = 90
uc_lower = 65

lc_upper = 122
lc_lower = 97

def wrap_number(number, lower_bound, upper_bound):
    if number < lower_bound:
        return number + (upper_bound - lower_bound + 1)
    if number > upper_bound:
        return number - (upper_bound - lower_bound + 1)
    return number

def encode(text, key):    
    encoded_text = ''
    for symbol in text:
        if symbol.isalpha():
            encode = ord(symbol) + key
            if symbol.isupper():
                encode = wrap_number(encode, uc_lower, uc_upper)
            else:
                encode = wrap_number(encode, lc_lower, lc_upper)
            encoded_text += chr(encode)
        else:
            encoded_text += symbol
    return encoded_text

def decode(text, key):
    return encode(text, -key)

plain_text = input('Enter text you wish to encode: ')
key = int(input('Enter key you want to use: '))
print(encode(plain_text, key))

plain_text = input('Enter text you wish to decode: ')
key = int(input('Enter key you want to use: '))
print(decode(plain_text, key))
