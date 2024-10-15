from morse_alphabet import morse_code

is_on = True

while is_on:
    text = input("\nText: ").lower()
    if text == "#":
        is_on = False
    else:
        for letter in text:
            print(f"{morse_code[letter]}", end=" ")
