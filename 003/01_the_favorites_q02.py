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

# 먼저, 반복을 위해 총 배열 내 원소의 갯수를 구합니다.
num_people = len(favorites)

# 떡볶이를 좋아하는 사람의 명수
num_toppoki = 0

# 반복문 시작
for position in range(num_people):
    # 반복문 내에서 배열 안의 position 번째의 사람을 가져온다.
    person = favorites[position]
    # 각각의 사람이 선택한 음식을 가져와 pick_food 변수에 저장한다.
    pick_food = person['pick']
    # 각각의 사람의 이름을 가져와 person_name 변수에 저장한다.
    person_name = person['name']
    # 각각의 사람이 선택한 음식의 컴포넌트를 가져와 pick_detail 변수에 저장한다.
    pick_detail = person['detail']

    # 떡볶이를 좋아하면서, 컴포넌트 메추리알을 좋아한다면 -> 사람 이름을 출력한다.
    if pick_food == '떡볶이' and pick_detail == '메추리알':
        print(person_name)