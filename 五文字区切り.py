moji = input("文字を入力＝＞")

def split_string(moji):
    return [moji[i:i+30] for i in range(0, len(moji), 30)]

result = split_string(moji)
print(result)
