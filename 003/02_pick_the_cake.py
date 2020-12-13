cakes = [
    '딸기케이크',
    '오뎅',
    '참치김밥',
    '홍차케이크',
    '초코케이크',
    '와사비김밥',
    '멸치김밥'
]

# 케이크의 갯수
num_cake = 0

# 김밥의 갯수
num_gimbab = 0


for cake in cakes:
    if '케이크' in cake:
        num_cake = num_cake + 1
    if '김밥' in cake:
        num_gimbab = num_gimbab + 1

print('케이크의 갯수 ->')
print(num_cake)

print('김밥의 갯수 ->')
print(num_gimbab)

# 참고
# if '케이크' in '딸기케이크':
#     print('케이크입니다')
