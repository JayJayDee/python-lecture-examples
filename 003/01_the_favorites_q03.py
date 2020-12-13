favorites = [
    {
        'name': '나즈그렐',
        'pick': '떡볶이',
        'detail': '오뎅'
    },
    {
        'name': '리로이 젠킨스',
        'pick': '김밥튀김',
        'detail': None
    },
    {
        'name': '말퓨리온 스톰레이지',
        'pick': '순대',
        'detail': '허파'
    },
    {
        'name': '바로크 사울팽',
        'pick': '김밥튀김',
        'detail': None
    },
    {
        'name': '밀하우스 마나스톰',
        'pick': '떡볶이',
        'detail': '떡'
    },
    {
        'name': '그롬 헬스크림',
        'pick': '떡볶이',
        'detail': '메추리알'
    },
    {
        'name': '첸 스톰스타우트',
        'pick': '순대',
        'detail': '간'
    },
    {
        'name': '바리안 린',
        'pick': '치즈돈까스',
        'detail': None
    },
    {
        'name': '볼진',
        'pick': '돈까스',
        'detail': None
    },
    {
        'name': '실바나스 윈드러너',
        'pick': '참치김밥',
        'detail': None
    },
    {
        'name': '가로쉬 헬스크림',
        'pick': '오뎅',
        'detail': None
    },
    {
        'name': '아서스 메네실',
        'pick': '소고기김밥',
        'detail': None
    }
]

# 반복문 시작
for person in favorites:

    # 각각의 사람이 선택한 음식을 가져온다
    pick_food = person['pick']

    # 각각의 사람의 이름을 가져온다
    person_name = person['name']

    # 만약 현재 사람이 선택한 음식에 '김밥' 이라는 글자가 있다면 ->
    # if '김밥' in pick_food:
    #     print(person_name + ' -> ' + pick_food)

    # 만약 현재 사람의 이름에 '헬스크림' 이라는 글자가 있다면 ->
    if '헬스크림' in person_name:
        print(person_name)
        print(pick_food)
        print('-----')