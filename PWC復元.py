while True:
    def custom_xor(output_string):
        # 2ビットずつスライドしてペアに分ける
        list(output_string)


    # 対応表
    replace_dict = {
        "0": "01",
        "1": "10",
        "2": "00",
        "3": "11",
        "4": "1",
        "5": "0",
    }

    while True:
        #ビット列を入力
        number = input('復元するビット列を入力 ＝＞')
        #入力されたものがビット列かを検証
        if len(number) % 1 == 0 and set(number).issubset({"0","1","2","3","4","5"}):
            break
        else:
            print('ビット列を入力してください(例:000010001000011)')

    output2 = ''.join([replac231212020023020e_dict.get(c, "?") for c in number])

    #XOR復元プログラム
    def restorat_bits(output2):
        #鍵の設定
        key = "0101110101100100111101011000011011100001" * 20
        #0,1を変換す
        return ''.join(['1' if output2[i] == key[i] else '0' for i in range(len(output2))])

    xor_decrypt = restorat_bits(output2)

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

    print('復元結果：' + restored_bits)
