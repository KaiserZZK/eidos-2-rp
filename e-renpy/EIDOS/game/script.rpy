# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# $ Zeil = Character('Zeil', color="#E03B8B")
default Morphy = Character('Morphy', color="#E03B8B")
# The game starts here.
label start:
    "Morphy" "在这个项目的伊始\n我怀揣着对人类迄今已掌握的科技还有知识的雄心壮志，"
    "Morphy" "决心我要完成一项足以划分人类文明阶段的成就。"
    "Morphy" "人类本质上是基因传播的副产物，\n而我会通过科技创造一个崭新的、游走于自然选择之外的物种。"
    "Morphy" "一个在思维运算上可以等同、乃至超越人类的造物。"
    "Morphy" "而我甚至可以控制这个物种，让它完成我的期许——\n就像基因传播长久以来控制我们一样。"
    "Morphy" "人类无法跳出基因施加在这个群体上的牢笼了。"
    "Morphy" "那退而求其次\n转头创造一种匹敌人类的存在并获得它的控制权——"
    "Morphy" "仍然算得上一种间接的抗争胜利。"

label background:
    scene bg auditorium
    with fade
    show roland neutral at left
    "Roland" "EIDOS———"
    "Roland" "这个一度只存在于理论构想中超级运算系统，\n正在被我们的科研团队快速实现。"
    "Roland" "在小规模的、当地的经济生产和计划管理中，\nEIDOS的部分程式已经可以做到精准、高效地分配资源。"
    "Roland" "随着帝国分配给研究所的算力比例指数级增长，\n我们在EIDOS项目的开发和应用上也取得了可观的成果。"
    "Roland" "那么，让我们把目光转向Morphy博士——\n他在三年前EIDOS项目伊始便担任首席科研人员。"
    "Roland" "Morphy博士，您来回答一下记者的问题吧。"
    hide roland 

    
    
    scene bg 1采访
    with fade
    "{i}演讲厅的灯光照得Morphy面上发热，口渴难耐。\n他抿了一口水，放下杯子，面色平静，略显疲惫。{/i}"

    show john neutral at right
    "记者" "博士您好，我们来谈谈EIDOS和人工智能吧。\nEIDOS是否是在任何方面都不亚于人类认知的人工智能？"
    "记者" "您能否做出断然的回答：\n{i}是{/i}或{i}不是？{/i}"
    hide john neutral

    
    "Morphy" "要完整回答这个问题需要解释诸多相关领域：\n认知的基本定义，组成EIDOS的不同系统，甚至是人类技术的界限……"
    "Morphy" "既然您这么急于听到明确的答复：\n是，毫无疑问是能够制造出来的——"
    "Morphy" "这种人工智能不仅不亚于人类的智识，\n而且无论从哪方面来说都要超过人类的智识。"
    "Morphy" "我们团队将最终的产物命名为EIDOS，\n而它完全进入社会的那一天必将到来，"
    "Morphy" "总的来说，它不会迟于2000年\n但愿你我都能目睹这一事实。"

    "演出placae-holder" "记者席出现轻微骚动"

    show john neutral at right
    "记者" "期限这么准确？\n您好像是按生产计划来讲的。"
    hide john neutral at right
    
    "Morphy" "差不多。\n我们控制论研究所有关这个课题的科学研究工作规划就定在2000年。"

    show john neutral at right
    "记者" "那制造出EIDOS意味着什么？"
    hide john neutral at right
    
    "Morphy" "首先，显而易见的事实：人类…"
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

    scene bg 1采访
    "Morphy" "…帝国将成为世界上第一个控制论国家。"
    "Morphy" "EIDOS将作为全国决策制定系统的一部分，辅助—甚至在狭义上决定—国家的各个方面：\n政治管理、经济生产、军事演练、社会生活。"
    "Morphy" "其次，我们也将在技术领域达到前所未有的高度。"
    "Morphy" "EIDOS的实现意味着人类\n将对这个迅速复杂化的世界获得更高的控制权："
    "Morphy"
    


    











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





















