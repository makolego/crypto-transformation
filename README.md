import time

key = {chr(i + 65): format(i + 1, '05b') for i in range(26)}

def compare_bits(output):
    key = "010111010110010011110101100001101110000101011101011001001111010110000110111000010101110101100100111101011000011011100001" * 6
    result = ""
    for i in range(len(output)):
        if output[i] != key[i]:
            result += "0"
        else:
            result += "1"
    return result

while True:
    continuethecrypto = input('暗号化しますか？ y or n＝＞').upper()
    if continuethecrypto == 'N':
        print('終了します。')
        break
    elif continuethecrypto != 'Y':
        print("YかNで答えてください。")
        continue

    while True:
        crypto = input("文字列を入力: ").upper()
        if len(crypto) <= 120:
            break
        else:
            print('文字数オーバーです。もう一度入力してください。')

    output = ""

    for char in crypto:
        if char in key:
            output += key[char]
        else:
            print(f"無効な文字が含まれています: {char}")
            output = ""
            break

    if output == "":
        continue

    shuturyoku = compare_bits(output)

    time.sleep(0.5)
    print("・")
    time.sleep(0.5)
    print("・")
    time.sleep(0.5)
    print("・")
    time.sleep(0.5)
    print("変換結果:", shuturyoku)
    time.sleep(0.3)
