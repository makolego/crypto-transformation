#PairwiseCipher

import time  # おまじない
import sys   # おまじない

# 暗号化用鍵
key_dict = {chr(i + 65): format(i + 1, "05b") for i in range(26)}
# 復元用鍵
reverse_key_dict = {v: k for k, v in key_dict.items()}

# 暗号鍵（ビット列に基づく処理）
def compare_bits(output):
    key = (
        "010111010110010011110101100001101110000101011101011001001111010110000110111000010101110101100100111101011000011011100001"
        * 6
    )
    return "".join(["1" if output[i] == key[i] else "0" for i in range(len(output))])

#PWCの暗号鍵
def custom_xor(shuturyoku):
    # 2ビットずつスライドしてペアに分ける
    pairs = [shuturyoku[i:i+2] for i in range(0, len(shuturyoku) - 1, 2)]

    # 各ペアに対応する値をリストで保存
    output = []
    for pair in pairs:
        if pair == '00':
            output.append(2)
        elif pair == '01':
            output.append(0)
        elif pair == '10':
            output.append(1)
        elif pair == '11':
            output.append(3)

    # 最後に1文字だけ残っている場合
    if len(shuturyoku) % 2 == 1:
        last_char = shuturyoku[-1]
        if last_char == '1':
            output.append(4)
        elif last_char == '0':
            output.append(5)

    return ''.join(map(str, output))


while True:

    while True:

        startthecrypto = input("起動しますか？ Y or N＝＞").lower()

        if startthecrypto in ["y"]:
            break
        elif startthecrypto in ['n']:
            sys.exit()
        else:
            print("Y か N で答えてください")

    # 暗号化と復元どちらを行うか
    while True:
        startthecrypto = input("暗号化、復元どちらを行いますか？＝＞").lower()
        if startthecrypto in ["hukugen", "fukugen", "angouka", "anngouka"]:
            break
        else:
            print("angoukaかhukugenで答えてください。")

    # 暗号化モード
    if startthecrypto in ["angouka", "anngouka"]:
        while True:
            crypto = input("暗号化したい文字列を入力: ").upper()
            if len(crypto) <= 120:
                break
            else:
                print("文字数オーバーです。もう一度入力してください。")

        output = ""
        for char in crypto:
            if char in key_dict:
                output += key_dict[char]
            else:
                print(f"無効な文字が含まれています: {char}")
                output = ""
                break

        if output == "":
            print("変換に失敗しました。")
        else:
            shuturyoku = compare_bits(output)

    result = custom_xor(shuturyoku)
    print(result)

# 復元モード
if startthecrypto in ["hukugen", "fukugen"]:
        #XOR復元プログラム
    def restorat_bits(restore_bits):
        #鍵の設定
        key = "0101110101100100111101011000011011100001" * 20
        #0,1を変換す
        return ''.join(['1' if restore_bits[i] == key[i] else '0' for i in range(len(restore_bits))])

    #入力された文字がビット列かを検証
    while True:
        #ビット列を入力
        restore_bits = input('復元するビット列を入力 ＝＞')
        #入力されたものがビット列かを検証
        if len(restore_bits) % 1 == 0 and set(restore_bits).issubset({"0","1"}):
            break
        else:
            print('ビット列を入力してください(例:000010001000011)')

    xor_decrypt = restorat_bits(restore_bits)

    def split_by_five(xor_decrypt):
        return [xor_decrypt[i:i+5] for i in range(0, len(xor_decrypt), 5)]

    xor_decrypt_slise = split_by_five(xor_decrypt)

    crypto_keys = {

        "00001": "a", "00010": "b", "00011": "c", "00100": "d", "00101": "e",
                "00110": "f", "00111": "g", "01000": "h", "01001": "i", "01010": "j",
                "01011": "k", "01100": "l", "01101": "m", "01110": "n", "01111": "o",
                "10000": "p", "10001": "q", "10010": "r", "10011": "s", "10100": "t",
                "10101": "u", "10110": "v", "10111": "w", "11000": "x", "11001": "y", "11010": "z",
            }

    restored_bits = "".join([crypto_keys.get(code, "？") for code in xor_decrypt_slise])

    print(restored_bits)
