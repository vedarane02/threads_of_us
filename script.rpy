define e = Character("Veda", color="#FF1493")
define b = Character("Avinash", color="#0000FF")

# Load your assets here
image bg_classroom = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/images/bg classroom.png"  # Classroom background image
image bg_college = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/images/bg hallway.jpg"  # College background image
image bg_fountain = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/images/fountain.jpg"  # Fountain background image
image e_sprite = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/images/zeil laugh.png"  # Veda's character sprite image
image b_sprite = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/images/Avinash.png"  # Updated Avinash's character sprite image

define music_bgm = "C:/Users/vedar/OneDrive/Desktop/Threads of Us/game/audio/Goo Goo Dolls – Iris [Official Music Video] [4K Remaster].mp3"  # Background music

label start:
    play music music_bgm  # Play background music
    scene bg_classroom
    show e_sprite at center  # Show Veda's sprite
    e "In a classroom full of future geniuses, I spotted him—always looking a little lost but charming nonetheless."

    menu:
        "Continue":
            jump level_1

label level_1:
    scene bg_classroom
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "One day, he just sat down next to me, grinning like he owned the place. I couldn’t help but wonder what was going on in that head of his."
    
    b "Is this seat taken, or am I just taking over your personal space?"
    e "Only if you promise not to take all the good vibes with you."

    e "That’s when our playful banter began, and oh, did we roast each other like champions!"

    menu:
        "Continue":
            jump level_2

label level_2:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "As the nights rolled on, our late-night talks turned into a roast fest. Who needs sleep when you have sarcasm?"
    
    b "I swear, if I knew you were this entertaining, I’d have sat next to you on day one. But then, where would I find my daily dose of roast?"
    e "Probably still lost in your own thoughts! Good luck finding that!"

    e "With every playful jab, I realized we were more than just classmates—we were a comedic duo in the making."

    menu:
        "Continue":
            jump level_3

label level_3:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "One memorable night, I gave up on our budget analysis project and decided to nap instead. When I woke up, my stuff was everywhere!"
    
    b "Don’t worry; I gathered your scattered belongings. I’m practically a professional organizer—just not for my own life."
    e "Wow, a compliment wrapped in a roast! You’re full of surprises, Avinash."

    e "That small act of kindness was the moment I started falling for him, but shh, don’t let him know!"

    menu:
        "Continue":
            jump level_4

label level_4:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "As time went by, we became masters of flirtation and roasts. My heart would race with each playful insult."
    
    b "Here, I got you something."  # Changed how he presents the chocolates
    e "Oh? What’s this?"
    
    e "How thoughtful! Just for me? I’m shocked you could remember something that isn’t about yourself!"

    e "But seriously, his gestures melted my heart amidst all the teasing."

    menu:
        "Continue":
            jump level_5

label level_5:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "One day, he surprised me with a Dairy Milk."
    
    b "I thought about getting something else, but I figured it’s better to stick with what I know."
    e "Flattery will get you nowhere! Besides, you only brought it for me to share, right?"

    e "Little did he know, his thoughtful gestures were starting to chip away at my defenses."

    menu:
        "Continue":
            jump level_6

label level_6:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "Before our macro exam, I came to meet him, planning to go home later."
    
    b "You seriously thought you could leave me? My heart can’t take that kind of betrayal!"
    e "Oh please, like I’d ever abandon you to your own devices! I’d rather watch a cat video on loop."

    e "But when I told him I was leaving, his face fell like a bad pun."

    menu:
        "Continue":
            jump level_7

label level_7:
    scene bg_college
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "So, I decided to stay, and his smile lit up the room."
    
    b "Finally! You made the right choice. Who else would endure my endless ramblings?"
    e "And who else would I roast for my entertainment? It’s a win-win!"

    e "With every laugh and playful jab, I could feel our bond growing stronger."

    menu:
        "Continue":
            jump level_8

label level_8:
    scene bg_fountain
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "The day after our exams, I was dying to hang out, but I needed a clever excuse."
    
    e "I casually asked him about a project his friend needed help with."
    
    b "Wait, you remembered that? I’m impressed! Did you actually take notes, or are you just buttering me up for a compliment?"
    e "A little of both! Gotta keep you on your toes."

    menu:
        "Continue":
            jump level_9

label level_9:
    scene bg_fountain
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    e "As we walked toward the fountain, he suddenly looked serious."
    
    b "So, Veda, there’s something I want to say."
    e "If it’s about your fashion choices, I’m already aware."

    e "He looked a bit nervous, and I could tell he was trying to find the right words."

    menu:
        "Continue":
            jump level_10

label level_10:
    scene bg_fountain
    show e_sprite at left  # Show Veda's sprite on the left
    show b_sprite at right  # Show Avinash's sprite on the right
    b "I kind of like you, Veda. No, I really like you. If you ever want to go out with me, I’m free as a bird!"
    
    e "A bird? More like a confused puppy! But a cute one, nonetheless."
    
    b "So, what do you say? Ice cream date, or should we stick to roasting each other over coffee?"

    menu:
        "Tease Him":
            jump tease

label tease:
    e "Why should I agree? You should probably ask me again when you're feeling less nervous!"
    b "Touché! But seriously, I’m just really hoping you say yes."

    menu:
        "Say Yes":
            jump say_yes
        "Tease Him More":
            jump tease_more

label say_yes:
    show e_sprite at center
    e "I finally said yes, but only because you make life infinitely entertaining."
    
    b "So, it really was my charm, wasn’t it?"
    
    e "Or maybe it’s just the chocolates talking!"

    menu:
        "Hug Him":
            jump hug
        "Tease Him Again":
            jump no_hug

label hug:
    e "After a bit of playful teasing, I finally wrapped my arms around him."
    e "In that moment, we both felt our hearts racing, knowing this was just the start of our beautiful journey."

    menu:
        "Play Again":
            jump start
        "Exit":
            return

label no_hug:
    e "Oh, come on! You’re not getting away that easily!"
    b "Fair enough. I’m ready whenever you are!"

    menu:
        "Hug Him":
            jump hug
        "Play Again":
            jump start
