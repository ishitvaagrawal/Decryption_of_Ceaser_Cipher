input_file = "Cipher.txt"
output_file = "Recover.txt"
key = int(input("Enter the key: "))
decrypted_text = ""

with open(input_file, "r") as file:
    encrypted_text = file.read()

for ch in encrypted_text:
    if ch.isalpha():
        if ch.islower():
            ch = chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
        elif ch.isupper():
            ch = chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
    elif ch.isdigit():
        ch = chr((ord(ch) - ord('0') - key) % 10 + ord('0'))

    decrypted_text += ch

with open(output_file, "w") as file:
    file.write(decrypted_text)

print("Decryption complete. Check", output_file)