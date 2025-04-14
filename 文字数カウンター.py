while True:
    letter = input("文字列を入力: ").upper()

    if len(letter) <= 100:
        break
    else:
        print('文字数オーバーです。もう一度入力してください。')

print(len(letter))
print('百文字以内です')
