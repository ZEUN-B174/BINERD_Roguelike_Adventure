# 이 파일에 게임 스크립트를 입력합니다.
init python:
    import random

    # 스테이터스
    MaxHP = 100 # 최대체력
    Hp = 100 # 현재체력
    Atk = 20 # 공격력
    Def = 10 # 방어력
    Qui = 10 # 민첩도
    ether = 200 # 에테르

    #시스템
    area1 = "1" # 구역 1 목적지
    area2 = "2" # 구역 2 목적지
    area3 = "3" # 구역 3 목적지
    AreaList = ["전투", "사건", "보상", "정예", "상점"]
    togo = "none" # 목적지 저장 변수

    dream1 = "a" # 사건 1 목적지
    dream2 = "b" # 사건 2 목적지
    dream3 = "c" # 사건 3 목적지
    DreamList = ["이세계 은행", "메루디스탄", "룰렛 TV쇼"]
    todream = "none" # 사건 선택지 저장 변수
    #선택지 중복 방지용
    dreamed1 = False
    dreamed2 = False
    dreamed3 = False

    floor = 1 # 층 수
    areanum = 0 #구역 번호
    dice = 0 # 랜덤이벤트에 쓸 주사위
    HowManyWay = 0 # 꿈 선택지 숫자 정하기용
    mode = "none" # 게임모드

    # 기물
    itemlist = ["사탕곰", "드림캐쳐", "미분음 오르골", "체력 증진기 #22", "지갑전사", "꿈바다 샘플 #009", "빨간 구두", "구멍난 주머니"]
    itemexp = ["곰인형 모양의 사탕. 전투에서 사용하면 체력을 20 회복한다.", "신비로운 문양의 드림캐쳐. 사건에서 로스트 되는 것을 3번 막아준다.", "12음계에서 벗어난 신비한 음을 연주하는 오르골. 꿈 계열 기물의 효과가 2배가 된다.", "다스니 연구소의 체력계 기물. 전투 진입 시, 체력이 2배가 된다.", "다스니 연구소의 현실적인 기물. 에테르에 비례해서 공격력이 증가한다.", "연구소에서 체취한 꿈의 일부. 마시면 기이한 꿈을 꿀 수 있다.", "전투 시 첫 3턴은 무조건 공격만 할 수 있다.", "구역에 입장할 때마다 에테르가 10씩 줄어든다."]
    
    candybear = False # 사탕곰
    dreamcatcher = False # 드림캐쳐
    musicbox = False # 미분음 오르골
    hpEnhancer = False # 체력 증진기 #22
    WalletWarrior = False # 지갑전사
    sample009 = False # 꿈바다 샘플 #009
    RedShoes = False # 빨간 구두
    badpocket = False # 구멍난 주머니

    # 기타 코드
    meru_process = 1 # 메루디스탄 사건 진척도.

init:
    screen stat():
        frame:
            xpadding 50
            ypadding 50
            align (0.075, 0.1)
            grid 2 5:
                text '체력'
                text "| [Hp]/[MaxHP]"

                text '공격력'
                text "| [Atk]"

                text '방어력'
                text "| [Def]"

                text '에테르'
                text "| [ether]"
                
                text "[floor]층"
                text "| [areanum]구역"

# image 문을 사용해 이미지를 정의합니다.
image room = "room_edited.png"
image bg1 = "dreamspace.jpg"
image bg2 = "spaceship.jpg"
image bg3 = "stars.jpg"
image bank = "bank.jpg"
image amste = "amsterdam.jpg"
image tvshow = "tv_show.jpg"

image perwin = "Perwin.png"

image tester normal = "Tester_default.png"
image tester nonex = "Tester_0-0.png"
image tester smile = "Tester_smile.png"
image tester surpriesd = "Tester_surprised.png"
image tester confident = "Tester_UU.png"
image tester injang = "Tester_-w-.png"
image tester wut = "Tester_wut.png"
image tester curious = "Tester_curious.png"

image meru normal = "Meru_default.png"
image meru confident = "Meru_UU.png"
image meru injang = "Meru_-w-.png"
image meru merong = "Meru_merong.png"

# 게임에서 사용할 캐릭터를 정의합니다.
define p = Character('페르윈 다스니', color="#fcb714")
define a = Character('Mîxayîl', color="#514ed7")
define na = Character("[name]", color="#565274")
define m = Character('메루', color="#7c4dff")
define m3ru = Character(who_bold=True, what_italic=True, what_xalign=0.5, what_textalign=0.5, what_color="#7c4dff")
define ezdan = Character('야즈단', what_italic=True, color="#7c4dff")

# 여기에서부터 게임이 시작합니다.
label start:

    $ name = renpy.call_screen("set_name",title="여기에 이름을 입력하면 돼.", init_name="테스터")
    scene room with dissolve

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
            p "그래도 말 안해주면 엄청 헷갈린 테니까 잘 들어."
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
    p "거래 구역에서 상품을 구매하거나, 「어떤 기물」 에서 중요하게 쓰이기도 하지."
    
    show tester curious
    na "그 기물이 뭔가요?"
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
    a "상점 구역: 에테르를 소비해 원하는 기물이나 버프를 구매할 수 있습니다."
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
    $ areanum = 0
    $ floor = 1
    $ ether = 200
    if meru_process == "done":
        $ meru_process = 1
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
        a "처음 시뮬레이션으로 들어오면 버프 3개와 기물 1개를 기본으로 받게 된답니다."
        a "시뮬레이션은 혼자 돌아다니기엔 위험하니 이걸 챙기길 바라요."
    jump select3
# 이곳은 로딩화면의 끝입니다.

label report:
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
    python:
        area1 = random.choice(AreaList)
        area2 = random.choice(AreaList)
        while (area1 == area2):
            area2 = random.choice(AreaList)
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
    python:
        area1 = random.choice(AreaList)
        area2 = random.choice(AreaList)
        while (area1 == area2):
            area2 = random.choice(AreaList)
        area3 = random.choice(AreaList)
        while (area1 == area3 or area2 == area3):
            area3 = random.choice(AreaList)
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

        dream1 = random.choice(DreamList)
        while (dream1 == "메루디스탄" and meru_process == "done"):
            dream1 = random.choice(DreamList)
        
        dream2 = random.choice(DreamList)
        while (dream2 == "메루디스탄" and meru_process == "done"):
            dream2 = random.choice(DreamList)
        
        dream3 = random.choice(DreamList)
        while (dream3 == "메루디스탄" and meru_process == "done"):
            dream3 = random.choice(DreamList)
    
    jump backto

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
    jump select3
# 이곳은 미개척 구역의 끝입니다.

# 사건 구역 이벤트
label bank:
    scene black with dissolve
    "..."
    na "...은행이 이세계에 있는 한, 어쩔 수 없지."
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

    jump backto
# 사건 1: 이세계 은행

label roulette:
    scene black with dissolve
    "..."
    na "역시, TV 프로그램에 나오길 잘한거같아."
    scene tvshow with dissolve
    "사회자" "신사 숙녀 여러분, 드디어 가장 재미있는 시간이 돌아왔습니다!"
    "사회자" "오늘의 우승자, [name]님은 어떤 상품을 가져가게 될까요?"
    "사회자" "[name]님, 앞의 룰렛을 돌려주세요!"

    "근데 아무리 생각해도 이 를렛 좀 위험해 보이는데..."
    menu:
        "어떻게 하지?"
        "그래도 돌린다!":
            "사회자" "결과는...!"
            $ dice = random.randrange(0, len(itemlist))
            "사회자" "축하합니다! {color=#7c4dff}[itemlist[dice]]{/color}(을)를 얻으셨군요!"
            "[itemlist[dice]]: [itemexp[dice]]"
            scene black
            "그리고 갑자기 꿈에서 쫒겨났다."
        "돌리지 않는다":
            scene black
            "그 순간, 꿈이 일그러지며 뒤틀리고, 꿈에서 쫓겨나게 된다."
            "다행히 나에게는 아무 이상도 없다."

    jump backto
# 사건 2: 룰렛

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
# 사건 템플릿

label merudistan:
    $ meru_process = 2
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에 사창가가 껴있다니."
    scene amste with dissolve
    "어쩔 수 없이 나는 어느 사창가에 들어서게 되었다."
    "길을 걷던 중, 무의식적으로 들어간 건물에서 고급진 테이블 앞에 앉아있는 한 창녀와 마주친다."
    show meru normal with dissolve
    "???" "...흐응?"
    show meru confident
    "???" "정말 기묘한 인연이군. 날 만나는 건 하늘의 별 따기일텐데."
    show meru merong
    m "만나서 반가워. 난 메루라고 해."
    show meru normal
    m "흐흥, 멀티버스에 대해서 들어본 적 있니?"
    m "어떤 사람은 날 쿠르디스탄의 귀여운 아이돌로 알고있겠지만, 난 그녀석과는 달라."
    m "쿠르디스탄의 천재 해커, 화류계의 정상이 바로 나지."
    show meru confident
    m "이렇게 마주친 기념으로 선물을 하나 줄게. 골라봐."
    show meru normal
    menu gift:
        "[[황금빛 바클라바]: 모든 축복을 획득한다.":
            $ Atk += 1000
            $ Def += 1000
            $ Qui += 100
        "[[정제된 농축 에테르]: 2000에테르를 획득한다.":
            $ ether += 2000
    
    show meru confident
    m "그럼 나중에 인연이 되면 또 보자고."
    show meru normal
    m3ru "Gerok, pêşde herin û riya xwe hilbijêrin.{p}방랑자여, 앞으로 나아가 길을 선택하거라."

    jump backto
# 사건 99: 메루디스탄 (1)

label merudistan_2:
    $ meru_process = 3
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에 사창가가..."
    na "응? 또야?"
    scene amste with dissolve
    "어쩔 수 없이 나는 또 사창가에 들어서게 되었다."
    "길을 걷던 중, 이전과 같은 건물에 들어가 고급진 테이블 앞에 앉아있는 메루와 마주친다."
    show meru normal with dissolve
    m "...흐응? 또야?"
    show meru confident
    m "정말 기묘한 인연이군. 날 두 번이나 만나는 건 하늘의 별 따기일텐데."
    show meru merong
    m "또 만나서 반가워. 저번에도 말했지만, 난 메루라고 해."
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
    m3ru "Gerok, pêşde herin û riya xwe hilbijêrin.{p}방랑자여, 앞으로 나아가 길을 선택하거라."

    jump backto
# 사건 99: 메루디스탄 (2)

label merudistan_3:
    $ meru_process = "done"
    scene black with dissolve
    "..."
    na "하필이면 내가 가야 할 길에"
    extend "..."
    na "\"사창가가 있다니\"... 또야?"
    scene amste with dissolve
    "어쩔 수 없이 나는 또 사창가에 들어서게 되었다."
    "길을 걷던 중, 전에는 알아차리지 못했던 신비한 분위기를 풍기는 그 건물에 들어가 날 지그시 바라보는 메루와 마주친다."
    show meru confident with dissolve
    m "흐흥~ 정말 끈질긴 인연이라니까~"
    show meru normal
    m "날 세 번 연속으로 만날 확률은 극히 적은데 말이지,"
    show meru merong
    m "뭐, 수없이 계속하다 보면 언젠가는 그럴 날이 오긴 하겠지만."
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
                        m3ru "정말?"
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
    ezdan "미안, 메루의 몸을 빌린 건 그 녀석이 가장 먼저 만들어진 스프라이트라서 그랬어."
    show meru confident
    ezdan "우리 귀여운 야지디족 프로그래머가 대단한 일을 벌이고 있는데, 이걸 그냥 보고만 있기에는 엄청 아까운 것 같아서 여기에 한번 와 본거야."
    show meru injang
    ezdan "이 모습을 그 애가 아닌 네가 보고 있다는 게 좀 웃기긴 하지만..."
    show meru normal
    ezdan "나중에 걔한테도 이 일을 말해주면 좋을 것 같아."
    ezdan "페르윈, 그녀석이 가장 바라고 있는 일이 날 직접 보는거니까."
    show meru confident
    ezdan "그럼 나중에 또 보자, [Name]"
    show meru normal
    ezdan "{i}Gerok, pêşde herin û riya xwe hilbijêrin.{p}방랑자여, 앞으로 나아가 길을 선택하거라.{/i}"

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
    elif todream == "메루디스탄": # 연계 이벤트 1
        if meru_process == 1:
            jump merudistan
        elif meru_process == 2:
            jump merudistan_2
        elif meru_process == 3:
            jump merudistan_3
    elif todream == "룰렛 TV쇼":
        jump roulette
    else:
        "님 버그 발생했음 실수로 사건 가는걸 여기다 안넣었거나 잘못 타이핑한거임"
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