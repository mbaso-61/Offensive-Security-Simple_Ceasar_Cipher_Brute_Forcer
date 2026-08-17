def ceasarBruteFrocer(ciphertext):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for shift in range(1, 26):
        decrypted = ""

        for char in ciphertext:
            if char.lower() in alphabet:
                index = alphabet.index(char.lower())
                new_index = (index - shift) % 26
                new_char = alphabet[new_index]

                # Preserve uppercase
                decrypted += new_char.upper() if char.isupper() else new_char
            else:
                decrypted += char

        print(f"Shift {shift:2}: {decrypted}")

text = input("Encrypted text: ")
print(ceasarBruteFrocer(text))

text = input("Encrypted text: ")

for shift in range(26):
    result = ""

    for char in text:
        if char.isalpha():
            result += chr((ord(char.lower()) - ord('a') - shift) % 26 + ord('a'))
        else:
            result += char

    print(shift, result)
