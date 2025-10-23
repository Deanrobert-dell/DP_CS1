#DP 2nd ceasar code
#list of letters to be used
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#function with shift and code type
#also add + shift and -shift for decode/encode
def caesar(text, shift, code):
    result = ""
    text = text.upper()

    for char in text:
        if char in letters:
            index = letters.index(char)
            if code == "encode":
                new_index = (index + shift) %26
            else:
                new_index = (index - shift) %26
            result += letters [new_index]
        else:
                result += char
    return result
    


#message to be decoded or encoded use 1 and 2 for input
code = input("enter message: ") 
question = input("do you want to encode (1) or decode (2)")
#if statement to determine encode or decode and print results
if question == "1":
    shift = int(input("Enter shift number: "))
    print("Encoded message:", caesar(code, shift, "encode"))
elif question == "2":
    shift = int(input("Enter shift number: "))
    print("Decoded message:", caesar(code, shift, "decode"))
else:
    print("Invalid option.")









