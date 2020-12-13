given_number = 111

# 나머지가 없는 수의 갯수
num_divided = 0

# 1부터 given_number 까지 반복
for number in range(1, given_number + 1):
    # given_number를 number로 나눈 나머지
    divided = given_number % number
    # 만약, 나머지가 0이라면 -> num_divided 숫자를 1 증가시킨다
    if divided == 0:
        num_divided = num_divided + 1

# 만약 완전히 나눠떨어진 수의 갯수가 2개라면, 소수의 정의에 따라 이 숫자는 소수이다.
if num_divided == 2:
    print('소수 입니다')

# 아닌 경우, 이 숫자는 합성수이다.
else:
    print('소수가 아닙니다')
