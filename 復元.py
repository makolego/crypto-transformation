# 復元

# 0,1を戻す　→　五個ずつ区切る　→　対応表に基づいて変換　→　出力

'''
restore_bits = 復元するビット列
xor_decrypt = XORで復元されたビット列
xor_decrypt_slise = XORで復元されたビット列を5文字づつに区切ったもの
crypto_keys = 暗号鍵の辞書
restored_bits = ローマ字に変換したビット列
'''


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
