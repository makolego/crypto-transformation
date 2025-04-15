while True:
    def custom_xor(input_string):
        # 2ビットずつスライドしてペアに分ける
        pairs = [input_string[i:i+2] for i in range(0, len(input_string) - 1, 2)]

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
        if len(input_string) % 2 == 1:
            last_char = input_string[-1]
            if last_char == '1':
                output.append(4)
            elif last_char == '0':
                output.append(5)

        return ''.join(map(str, output))

    while True:
        input_string = input('暗号化するビット列を入力 ＝＞')
        #入力されたものがビット列かを検証
        if len(input_string) % 1 == 0 and set(input_string).issubset({"0","1"}):
            break
        else:
            print('ビット列を入力してください(例:000010001000011)')

    result = custom_xor(input_string)
    print(result)


