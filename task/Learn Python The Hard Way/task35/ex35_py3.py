from sys import exit

# 黄金屋，贪婪者挂
def gold_room():

    print("This room is full of gold.  How much do you take?")
    next = input("> ")
    
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

def bear_room():
    print("""
    
    There is a bear here.
    The bear has a bunch of honey.
    The fat bear is in front of another door.
    How are you going to move the bear?
    
    """)

    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":   # 拿蜂蜜
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved: # 挑衅熊
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
   
    print("""
    
    Here you see the great evil Cthulhu.
    He, it, whatever stares at you and you go insane.
    Do you flee for your life or eat your head?
    
    """)

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()  # 恶魔的房间，一进不复返

# GG，并输出挂掉的原因
def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("""
    
    You are in a dark room.
    There is a door to your right and left.
    Which one do you take?
    
    """)
    
    # 输入下一步的行走方向，左或者右
    next = input("> ")

    if next == "left":
        bear_room()       # 进入熊房间
    elif next == "right":
        cthulhu_room()    # 进入恶魔房间
    else:
        dead("You stumble around the room until you starve.")

# 开始运行游戏
start()
