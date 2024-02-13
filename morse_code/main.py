import art
import morse


def code_generator(start_text):
    coded_text = ""
    for char in start_text:
        if char in morse.code:
            coded_char = morse.code[char]
            coded_text += coded_char
            coded_text += " "
        elif char == " ":
            coded_text += "       "
        else:
            continue
    print(f"Here's the coded result: {coded_text}")


print(art.logo)
restart = True

while restart:
    text = input("Welcome to the morse code generator!\nPlease type the message you would like to encode: ").lower()
    code_generator(text)
    again = input("Type 'yes' if you want to encode another message, otherwise type 'no'. ").lower()
    if again != "yes":
        restart = False
        print("Goodbye\n−−· −−− −−− −·· −··· −·−− ·")
