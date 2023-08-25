import random

def encode(word):
    '''gives us the encoded version of the code language'''

    if len(word) >= 3:

        first = word[0]
        new = word[1:] + first
        random_char = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=3))
        encoded = random_char + new + random_char
        return encoded
    
    else:
        return word[::-1]
    
def decode(encoded):
    '''gives us the decoded version of the code language'''

    if len(encoded) < 6:  
        return encoded[::-1]
    
    else:
        random_chars = encoded[:3]
        new_word = encoded[3:-3]
        first_letter = new_word[-1]
        decoded_word = first_letter + new_word[:-1]
        return decoded_word  

def main():
    """giving the choice to decode or encode the message"""

    choice = input("Do you want to code or decode? (c/d): ").lower()

    if choice == 'c':
        message = input("Enter the message you want to encode: ")
        encoded = encode(message)
        print("Encoded message:", encoded)


    elif choice == 'd':
        encoded = input("Enter the message you want to decode: ")
        decoded = decode(encoded)
        print("Decoded message:", decoded)


    else:
        print("Invalid choice. Please enter 'c' for coding or 'd' for decoding.")

if __name__ == "__main__":
    main()        
