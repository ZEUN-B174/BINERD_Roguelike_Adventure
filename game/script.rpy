﻿# 이 파일에 게임 스크립트를 입력합니다.

# 파이썬 코드
init python:
    import random
    from dataclasses import dataclass

    # 플레이어 스테이터스
    MaxHP = 100 # 최대체력
    Hp = 100 # 현재체력
    Atk = 20 # 공격력
    Def = 10 # 방어력
    Qui = 10 # 민첩도
    ether = 200 # 에테르

    # 초기화 안되는 소모품
    etherium = 0 # 에테리움

    # 적 스테이터스
    enemyMaxHP = 100 # 적 최대체력
    enemyHp = 100 # 적 현재체력
    enemyAtk = 20 # 적 공격력
    enemyDef = 10 # 적 방어력
    enemyQui = 10 # 적 민첩도
    enemyEliment = "" # 적 속성

    # 기타
    MAX_DMG = 2147483647
    
    #시스템
    area1 = "1" # 구역 1 목적지
    area2 = "2" # 구역 2 목적지
    area3 = "3" # 구역 3 목적지
    AreaList = ["전투", "사건", "보상", "정예", "상점"]
    togo = "none" # 목적지 저장 변수

    dream1 = "a" # 사건 1 목적지
    dream2 = "b" # 사건 2 목적지
    dream3 = "c" # 사건 3 목적지

    DreamList = ["이세계 은행", "메루디스탄", "룰렛 TV쇼", "드림랜드", "???"]
    NoMeru = ["이세계 은행", "룰렛 TV쇼", "드림랜드", "???"]

    todream = "none" # 사건 선택지 저장 변수
    damage = "" # 대미지 표시를 깔끔하게 하기 위한 변수

    #선택지 중복 방지용
    dreamed1 = False
    dreamed2 = False
    dreamed3 = False

    floor = 1 # 층 수
    areanum = 0 #구역 번호
    dice = 0 # 랜덤이벤트에 쓸 주사위
    HowManyWay = 0 # 꿈 선택지 숫자 정하기용
    mode = "none" # 게임모드
    
    ###### 적
    @dataclass
    class Enemy:
        name: str # 이름
        ele: str # 속성
        max_hp: int = 100 # 최대체력
        hp: int = 100 # 현재체력
        attack: int = 20 # 공격력
        defence: int = 10 # 방어력
        qui: int = 10 # 민첩도

    # 적 정의
    slime = Enemy(
        name = "도트 슬라임",
        ele = "디지털",
        attack = 10,
        defence = 5,
        qui = 5
    )

    ###### 버프
    @dataclass
    class Buff:
        name: str # 버프 이름
        script: str # 버프 설명
        effect: str # 버프 효과
        own: bool = False # 버프을 소유하고 있는지 판단

    # 아이템 템플릿

    #버프이름 = Buff(
    #    name = "버프이름",
    #    script = "버프설명",
    #    effect = "버프 효과"
    #)
    
    ###### 아이템
    @dataclass
    class Item:
        name: str # 아이템 이름
        script: str # 아이템 설명
        effect: str # 아이템 효과
        type_i: str # 아이템 종류
        own: bool = False # 아이템을 소유하고 있는지 판단

    # 아이템 정의
    dreamcatcher = Item(
        name = "드림캐쳐",
        script = "신비로운 문양의 드림캐쳐. 악몽 속성 적에게 가하는 피해가 20% 증가한다.",
        type_i = "일반",
        effect = "버프"
    )

    musicbox = Item(
        name = "미분음 오르골",
        script = "12음계에서 벗어난 신비한 음을 연주하는 오르골. 꿈 계열 아이템의 효과가 2배가 된다.",
        type_i = "일반",
        effect = "버프"
    )

    hpEnhancer = Item(
        name = "체력 증진기 #22",
        script = "다스니 연구소의 체력계 아이템. 전투 진입 시, 체력이 2배가 된다.",
        type_i = "일반",
        effect = "버프"
    )

    WalletWarrior = Item(
        name = "지갑전사",
        script = "다스니 연구소의 게임계 아이템. 에테르에 비례해서 공격력이 증가한다.",
        type_i = "일반",
        effect = "버프"
    )

    sample009 = Item(
        name = "꿈바다 샘플 #009",
        script = "연구소에서 체취한 꿈의 일부. 전투 시 일정 확률로 파괴되며, 파괴될 시 기이한 꿈을 꿀 수 있다.",
        type_i = "파괴 가능 아이템",
        effect = "미묘한 아이템"
    )

    regularSword = Item(
        name = "정기점검",
        script = "다스니 연구소의 게임계 아이템. 짝수 턴마다 공격력이 20% 증가한다.",
        type_i = "일반",
        effect = "버프"
    )

    tempSword = Item(
        name = "임시점검",
        script = "다스니 연구소의 게임계 아이템. 사용 시, 공격력이 30% 증가한다. 3번 사용 가능하며, 2턴동안 지속된다.",
        type_i = "파괴 가능 아이템",
        effect = "버프"
    )

    extendSword = Item(
        name = "연장점검",
        script = "다스니 연구소의 게임계 아이템. 20턴이 넘어갈 시, 공격력이 40 증가한다.",
        type_i = "일반",
        effect = "버프"
    )

    emergSword = Item(
        name = "긴급점검",
        script = "다스니 연구소의 게임계 아이템. 사용 시, 공격력이 200% 증가한다. 단 1턴동안 지속된다.",
        type_i = "파괴 가능 아이템",
        effect = "버프"
    )

    # 아이템 템플릿

    #아이템이름 = Item(
    #    name = "아이템이름",
    #    script = "아이템설명",
    #    type_i = "아이템 특성",
    #    effect = "아이템 효과"
    #)

    itemlist = [dreamcatcher, musicbox, hpEnhancer, WalletWarrior, sample009]

    # 기타 코드
    meru_process = 1 # 메루디스탄 사건 진척도.

    ###### 함수

    # 랜덤 뽑기
    def get_random(object_list):
        # 뽑을 거리가 하나라도 있는지 검증
        for i in object_list:
            if i.own == True:
                obj = "null"
            else:
                obj = 1
                break
        # 뽑을 거리가 있을 때, 없는 것 중에서 뽑기
        if obj == 1:
            obj = random.choice(object_list)
            while obj.own == True:
                obj = random.choice(object_list)
            obj.own = True
        return obj

    # 아군 대미지 계산식(나에게 가해지는 대미지)
    def get_myDamage():
        # 공격 회피
        chance = Qui - enemyQui
        dice = random.randint(1, 100)
        if dice <= chance:
            return "회피"
        else:
            # 대미지 계산
            return min(enemyAtk*(1/(1 + Def)), MAX_DMG)

    # 적 대미지 계산식(적에게 가해지는 대미지)
    def get_enemyDamage():
        # 공격 회피
        chance = enemyQui - Qui
        dice = random.randint(1, 100)
        if dice <= chance:
            return "회피"
        else:
            # 대미지 계산
            return min(Atk*(1/(1 + enemyDef)), MAX_DMG)

# 렌파이 코드
init:
    screen stat():
        frame:
            xpadding 50
            ypadding 50
            xpos 150
            ypos 150
            grid 1 7:
                text '체력'
                bar value StaticValue(Hp, MaxHP) xalign 0.5 xsize 600
                text '공격력: [Atk]'
                text '방어력: [Def]'
                text '에테르: [ether]'
                text "[floor]차원"
                text "[areanum]구역"

# image 문을 사용해 이미지를 정의합니다.

# 배경 이미지
image room = "room_edited.png"
image bg1 = "dreamspace.jpg"
image bg2 = "spaceship.jpg"
image bg3 = "stars.jpg"
image bank = "bank.jpg"
image amste = "amsterdam.jpg"
image tvshow = "tv_show.jpg"

# 다스니 박사 이미지
image perwin = "Perwin.png"

# 주인공 이미지
image tester normal = "Tester_default.png"
image tester nonex = "Tester_0-0.png"
image tester smile = "Tester_smile.png"
image tester surpriesd = "Tester_surprised.png"
image tester confident = "Tester_UU.png"
image tester injang = "Tester_-w-.png"
image tester wut = "Tester_wut.png"
image tester curious = "Tester_curious.png"

# 메루 이미지
image meru normal = "Meru_default.png"
image meru confident = "Meru_UU.png"
image meru injang = "Meru_-w-.png"
image meru merong = "Meru_merong.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character('페르윈 다스니', color="#fcb714")
define a = Character('Mîxayîl', color="#514ed7")
define na = Character("[name]", color="#565274")
define ny = Character('니알리', color="#c5293e")

define m = Character('「메루」', color="#7c4dff")
define m3ru = Character(who_bold=True, what_italic=True, what_color="#7c4dff", what_font="Caveat-VariableFont_wght.ttf", what_size=100)
define ezdan = Character('야즈단', what_italic=True, color="#7c4dff")

# 여기에서부터 게임이 시작합니다.
label start:

    $ name = renpy.call_screen("set_name",title="여기에 이름을 입력하면 돼.", init_name="테스터")
    scene room with dissolve

    play music "Evening of Tel Aviv.mp3"
    show tester nonex at right with easeinright
    show perwin at left

    na "안녕하세요, 페르윈 씨.{w=.7} 이메일 보고 관심이 생겨서 와 봤어요."

    p "비 디트나 테 케프흐웨스 붐, 투 호르테 지 코레예 이, 라스트?"

    show tester wut
    na "?"

    p "..."
    show tester injang
    p "미안, 번역기가 작동 안하고 있었어."
    show tester normal
    p "어쨌든. 꽤 빨리 왔네.{w=.7} 머나먼 한국 땅에서 여기까지 올려면 꽤 힘들었을 텐데."
    p "먼저 내 시뮬레이션부터 소개해줄게."
    p "혹시 로그라이크라고 들어봤어?"
    show tester nonex

    menu:
        na "로그라이크라..."
        "들어봤어요.":
            show tester confident
            p "그럼 자세한 설명은 필요 없겠네."
        "못 들어봤어요.":
            show tester injang
            p "아, 설명하기 귀찮은데."
            p "그래도 말 안해주면 엄청 헷갈릴 테니까 잘 들어."
            p "로그라이크는 간단히 말해서, 던전 탐험을 하면서 아이템을 얻고, 적과 싸우고, 보스를 처치하는 게임이야."
            p "대부분의 로그라이크는 던전이 랜덤으로 생성되고, 적도 랜덤으로 나오고, 아이템도 랜덤으로 나와."
            p "이런 요소가 로그라이크의 매력이기도 하지."
            p "뭐 딱히 더 자세하게 설명 안해도 될테니까 이정도에서 넘어갈게."

    show tester normal
    p "어쨌든 이걸 물어본 이유가 내가 만든 시뮬레이션이 로그라이크의 요소를 채용해서 그렇거든."
    p "내 시뮬레이션은 간단해.{w=.7} 다양한 방을 지나면서 각종 버프를 얻어 보스몹을 물리치는 게 목표야."
    p "아마 호요버스에서 만든 붕괴: 스타레일의 시뮬레이션 우주와 비슷할거야.{w=.7} 사실 거기서 영감을 얻어서 만들었거든."
    p "크흠, 아무튼!{w=.7} 시작하게 되면 넌 3개의 구역 중 하나로 들어갈 수 있어."
    p "내 시뮬레이션에는 여러 가지의 구역이 있는데, 낮은 난이도의 전투를 할 수 있는 전투 구역과 다양한 사건이 발생하는 사건 구역이 있어."
    
    show tester curious
    na "구역이 그거 두 개밖에 없나요?"
    show tester normal

    p "그건 아니야."
    p "상점 구역이나 정예 구역, 보상 구역도 있어."
    p "시뮬레이션 들어가면 설명 다 나오니까, 내가 설명 안해줬다고 걱정하지 말고."
    
    show tester confident
    na "알겠어요."
    show tester normal

    p "다음으로 전투에 대해서 설명해줄게."
    p "대미지는 간단하게 공격력에서 방어력을 뺀 만큼 들어가.{w=.7}..게 할 예정이었는데 아무래도 대미지가 아예 안들어가는게 좀 거시기해서 말이지."
    p "현재 쓰는 식은 이거야.{p=.7}대미지 = 공격력*(1/(1+방어력))"
    p "뭐, 어차피 공식이 중요한 게 아니라 이정도에서 넘어갈게."
    p "이제 에테르에 대해서 설명해줄게."
    p "에테르는 내 시뮬레이션에서 사용하는 재화야."
    p "거래 구역에서 상품을 구매하거나, 「어떤 아이템」 에서 중요하게 쓰이기도 하지."
    
    show tester curious
    na "그 아이템이 뭔가요?"
    show tester normal

    p "그건 비밀!"
    p "음, 이정도 설명했으면 쉽게 깰 수 있을거야."
    p "힘내!"
    show tester wut
    hide perwin with easeoutleft

    show tester at center with ease
    na "..."
    show tester injang
    na "뭐, 어떻게든 되겠지."
    stop music fadeout 1.0

label Tutorial:
    scene bg1 with dissolve
    a "다스니 박사님의 시뮬레이션에 오신 걸 환영합니다."
    a "저는 박사님의 AI 조수, Mîxayîl(미하일)입니다."
    a "박사님이 마저 하지 못한 설명은 제가 해드릴테니 걱정하지 마세요."
    show screen stat
    a "이건 게임에 들어가면 보이는 당신의 능력치를 나타낸 상태창이랍니다."
    a "상단에는 체력과 공격력, 방어력, 에테르가 보이고, 하단에는 현재 층과 구역이 보입니다."
    hide screen stat
    a "이건 이쯤에서 넘어가고, 다음으로 박사님이 제대로 말하지 않은 구역에 대해서 설명해드릴게요."
    a "상점 구역: 에테르를 소비해 원하는 아이템이나 버프를 구매할 수 있습니다."
    a "정예 구역: 전투 구역보다 더 강한 적을 마주치고, 보상도 전투 구역보다 더 많이 나옵니다."
    a "보상 구역: 사건 구역과 비슷하지만, 더 좋은 보상이 나오고, 안좋은 사건은 뜨지 않습니다."
    a "이것 외에도 전설로만 여겨지는 미개척 구역이 있긴 한데...{w=.7} 이건 거의 볼 일이 없을 테니 신경 안쓰셔도 됩니다."
    a "일단 어느정도 감을 잡으셨을 테니 시작해봐요."
    a "일단, 스토리 모드를 먼저 플레이해보세요."
    menu:
        "무엇을 하실 건가요?"
        "스토리 모드":
            $ mode = "tutorial"
            jump MainGame
# 이곳은 튜토리얼의 끝입니다.

label StandBy:
    hide screen stat
    python:
        areanum = 0
        floor = 1
        ether = 200
        if meru_process == "done":
            meru_process = 1
        for ait in itemlist:
            ait.own = False
    
    scene bg1 with dissolve
    menu:
        "무엇을 하실 건가요?"
        "스토리 모드":
            $ mode = "story"
            jump MainGame
        "무한 모드":
            $ mode = "infinite"
            jump MainGame
        "쿠르드어 모드":
            $ mode = "kurdi"
            jump MainGame
# 이곳은 메인화면의 끝입니다.

label MainGame:
    scene bg1 with dissolve
    show screen stat
    if mode == "tutorial":
        a "시뮬레이션으로 제대로 들어오셨군요."
        a "처음 시뮬레이션으로 들어오면 버프 3개와 아이템 1개를 기본으로 받게 된답니다."
        a "시뮬레이션은 혼자 돌아다니기엔 위험하니 이걸 챙기길 바라요."
    jump select3
# 이곳은 로딩화면의 끝입니다.

label report:
    $ solid_ether = ether // 10
    "[ether]에테르 >> [solid_ether]에테리움"
    $ etherium += solid_ether
    "보고서 닫기"
    jump StandBy

label boss:
    scene bg3 with dissolve
    menu:
        "진입할 구역을 정해주세요."
        "보스전":
            jump BossBattle
# 이곳은 보스전 진입의 끝입니다.

label special:
    scene bg3 with dissolve
    menu:
        "진입할 구역을 정해주세요."
        "미개척 구역":
            jump pioneer
# 이곳은 미개척 구역 진입의 끝입니다.

label select2:
    scene bg3 with dissolve
    $ area1, area2 = random.sample(AreaList, k=2)
    menu:
        "진입할 구역을 정해주세요."
        "[area1]":
            $ togo = area1
            jump destination
        "[area2]":
            $ togo = area2
            jump destination
# 이곳은 구역 2선택의 끝입니다.

label select3:
    scene bg3 with dissolve
    $ area1, area2, area3 = random.sample(AreaList, k=3)
    menu:
        "진입할 구역을 정해주세요."
        "[area1]":
            $ togo = area1
            jump destination
        "[area2]":
            $ togo = area2
            jump destination
        "[area3]":
            $ togo = area3
            jump destination
# 이곳은 구역 3선택의 끝입니다.

label battle:
    $ areanum += 1
    scene bg2 with dissolve
    a "전투 구역에 진입했습니다."

    $ dice = random.randint(0, 1)
    if areanum == 8:
        jump boss
    elif dice == 0:
        jump select2
    else:
        jump select3
# 이곳은 전투 구역의 끝입니다.

label happening:
    $ areanum += 1
    scene bg2 with dissolve

    a "사건 구역에 진입했습니다."
    $ HowManyWay = random.randint(1, 3)
    "당신의 앞에는 [HowManyWay]갈래의 꿈으로 향하는 문이 있습니다."
    if HowManyWay == 1:
        "눈앞의 꿈으로 나아가봅시다."
    elif HowManyWay == 2:
        "당신은 어떤 꿈을 먼저 경험할 지 정해야 합니다."
    else:
        "당신은 어떤 꿈을 경험할 지 정해야 합니다."
    python:
        dreamed1 = False
        dreamed2 = False
        dreamed3 = False

        if meru_process == "done":
            dream1, dream2, dream3 = random.sample(NoMeru, k=3)
        else:
            dream1, dream2, dream3 = random.sample(DreamList, k=3)

    jump backto

# 꿈 선택지
label SelectDream1:
    scene bg1 with dissolve
    menu:
        m3ru "Gerok, pêşde herin û riya xwe hilbijêrin."
        "[dream1]" if dreamed1 == False:
            $ todream = dream1
            $ dreamed1 = True
            jump sleep

        "꿈에서 깨기" if dreamed1 == True:
            jump RoadSign

label SelectDream2:
    scene bg1 with dissolve
    menu:
        m3ru "Gerok, pêşde herin û riya xwe hilbijêrin."
        "[dream1]" if dreamed1 == False:
            $ todream = dream1
            $ dreamed1 = True
            jump sleep

        "[dream2]" if dreamed2 == False:
            $ todream = dream2
            $ dreamed2 = True
            jump sleep

        "꿈에서 깨기" if dreamed2 == True and dreamed3 == True:
            jump RoadSign

label SelectDream3:
    scene bg1 with dissolve
    menu:
        m3ru "Gerok, pêşde herin û riya xwe hilbijêrin."
        "[dream1]" if dreamed1 == False and dreamed2 == False and dreamed3 == False:
            $ todream = dream1
            $ dreamed1 = True
            jump sleep

        "[dream2]" if dreamed1 == False and dreamed2 == False and dreamed3 == False:
            $ todream = dream2
            $ dreamed2 = True
            jump sleep

        "[dream3]" if dreamed1 == False and dreamed2 == False and dreamed3 == False:
            $ todream = dream3
            $ dreamed3 = True
            jump sleep

        "꿈에서 깨기" if dreamed1 == True or dreamed2 == True or dreamed3 == True:
            jump RoadSign
# 이곳은 사건 구역의 끝입니다.

label reward:
    $ areanum += 1
    scene bg2 with dissolve
    a "보상 구역에 진입했습니다."

    $ dice = random.randint(0, 1)
    if areanum == 8:
        jump boss
    elif dice == 0:
        jump select2
    else:
        jump select3
# 이곳은 보상 구역의 끝입니다.

label EliteBattle:
    $ areanum += 1
    scene bg2 with dissolve
    a "정예 구역에 진입했습니다."

    $ dice = random.randint(0, 1)
    if areanum == 8:
        jump boss
    elif dice == 0:
        jump select2
    else:
        jump select3
# 이곳은 정예 구역의 끝입니다.

label store:
    $ areanum += 1
    scene bg2 with dissolve
    a "상점 구역에 진입했습니다."

    $ dice = random.randint(0, 1)
    if areanum == 8:
        jump boss
    elif dice == 0:
        jump select2
    else:
        jump select3
# 이곳은 상점 구역의 끝입니다.

label BossBattle:
    $ areanum += 1
    scene bg2 with dissolve
    a "보스 구역에 진입했습니다."

    python:
        areanum = 0
        floor += 1
        dice = random.randint(1, 10)
    if (floor == 3 and (dice == 4 or mode == "tutorial")):
        jump pioneer
    elif floor == 4:
        jump report
    else:
        jump select3
# 이곳은 보스 전투 구역의 끝입니다.

label pioneer:
    scene black
    hide screen stat
    $ areanum = "-2147483647"
    $ floor = "7KSR6rCE6rOE"
    a "..."
    a "ERROR: 예기치 못한 목적지에 도달-습니---"
    a "..."
    a "......"
    a "---시ㅁ-레-- -주-번역 모듈 실행..."
    a "..."
    a "......"
    a "실행 완료."
    play music "Unexplored Area.mp3" fadein 1.0
    scene bg1 with dissolve
    show screen stat
    if mode == "tutorial":
        a "미개척 구역에 처음 오신 걸 환영합니다, [name]님."
        a "이곳은 다스니 박사님도 발견하지 못한 미지의 공간으로, {p=.7}제가 여기에 도착하면서 인간이 알아볼 수 있는 형태로 정리했습니다."
        a "그렇지만 언어는 완벽하게 변환을 못 해서 [name]님이 보시기에는 구글 번역기로 어설프게 번역한 쿠르드어처럼 느껴질 거에요."
        a "대신, 여기서 발생한 사건을 다스니 박사님께 보고하시면 다음부터는 제대로 된 한국어로 보일 테니 걱정 안하셔도 됩니다."
    else:
        a "미개척 구역에 오신 걸 환영합니다, [name]님."

    $ areanum = 0
    $ floor = 3
    stop music fadeout 1.0
    jump select3
# 이곳은 미개척 구역의 끝입니다.

# 사건 구역 이벤트
label bank:
    scene black with dissolve
    "..."
    na "...은행이 이세계에 있는 한, 어쩔 수 없지."
    play music "Clockwise Clockwork (Variation).mp3"
    scene bank with dissolve
    "그렇게 당신은 말이 통하지 않는 이세계의 은행에 도착했습니다."
    "여기에서 저축한 돈 {color=#7c4dff}300에테르{/color}를 돌려받기 위해서말이죠."
    "은행 직원" "Bi xêr hatî, mişterî. Ez çawa dikarim alîkariya te bikim?"
    $ dice = random.randint(1, 10)
    menu:
        "어떻게 말해야 하지..."
        "몸짓 언어를 최대한 써서 내 의도를 설명한다.":
            if (dice <= 5):
                "은행 직원" "Ji ber vê yekê we teserûfên xwe paşde xwest."
                "은행 직원은 나에게 {color=#7c4dff}300에테르{/color}를 주었다."
                $ ether += 300
            else:
                "은행 직원" "Ma hûn dixwazin hin teserûfên xwe paşde bistînin?"
                "은행 직원은 나에게 {color=#7c4dff}100에테르{/color}를 주었다."
                $ ether += 100
        "주변에서 사람들이 하는 말을 대충 끼워맞춘다.":
            if (dice > 7):
                "은행 직원" "Ji ber vê yekê we dixwest ku teserûfên xwe plus faîzê paşde bistînin."
                "은행 직원은 나에게 {color=#7c4dff}500에테르{/color}를 주었다."
                $ ether += 500
            else:
                "은행 직원" "Ez nikarim fêm bikim ka hûn çi dibêjin."
                "은행 직원은 나에게 아무것도 주지 않았다."

    stop music fadeout 1.0
    jump backto
# 사건 1: 이세계 은행

label roulette:
    scene black with dissolve
    "..."
    na "역시, TV 프로그램에 나오길 잘한거같아."
    play music "Theater Street.mp3" fadein 1.0
    scene tvshow with dissolve
    "사회자" "신사 숙녀 여러분, 드디어 가장 재미있는 시간이 돌아왔습니다!"
    "사회자" "오늘의 우승자, [name]님은 어떤 상품을 가져가게 될까요?"
    "사회자" "[name]님, 앞의 룰렛을 돌려주세요!"

    "근데 아무리 생각해도 이 룰렛 좀 위험해 보이는데..."
    menu:
        "어떻게 하지?"
        "그래도 돌린다!":
            "사회자" "결과는...!"
            $ dice = get_random(itemlist)
            if dice == "null":
                "룰렛이 돌아가다... 갑자기 부서졌다."
                "사회자" "이런! 문제가 생겼군요. 죄송합니다. 대신 당신에게 {color=#7c4dff}500에테르{/color}를 드리겠습니다."
                $ ether += 500
            else:
                "사회자" "축하합니다! {color=#7c4dff}[dice.name]{/color}(을)를 얻으셨군요!"
                "[dice.name]: [dice.script]"
                na "흠, 이거 좋은거 맞나?"
            stop music
            scene black
            "그 순간, 갑자기 바닥이 꺼지고 어두운 바닥으로 떨어지면서..."
            "...그대로 꿈에서 벗어난다."
        "돌리지 않는다":
            stop music
            scene black
            "그 순간, 꿈이 일그러지며 뒤틀리고, 꿈에서 쫓겨나게 된다."
            "다행히 나에게는 아무 이상도 없다."

    jump backto
# 사건 2: 룰렛

label perwin:
    scene black with dissolve
    "..."
    na "응? 잠깐 이거 안들어가지지?"
    scene bg2 with dissolve
    show perwin at left
    show tester nonex at right with easeinright
    na "박사님 무슨 일 생겼어요??"
    p "..."
    na "..."
    p "어, 그게..."
    show tester injang
    extend "버그가 발생해서."
    p "미안!! 얼른 고칠게!!"
    "..."
    "......"
    show tester normal
    p "자! 다 됐다! 점검 보상으로 여기 중에 하나 골라!"

    menu:
        "정기점검" if regularSword.own == False:
            "[regularSword.name]: [regularSword.script]"
            $ regularSword.own = True

        "임시점검" if tempSword.own == False:
            "[tempSword.name]: [tempSword.script]"
            $ tempSword.own = True

        "연장점검" if extendSword.own == False:
            "[extendSword.name]: [extendSword.script]"
            $ extendSword.own = True

        "긴급점검" if emergSword.own == False:
            "[emergSword.name]: [emergSword.script]"
            $ emergSword.own = True

        "그냥 에테르 주세요":
            "당신은 {color=#7c4dff}321에테르{/color}를 받았다."
            $ ether += 321
            
    p "그럼 이제 가볼게!!"
    hide perwin with easeoutleft
    show tester at center with ease
    na "박사님, 아이템 이름이 왜..."
    na "..."
    show tester wut
    extend "이런 미친"
    jump backto
# 사건 3: 다스니 박사의 실수

label dreamland:
    scene black with dissolve
    "..."
    na "내가 드림랜드에 오다니... 믿기지가 않는군."
    play music "Imaginary World.mp3" fadein 1.0
    scene bg1 with dissolve
    "당신은 신비로운 분위기의 지평선 앞에 서 있다."
    "그리고 기다란 하얀색 촉수가 있는 한 사람?과 마주친다."

    ny "흐음? 인간이 여기에 오는 건 오랜만이군."
    ny "난 니알라토텝. 그냥 니알리라고 불러."
    ny "여기엔 어쩐 일로 온 거야? 이렇게 인간한테 위험한 곳에 말이지."

    "어느새 수많은 적들이 당신 곁을 둘러싸고 있는 걸 발견한다."

    $ dice = random.randint(1, 10)
    menu:
        ny "어떻게 할래?"
        "그냥 꿈에서 깨어날래: 100에테르를 얻는다." if dice == 2:
            ny "쳇, 아쉽게됐네."
            "꿈에서 벗어난 당신 손에는 빛나는 {color=#7c4dff}100mL의 에테르{/color}가 쥐어져 있었다."
            $ ether += 100
        "네 계략이지?: 정예 적 「니알라토텝」과 전투를 한다. 3★ 버프 1개와 2★아이템 1개를 얻는다." if dice == 4:
            ny "정답~ 그치만 이제 싸워야 할 적은 내가 되는데?"
        "날 도와줘: 낮은 난이도의 전투를 하고 1~2★ 버프 3개를 얻는다.":
            ny "인간, 내가 특별히 이번에만 도와주는거야?"
        "나 혼자서 할래: 높은 난이도의 전투를 하고 1~2★ 버프 3개와 2★아이템 1개를 얻는다.":
            ny "그래, 네가 죽든 말든 내 일 아니니까 맘대로 해."

    stop music fadeout 1.0
    jump backto
# 사건 4: 드림랜드의 니알라토텝(전투)

label template_dream:
    scene black with dissolve
    "..."
    na "대사"
    scene bg1 with dissolve
    "대사"

    menu:
        "선택지대사"
        "Choice 1":
            "선택지1"
        "Choice 2":
            "선택지2"

    jump backto
# 사건 0: 템플릿

label merudistan:
    $ meru_process = 2
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에 사창가가 껴있다니."
    play music "Mysterious Dreams.mp3" fadein 1.0
    scene amste with dissolve
    "어쩔 수 없이 나는 어느 사창가에 들어서게 되었다."
    "길을 걷던 중, 무의식적으로 들어간 건물에서 고급진 테이블 앞에 앉아 타로 카드로 점을 보고 있는 한 여자와 마주친다."
    show meru normal with dissolve
    "???" "...흐응?"
    "그녀는 손에 있던 카드를 내려놓으며 이렇게 말했다."
    show meru confident
    "???" "정말 기묘한 인연이군. 날 만나는 건 하늘의 별 따기일텐데."
    show meru merong
    m "만나서 반가워. 난 메루라고 해."
    "메루? 페르윈의 친구인 그 매춘부 아닌가?"
    show meru normal
    m "흐흥, 멀티버스에 대해서 들어본 적 있니?"
    m "어떤 사람은 날 쿠르디스탄의 귀여운 아이돌이나 창녀 쯤으로 알고있겠지만, 난 그녀석과는 본질부터 달라."
    m "운명의 선지자, 위대한 하늘의 대리자. 사람들은 날 이렇게 부르지."
    show meru confident
    m "뭐, 그래도 이렇게 마주친 기념으로 선물을 하나 줄게. 골라봐."
    show meru normal
    menu gift:
        "[[황금빛 바클라바]: 모든 축복을 획득한다.":
            $ Atk += 1000
            $ Def += 1000
            $ Qui += 100
        "[[정제된 농축 에테르]: 2000에테르를 획득한다.":
            $ ether += 2000
    
    show meru confident
    m "그럼 나중에 인연이 되면 또 보자."
    show meru normal
    m3ru "Gerok, pêşde herin û riya xwe hilbijêrin.{p}{font=DungGeunMo.ttf}{size=60}방랑자여, 앞으로 나아가 길을 선택하거라.{/size}{/font}"

    stop music fadeout 1.0
    jump backto
# 사건 99: 메루디스탄 (1)

label merudistan_2:
    $ meru_process = 3
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에 사창가가..."
    na "응? 또야?"
    play music "Mysterious Dreams.mp3" fadein 1.0
    scene amste with dissolve
    "어쩔 수 없이 나는 또 사창가에 들어서게 되었다."
    "길을 걷던 중, 신비로운 분위기를 풍기던 그 건물에 들어가 지루하다는 듯이 타로카드를 보던 「메루」와 마주친다."
    show meru normal with dissolve
    m "...흐응? 또야?"
    show meru confident
    m "정말 기묘한 인연이군. 날 두 번이나 만나는 건 하늘의 별 따기일텐데."
    show meru merong
    m "또 만나서 반가워. 저번에도 말했지만, 난 「메루」라고 해."
    show meru normal
    m "날 두번이나 만날 정도면 인연을 넘어선 운명 아닐까?"
    show meru confident
    m "자, 이번에도 골라봐."
    show meru normal
    menu:
        "[[꿈결 비단]: 방어력이 100 증가한다.":
            $ Def += 100
        "[[금실을 엮는 바늘]: 공격력이 100 증가한다.":
            $ Atk += 100     
    
    show meru confident
    m "그럼 나중에 또 보자."
    show meru normal
    m3ru "Gerok, pêşde herin û riya xwe hilbijêrin.{p}{font=DungGeunMo.ttf}{size=60}방랑자여, 앞으로 나아가 길을 선택하거라.{/size}{/font}"

    stop music fadeout 1.0
    jump backto
# 사건 99: 메루디스탄 (2)

label merudistan_3:
    $ meru_process = "done"
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에..."
    na "\"사창가가 있다니\"... 또야?"
    play music "Mysterious Dreams.mp3" fadein 1.0
    scene amste with dissolve
    "어쩔 수 없이 나는 또 사창가에 들어서게 되었다."
    "길을 걷던 중, 이전과를 다르게 무척이나 신비한 분위기를 풍기는 그 건물에 들어가 날 지그시 바라보는 메루와 마주친다."
    show meru confident with dissolve
    m "흐흥~ 또보네? 정말 끈질긴 인연이라니까~"
    show meru normal
    m "날 세 번 연속으로 만날 확률은 극히 적은데, 정말 놀랍지 않니?"
    show meru merong
    m "뭐, 수없이 이 시뮬레이션을 리트라이 하다 보면 언젠가는 그럴 날이 오긴 하겠지만."
    show meru confident
    m "아무리 그렇다고 해도 이럴 확률이 적긴 하니까~"
    show meru normal
    m "저기, 내가 재밌는 걸 하나 알려줄까?"
    m "넌 내가 진짜 메루라고 생각해? 아니면 아니라고 생각해?"
    na "그게 무슨..."
    menu:
        m "대답해 볼래?"
        "맞다":
            menu:
                m "진짜?"
                "맞다":
                    menu:
                        m3ru "{font=DungGeunMo.ttf}{size=60}정말?{/size}{/font}"
                        "아니다":
                            m "..."
                        "아니다":
                            m "..."
                "아니다":
                    m "..."
        "아니다":
            m "..."
    show meru confident
    m "맞아, 난 사실..."
    show meru normal
    ezdan "전지전능한 야지디족의 신, 야즈단이지."
    show meru merong
    ezdan "미안, 처음부터 내가 신인 걸 밝히고 오면 부담스러워 할까 봐."
    show meru normal
    ezdan "부득이하게 메루 모습을 좀 빌렸어. 그 아이도 허락했고."
    show meru confident
    ezdan "어쨌거나, 우리 귀여운 야지디족 프로그래머가 대단한 일을 벌이고 있는데, 이걸 그냥 보고만 있기에는 엄청 아까운 것 같아서 여기에 한번 와 본거야."
    show meru injang
    ezdan "이 모습을 그 애가 아닌 네가 보고 있다는 게 좀 웃기긴 하지만..."
    show meru normal
    ezdan "나중에 걔한테도 이 일을 말해주면 좋을 것 같아."
    ezdan "페르윈, 그녀석이 가장 바라고 있는 일이 날 직접 보는거니까."
    show meru confident
    ezdan "그럼 나중에 또 보자, [name]."
    show meru normal
    ezdan "{i}{font=Caveat-VariableFont_wght.ttf}{size=100}Gerok, pêşde herin û riya xwe hilbijêrin.{/size}{/font}{p}방랑자여, 앞으로 나아가 길을 선택하거라.{/i}"

    stop music fadeout 1.0
    jump backto
# 사건 99: 메루디스탄 (3)

# 보상 구역 이벤트

# 함수코드
label destination:
    if (togo == "전투"):
        jump battle
    elif (togo == "사건"):
        jump happening
    elif (togo == "보상"):
        jump reward
    elif (togo == "정예"):
        jump EliteBattle
    else:
        jump store
# 도착지 함수

label RoadSign:
    $ dice = random.randint(0, 1)
    if areanum == 8:
        jump boss
    elif dice == 0:
        jump select2
    else:
        jump select3
# 선택지 수량 함수 

label backto:
    if HowManyWay == 1:
        jump SelectDream1
    elif HowManyWay == 2:
        jump SelectDream2
    else:
        jump SelectDream3
# 꿈 선택지 함수

label sleep:
    if todream == "이세계 은행":
        jump bank

    elif todream == "메루디스탄":
        if meru_process == 1:
            jump merudistan
        elif meru_process == 2:
            jump merudistan_2
        elif meru_process == 3:
            jump merudistan_3
    # 연계 이벤트 1

    elif todream == "룰렛 TV쇼":
        jump roulette

    elif todream == "드림랜드":
        jump dreamland

    elif todream == "???":
        jump perwin

    else:
        "님 버그 발생했음 실수로 사건 가는걸 여기다 안넣었거나 잘못 타이핑한거임"
        jump perwin
# 꿈 이동 함수

# GUI
screen set_name(title, init_name):
    frame:
        xpadding 100
        ypadding 100
        xalign 0.5 yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5