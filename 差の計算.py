user_input = input("ビット列を入力＝＞ ")

def compare_bits(user_input):
    key = "0101110101100100111101011000011011100001"
    result = ""

    for i in range(len(user_input)):
        if user_input[i] != key[i]:
            result += "0"
        else:
            result += "1"

    return result

output = compare_bits(user_input)
print("結果:", output)
