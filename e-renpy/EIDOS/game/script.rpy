# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Zeil = Character('Zeil', color="#E03B8B")
default Morphy = Character('Morphy', color="#E03B8B")

define Morphy = Character("Morphy")
define 记者 = Character("记者")
# The game starts here.
label start:
    play music "audio/00-seaside-short.mp3" fadein 1.0 volume 0.5
    "Morphy" "在这个项目的伊始\n我怀揣着对人类迄今已掌握的科技还有知识的雄心壮志，"
    "Morphy" "决心我要完成一项足以划分人类文明阶段的成就。"
    "Morphy" "人类本质上是基因传播的副产物，\n而我会通过科技创造一个崭新的、游走于自然选择之外的物种。"
    "Morphy" "一个在思维运算上可以等同、乃至超越人类的造物。"
    "Morphy" "而我甚至可以控制这个物种，让它完成我的期许——\n就像基因传播长久以来控制我们一样。"
    "Morphy" "人类无法跳出基因施加在这个群体上的牢笼了。"
    "Morphy" "那退而求其次\n转头创造一种匹敌人类的存在并获得它的控制权——"
    "Morphy" "仍然算得上一种间接的抗争胜利。"
    stop music fadeout 1.0

label background:
    scene bg 1远景
    with fade
    "科学院控制论研究所。时间：1998"
    scene bg 1近景
    "科学院控制论研究所。时间：1998"
    play music "audio/01-.mp3" fadein 1.0 volume 0.5
    scene bg 对话交互main
    with fade
    show roland neutral at left
    "Roland" "EIDOS———"
    "Roland" "这个一度只存在于理论构想中超级运算系统，\n正在被我们的科研团队快速实现。"
    "Roland" "在小规模的、当地的经济生产和计划管理中，\nEIDOS的部分程式已经可以做到精准、高效地分配资源。"
    "Roland" "随着帝国分配给研究所的算力比例指数级增长，\n我们在EIDOS项目的开发和应用上也取得了可观的成果。"
    "Roland" "那么，让我们把目光转向Morphy博士——\n他在三年前EIDOS项目伊始便担任首席科研人员。"
    "Roland" "Morphy博士，您来回答一下记者的问题吧。"
    hide roland
    stop music fadeout 1.0

    
    scene bg 对话交互main left only
    #scene bg 1采访
    with fade
    "{i}演讲厅的灯光照得Morphy面上发热，口渴难耐。\n他抿了一口水，放下杯子，面色平静，略显疲惫。{/i}"

    #show john neutral at right
    scene bg 对话交互main right
    "记者" "博士您好，我们来谈谈EIDOS和人工智能吧。\nEIDOS是否是在任何方面都不亚于人类认知的人工智能？"
    "记者" "您能否做出断然的回答：\n{i}是{/i}或{i}不是？{/i}"
    #hide john neutral

    scene bg 对话交互 main lleft
    "Morphy" "要完整回答这个问题需要解释诸多相关领域：\n认知的基本定义，组成EIDOS的不同系统，甚至是人类技术的界限……"
    "Morphy" "既然您这么急于听到明确的答复：\n是，毫无疑问是能够制造出来的——"
    "Morphy" "这种人工智能不仅不亚于人类的智识，\n而且无论从哪方面来说都要超过人类的智识。"
    "Morphy" "我们团队将最终的产物命名为EIDOS，\n而它完全进入社会的那一天必将到来，"
    "Morphy" "总的来说，它不会迟于2000年\n但愿你我都能目睹这一事实。"

    play music "audio/02-.mp3" fadein 1.0 volume 0.5
    "演出placae-holder" "记者席出现轻微骚动"
    stop music fadeout 1.0

    play music "audio/01-.mp3" fadein 1.0 volume 0.5
    show john neutral at right
    "记者" "期限这么准确？\n您好像是按生产计划来讲的。"
    hide john neutral at right
    
    "Morphy" "差不多。\n我们控制论研究所有关这个课题的科学研究工作规划就定在2000年。"

    show john neutral at right
    "记者" "那制造出EIDOS意味着什么？"
    hide john neutral at right
    
    "Morphy" "首先，显而易见的事实：人类…"
#     completel silence
    scene bg 1采访b
    show 1领导示意a
    "{i}Morphy注意到Roland朝他打了个手势{/i}"
    hide 1领导示意a
    show 1领导示意b
    ""
    hide 1领导示意b
    show 1领导示意c
    ""
    hide 1领导示意c

    play music "audio/01-.mp3" fadein 1.0 volume 0.5
    scene bg 1采访
    "Morphy" "…帝国将成为世界上第一个控制论国家。"
    "Morphy" "EIDOS将作为全国决策制定系统的一部分，辅助—甚至在狭义上决定—国家的各个方面：\n政治管理、经济生产、军事演练、社会生活。"
    "Morphy" "其次，我们也将在技术领域达到前所未有的高度。"
    "Morphy" "EIDOS的实现意味着人类\n将对这个迅速复杂化的世界获得更高的控制权："
    Morphy "EIDOS并不仅仅是单个意义上的“人工智能”，\n它也是复杂的控制系统的组合智能。"

    Morphy "加在一起，EIDOS将可以承担\n管理生产、发展科学知识，从事宇宙实验等等的使命。"

    show john neutral at right
    "记者" "抱歉，Morphy博士，我没听明白：这怎么会是更高的控制权呢？\n听上去EIDOS将控制我们的一切活动。"
    hide john neutral at right

    Morphy "这完全是一种误解。\n在自动化系统和人工智能发展的任何层面上都少不了人，"

    Morphy "只因为人才能给系统下达任务，只有人才能处于一切信息过程的开端和终端，\n只有人才能确定标准和对结果做出评价。"

    Morphy "通过将演绎思维，包括定理证明过程，自动化，\n啊，说得通俗一些——"

    Morphy "当电子计算机和所谓”人工智能“可以代理无法穷尽的数学运算，\n我们作为人类的 特殊性 将被全面解放。"

    Morphy "EIDOS的现身——是人类的胜利。\n这是未来真正的方向，毋庸置疑。"

    scene bg 1采访黑背景
    Morphy "（在这个混乱的、没有秩序，也没有人在乎你、我或是他的世界中，\n我却牢牢抓住了唯一一件重要的事情。）"
    Morphy "（这是我的胜利，\n这也将代表人类的胜利。）"

    scene bg 1采访
    show john neutral at right
    "记者" "您愿意跟我讲讲，EIDOS最终会以什么形式\n展现在我们这种普通人面前吗？"
    hide john neutral at right

    show john neutral at right
    "记者" "它有人的面貌、能说人的语言吗？"
    hide john neutral at right

    Morphy "只要我们愿意，就能够赋予EIDOS以人的外貌。\n但这不是主要任务，没有比这个更简单的了。"

    Morphy "EIDOS是人工智能，\n人工智能模拟天然认知。"

    Morphy "当您与任何人类，任何 拥有天然认知的对象 交流时，\n您并不知道对方将回答您什么，"

    Morphy "所以，回答您第二个问题，\n“EIDOS能说人的语言吗？”"

    Morphy "当它自觉地做出应答您时，只要您不掀开它的拟人躯壳，\n暴露出下面许许多多的零件和导线，"

    Morphy "您就连一点人工的痕迹也发现不了。"

    show john neutral at right
    "记者" "您把所有这一切讲得这么平淡无奇，\n我还是初次听到，简直不可思议！"
    hide john neutral at right

    show john neutral at right
    "记者" "这就是说，EIDOS将不仅具有知识，\n还能听、能说、能计算、能思考等等。"
    hide john neutral at right

    show john neutral at right
    "记者" "是否能理解为，它将了解人的一切？\n心灵、情绪和感情。"
    hide john neutral at right

    show john neutral at right
    "记者" "它即能开玩笑和感到难过，又能发出责难和表示同情？\n而所有这一切都是由既不知道欢乐也不知道痛苦的、无生命的一堆钢铁做出来的？"
    hide john neutral at right

    scene bg 1采访微笑
    Morphy "【轻微诧异，露出宽慰对方似的笑容】\n噢，原来这个令您感到......您相信一种“无法被传达的灵性”？"
    
    scene bg 1采访
    Morphy "需要强调的是，研究所对EIDOS的主要目标\n并不包含打造一个“​​富有人类感情“的拟人机器。"

    Morphy "同时，所谓人类的灵性是不存在的。\n凡是人能够表达的，毫无例外都是可以模拟的。"
    Morphy "现在我要做一个补充，有一个例外："
    Morphy "要想使机器系统具有猜测人的观点和兴趣、\n以及希望事物将要如何发展的动机，这种可能是不存在的。"


    


    











#
# 随着帝国分配给研究所的算力比例指数级增长，
# 我们在EIDOS项目的开发和应用上也取得了可观的成果。
#
# 那么，让我们把目光转向Morphy博士——
# 他在EIDOS项目伊始便担任首席科研人员。
#
# Morphy博士，您来回答一下记者的问题吧。
#
#
#
#
#     scene bg auditorium
#     with fade
#
# label sprites:
#     "Zeil"  "But wait, where are you?"
#     show zeil delighted
#     "Zeil"  "Oh!"
#     show zeil angry
#     "Zeil" "It's not like I was looking for you or anything."
#     show extra normal at right
#     "Random Girl" "Tsundere..."
#     hide extra
#     "Zeil" "..."
# label character:
#     show zeil bored
#     "Zeil" "Wow... this is too plain."
#     show zeil smile2 with dissolve
#     "Zeil" "I want my color to be bright pink!"
#     Zeil "Wonderful!"
# label background:
#     Zeil "Come on! Let's go the gym."
#     scene bg gym
#     with fade
    
    show zeil smile2 at left
    Zeil "You got here faster than I did!"  
label bgm:
    play music "audio/bgm_basketball.mp3" fadein 1.0 volume 0.5
    Zeil "Oh, the basketball team is playing?"
    Zeil "It's too loud. I'll meet you in the classroom."
    
    stop music fadeout 1.0
    scene bg classroom
    with fade
    
label sfx:
    play sound "audio/sfx_bell.mp3"
    Zeil "Oh no. It's already time."


label choices:
    default learned = False
    Zeil "Did you learn a thing or two?"
menu:
    "Yes":
        jump choices1_a
    "...":
        jump choices1_b
label choices1_a:
    Zeil "Good!"
    $ learned = True
    jump choices1_common

label choices1_b:
    Zeil "..."
    jump choices1_common

label choices1_common:
    Zeil "For more effects, you can check out Ren'Py's guides."
    Zeil "The link can be found in the description."

label flags:
    if learned:
        Zeil "If you learned a thing or two, please like the video!"
    else:
        Zeil "You can check out my other videos to learn more about game development!"

    return





















