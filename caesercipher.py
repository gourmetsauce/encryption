import sys, argparse

# upper and lower bounds for the characters a-z(LC) and A-Z(UC)
UC_UPPER = 90
UC_LOWER = 65
LC_UPPER = 122
LC_LOWER = 97

# makes sure that the number is within a certain range
def wrap_number(number, lower_bound, upper_bound):
    if number < lower_bound:
        return number + (upper_bound - lower_bound + 1)
    if number > upper_bound:
        return number - (upper_bound - lower_bound + 1)
    return number

# uses the key to substitute the approprate characters in the given text
def encode(text, key): 
    encoded_text = ''
    for symbol in text:
        if symbol.isalpha():
            encode = ord(symbol) + key
            if symbol.isupper():
                encode = wrap_number(encode, UC_LOWER, UC_UPPER)
            else:
                encode = wrap_number(encode, LC_LOWER, LC_UPPER)
            encoded_text += chr(encode)
        else:
            encoded_text += symbol
    return encoded_text

# calls encode with negative key to give back original text
def decode(text, key):
    return encode(text, -key)

# default mode if no arguments passed in
prompt = '''What would you like to do?
Options:
1. encode(e)
2. decode(d)
'''

if len(sys.argv) == 1:
    mode = input(prompt).lower()
    mode_encode = ['1', 'encode', 'e']
    mode_decode = ['2', 'decode', 'd']

    if mode in mode_encode:
        plain_text = input('Enter text you wish to encode: ')
        key = int(input('Enter key you want to use: '))
        print(encode(plain_text, key))

    if mode in mode_decode:
        plain_text = input('Enter text you wish to decode: ')
        key = int(input('Enter key you want to use: '))
        print(decode(plain_text, key))

# get user arguments if passed in
else: 
    parser = argparse.ArgumentParser(description='caeser cipher encoder/decoder')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encode', action='store_true', help='encode text')
    group.add_argument('-d', '--decode', action='store_true', help='decode text')
    parser.add_argument('-v', '--verbose', action='store_true', help='add verbosity')
    parser.add_argument('text', help='the text to be encoded/decoded')
    parser.add_argument('key', type=int, help='the key for encoding/decoding')
    args = parser.parse_args()

    output = ''
    if args.encode:
        output = encode(args.text, args.key)
    elif args.decode:
        output = decode(args.text, args.key)

    if args.verbose:
        print('input: {}\nkey: {}\noutput: {}'.format(args.text, args.key, output))
    else:
        print(output)
