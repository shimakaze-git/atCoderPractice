input_num = int(input())

count = 0
# 1と0以外が混ざっている場合は終了する
for i in str(input_num):
    # 1がある値をカウントアップ
    if int(i) == 1:
        count += 1

print(count)
