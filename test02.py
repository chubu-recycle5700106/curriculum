while True:
    try:
        print()
        print('1: ValueError例外を発生')
        print('2: IndexError例外を発生')
        print('3: 例外を発生させない')
        print('4: 終了')
        number = int(input('選択してください。: '))
        # 問①：if文を用いて、以下の画像のように処理されるように記述しましょう。
    
        if number == 1:
            print('↓')
            print('Value Error')
            print('invalid literal for int() with base 10: 1')
            print('↓')
            print('もう一度選択しましょう')
            continue

        elif number == 2:
            print('↓')
            print('Index Error')
            print('string index out of range')
            print('↓')
            print('もう一度選択しましょう')
            continue

        elif number == 3:
            print('↓')
            print('例外を発生させませんでした')
            print('↓')
            print('もう一度選択しましょう')
            continue

        elif number == 4:
            print('↓')
            print('終了します')
            break
    
    # 問②：else節を用いて、以下の画像のように処理されるように記述しましょう。
        else :
           print('↓')
           print('終了します')
           break

    except ValueError as e:
        print(e.args)

print('↓')
print('無限ループを終了します')