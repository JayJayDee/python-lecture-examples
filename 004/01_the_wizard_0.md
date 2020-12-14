# Quiz 01. The Wizard

사람 5명이 위자드 라고 하는 카드게임을 하러 모였습니다. 간소하게 약 8 라운드의 트릭들을 진행했고, 게임의 결과를 다음과 같이 `Array` 로 나타내었습니다. 

```python
game_result = [
    { 'round': 1, 'name': 'JD', 'score': -10 },
    { 'round': 1, 'name': 'YE', 'score': 20 },
    { 'round': 1, 'name': 'HW', 'score': 0 },
    { 'round': 1, 'name': 'CO', 'score': 20 },
    { 'round': 1, 'name': 'LS', 'score': 10 },
    { 'round': 2, 'name': 'JD', 'score': 20 },
    { 'round': 2, 'name': 'YE', 'score': 30 },
    { 'round': 2, 'name': 'HW', 'score': 10 },
    { 'round': 2, 'name': 'CO', 'score': 5 },
    { 'round': 2, 'name': 'LS', 'score': 0 },
    { 'round': 3, 'name': 'JD', 'score': 20 },
    { 'round': 3, 'name': 'YE', 'score': 20 },
    { 'round': 3, 'name': 'HW', 'score': 10 },
    { 'round': 3, 'name': 'CO', 'score': 5 },
    { 'round': 3, 'name': 'LS', 'score': 0 },
    { 'round': 4, 'name': 'JD', 'score': -10 },
    { 'round': 4, 'name': 'YE', 'score': 20 },
    { 'round': 4, 'name': 'HW', 'score': -10 },
    { 'round': 4, 'name': 'CO', 'score': 10 },
    { 'round': 4, 'name': 'LS', 'score': 10 }
]
```

`Array` 내의 `Dictionary` 내에서 `round` 는 게임의 라운드 수를 의미합니다.  예를들어 `'round': 1` 이라면 1라운드의 결과입니다. `name` 은 플레이어의 이름입니다. `score`는 해당 라운드에서 획득한 점수입니다. 

## 질문들

다음의 질문들을 파이썬 코드로 답할 수 있도록 작성해 보세요.

- 플레이어 `YE` 의 총 점수 합은 얼마인가요?
- 모든 라운드를 통틀어 점수를 20점 **이상** 획득한 사람들을 모두 출력해보세요.
- 플레이어 `JD` 의 평균 점수는 얼마인가요?

## 다음시간에 할 것들

반드시 할 필요는 없지만 고민해 보면 큰 도움이 될 거예요.

- 이 게임의 최종 승자의 이름을 출력해 보세요.
- 각 플레이어들의 평균 점수를 출력해 보세요.