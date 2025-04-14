key = {chr(i + 65): format(i + 1, '05b') for i in range(26)}

crypt = input("文字列を入力: ").upper()

output = ""


for char in crypt:
    if char in key:
        output += key[char]
    else:
        print(f"無効な文字が含まれています: {char}")
        break

def split_string(output):
    return [output[i:i+5] for i in range(0, len(output), 5)]

result = split_string(output)
print(result)
