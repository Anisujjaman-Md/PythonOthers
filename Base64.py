import base64

def encode(message):
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def decode(message):
    message_bytes = message.encode('ascii')
    string_bytes = base64.b64decode(message_bytes)
    return string_bytes.decode('ascii')

def main():  
    message = input("Enter a message: ")
    
    encode_string = int(input("Enter 1 for encode or 2 for decode: "))
    if encode_string == 1:
        print("Encoded Base64 String is:", encode(message))
    elif encode_string == 2:
        print("Decoded from Base64 To String is:", decode(message))
    else:
        print("Invalid input")
main()