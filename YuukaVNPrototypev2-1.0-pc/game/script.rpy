# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("[name]")
define k = Character(_("Kyla"), color="#ed1c96")
define l = Character(_("Leila"), color="#75e3c2")
define a = Character(_("Aunt Anna"), color="#ff9543")
define y = Character(_("Yuuka"), color="#fa8de3")
define un1 = Character(_("???"), color="#ff9543") # unknown plain or coloured
define un2 = Character(_("???"), color="#fa8de3")
define mar = Character(_("Marcoss"), color="#259951")
define c = Character("Canlu")
define s = Character("Sparas")

image marcoss happy = "Marcoss/big smile eye1.png"
image marcoss angry = "Marcoss/regular face eye4.png"
image canlu nervous = "Dingo Boi/ding umm eye1.png"
image sparas calm = "Sparas/sparas meh eye2.png"
image sparas happy = "Sparas/sparas big smile eye2.png"

define fadehold = Fade(0.5, 1.0, 0.5)

transform leftside:
    xalign 0.25
    yalign 1.0

transform rightside:
    xalign 0.75
    yalign 1.0

# The game starts here.

label start:

    play music "yuuka bgm 1.mp3"

    scene bg bedroom 1
    with fade

    # GUI needed for name

    $ name = renpy.input("What's your name?", length=32)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "{i}Beep! Beep! Beep!{/i}"

    "I drowsily opened my eyes as the sound of the alarm blared at my ears."

    "I lazily waved my hand to my left, searching for the alarm to turn it off.
    As the torturous sound of the alarm stopped, I slowly sat up in my bed,
    my eyes still blurry as they looked at the alarm."

    m "6:00 AM..."

    "Groaning slightly at the time I got up and started my daily routine for the day"

    scene bg kitchen 1
    with fade

    "Walking down the stairs, I encountered a sight I wouldn’t have ever thought I would see;
    the frame of a familiar back rushing around the kitchen trying to make breakfast."

    "Keyword, “\Trying”\."

    "I sighed as I watch them struggle trying to multitask several tasks at once.
    The little busy-body had stuffed bread in the toaster, rice in the rice cooker,
    and was busy trying to cook some eggs and bacon."

    "Normally, this wouldn’t be a problem... but I couldn’t keep a straight face as the toast sprang out looking burnt,
    and the eggs in such a tinge of black I would’ve thought it came from under a tire."

    "And the bacon... oh the poor bacon..."

    m "K-Kyla.."

    show kyla 1

    k "Ah! B-brother! You’re awake, good morning…"

    "Stopping what she was doing, my little sister looked at me awkwardly,
    probably because what I was feeling was showing in my face."

    m "What are you doing?"

    k "Cooking!"

    "She said proudly, only to then deflate as the fire alarm went off."

    "The bacon and eggs were burnt beyond saving."

    "I sighed as I went to grab a towel by the side and started to blow the
    smoke away before turning off the fire alarm."

    m "Kyla, how many times have I told you to just leave the cooking to me?"

    k "B-but, I just want to help…"

    "Ever since mother and father left them to work overseas, I was the one
    who had to take care of most of the house work."

    "Including cooking, laundry, and buying groceries.
    The only silver lining was that his parents sent a healthy sum of
    money every month for them to live off of."

    m "I know I know, but don’t worry about cooking food. Just leave it to your big brother.. kay? Here,
    come help me clean up and I’ll cook breakfast for us."

    k "..."

    "Kayla just nodded begrudgingly before picking her burnt creations up and
    tossing them in the trash."

    "As much as it pained me to waste food...this one was far from being edible.
    Though, it's obvious having to throw away the food she tried so hard to
    make pained my sister even more."

    "Turning my attention away from my sister, I looked at fridge to decide what to cook for today."

    "Maybe some eggs and ham?"

    "My thoughts froze as I stared at the fridge."

    ". . ."

    ". . . . ."

    "There are no more eggs and somehow there is no ham left either even though
    I bought some just two days ago!!!!"

    "I turned around towards my sister, who, by chance, happened to notice my gaze,
    quickly turned away, confirming my guess."

    "I wanted to ask how she managed to use up all the eggs but more than anything..."

    "HOW THE HELL DID SHE MANAGE TO USE ALL THE HAM!?!?!?"

    "But now's not the time. First I have to make breakfast."

    "I grabbed two instant noodle cups from the cupboard and put some water to boil. While
    instant noodles weren't the healthiest thing to start off the day with, it was
    certainly better than nothing."

    "Now that I notice, there's nothing wrong with the rice cooker, though, to be
    honest it would take a special type of stupid to mess up making rice in a rice cooker."

    "As the water finished boiling, I began to prepare the instant noodles,
    though preparing probably isn’t the right word as I’m basically just
    opening the cup then pouring the packet ingredients in."

    "It was nothing compared to actually cooking a good hearty meal."

    m "So, why did you try to cook before I woke up? Y’know it could have possibly been dangerous, right?"

    "I asked aloud as my hands fiddled with the cups."

    k "I...I just wanted to surprise you. Kind of like how you uses to surprise
    mom and dad during the weekends."

    "I remained silent as I watched the sad expression that had formed in her face."

    m "You don't have to act like me y'know? Mom and dad are gonna be away for awhile,
    so you should take it easy. Don't just try to jump into cooking so suddenly,
    especially when I'm not awake."

    k ". . ."

    "Hearing Kyla not answer made me feel a bit guilty, everything I said made me a hypocrite."

    "Ever since mom and dad left I've been working my butt off to support me and my sister
    and have tried my hardest to make sure she stays focused on her studies rather
    than worrying about anything else."

    "I didn’t want her to be doing what I was doing right now."

    m "Here, how about this Kyla."

    k "Hm?"

    m "I’ll teach how to cook... properly."

    "Her expression quickly turned into happiness and excitement."

    k "You... you will?"

    "Kyla asked happily."

    m "Yeah yeah, but I’ll only allow you to cook lunch, okay?"

    k "Hn! That’s fine!"

    "She was beaming with happiness"

    k "But promise, m’kay? I don’t want you to back out of this!"

    "She was slightly glaring but still happy nevertheless."

    m "Aye, aye, what are you? Our mother?"

    "She just continued to glare"

    m "Fine, I promise to teach you how to cook. How does tomorrow soon?"

    k "Hm! That’s good!"

    m "Alright, alright, and now that that's done, back to “\cooking“\. After that,
    I'll go buy food from Aunty Anna's place."

    "I waved my hand to her as I went to prepare our breakfast."

    k "Oh yeah, [name]. Maybe you should go visit Leila’s place later.
    I heard she came home back from her vacation."

    m "Eh? She did? When’d you hear about it?"

    "I asked bewildered, yet happy at the same time. It’s been 2 weeks since I last
    saw Leila, and I didn’t really know when she would be coming back, even she didn’t know."

    k "Oh, I just saw their car head into their driveway last night. Like, reeaaaallly~ late in the night."

    "Oh, so that explains it. I usually head in to bed at around 12 AM, so I doubt I would've seen them."

    "But then again, that brings up the question, Why was Kyla awake so late in the night?.
    I guess that's something for another time. First, I want to know more about my
    old childhood friend."

    m "Hmm, maybe I should visit her on my way to Aunt Anna’s--"

    k "That might not be a good idea, they came back at around 3 AM, so they're all probably still tired."

    menu:

        "Once again, Why was she awake at such hours?"

        "Choose to visit Leila’s home before going to Aunt Anna’s.":

            jump visit

        "Visit at a later time.":

            jump later

label visit:

    "Hmm, I'll go check on her anyways. I can say sorry afterwards if she's still tired.
    Her parents might get mad though..."

    "Eh, you only live once."

    m "Don’t worry. I’m just gonna say hi to her then I'll go buy groceries.
    Won’t take too much of her time."

    k "If you say so..."

    "Taking Kyla's hesitant agreement as my cue, I filled the instant noodles with the water.
    Now I only had to wait"

    scene bg neighbourhood 1
    with fade

    "While I was walking down the street I checked my phone"

    "8:47 AM."

    "Aunt Anna’s shop should be open now, but before that, I needed to head somewhere first."

    "Stopping at a house just two doors away, I walked to the front door, I felt a
    bit of excitement and happiness as I ringed the doorbell."

    "I stared at the door as a bit of nervousness creeped up on me.
    Maybe it really was a bad idea to come at this time of day,
    especially when Leila and her family probably had just returned from a long trip."

    "But my worries were soon dashed away as the door opened, revealing..."

    "...to no one's surprise a very tired looking Leila, giving me a glare to top it off."

    show leila 1

    "I smiled awkwardly as she continued glaring at me for a solid minute, and I couldn't
    help but notice the stray hairs then went through and fro all across her head."

    m "Um... Hi Leila. Long time no see?"

    "That was very awkward."

    l "You’re an annoying person you know that?"

    "Her voice, which sounded as dead as a bush in the Antarctic, did nothing to remedy the situation."

    m "Uh, yeah...Sorry about that. I was just excited to see you after two weeks."

    "Sighing, Leila dropped her glare as she then tried to fix her messy hair,
    trying to at least save a little bit of her pride after having to look a complete mess."

    "After that, Leila asked me with a yawn."

    l "Noted. Also, how did you know we were back home?"

    m "Oh, Kyla saw you guys come in this morning and she told me about it."

    l "But we came back at three..."

    m "Yeah, had the same thought when she told me."

    "I chuckled as Leila returned a small smile."

    m "Anyways, want to come with me to Aunt Anna’s store then? I’ll pay for anything you buy."

    "I asked hopefully."

    "Leila seemed to ponder for a second before deciding"

    l "Sure, could use the exercise. I had to sit in the car for five hours.
    Five hours!!!"

    m "Cool, c’mon then, let’s head there right now. Auntie should have the place open by now."

    l "Oi, gimme a second to at least fix my hair first!"

    m "Yeah yeah, I’ll be waiting just outside then."

    "After Leila had finally finished getting ready, we headed to our new destination."

    scene bg store 1
    with fade

    "As we headed down the street, I saw our destination closing in.
    It was a small store, one that could probably only fit 15 costumers and be
    filled to the brim."

    "But while it was certainly a small store, and noticeably had much less
    variety and supply than the other food marts, it was the closest one to home,
    plus the clerk was a friend of the family, enough for me and my sister to even call her aunt."

    "Chuckling at the thought, Leila entered the store first, the bell right above
    the door ringing to signal a new costumer coming in."

    m "Aunty Anna! Good morning, how are you?"

    "I called the old woman behind the counter."

    show leila 1 at rightside

    l "Morning Mrs. Cruss."

    "Leila waved at her while smiling."

    show aunt anna 1 at leftside

    a "Ah, if it isn’t Leila and [name]. What brings here today?
    Did you want to buy something or just visit me?"

    m "Eh, I’m here to buy some groceries, Leila came because I said I’d pay for her."

    a "Ah, how nice of you, dear. Almost like a date"

    "I could feel my face flushing for a second at the misunderstanding"

    m "I-it’s nothing of the sort Auntie, just a friend treating another friend after they just returned home."

    l "Yeah, if I wanted to date someone, it certainly wouldn’t be this guy,"

    "Said Leila jokingly."

    a "Well if you say so."

    "As I went to grab a basket to collect all the stuff I needed to buy,
    Leila was milling around the store looking for something good to eat."

    "After both of us grabbed what we wanted, we headed to the counter to pay."

    # bookmark

    a "Oh, I see you’re buying more ham today. Didn’t you buy quite a lot not
    that long ago?"

    m "Well, Kyla decided she would try and cook breakfast this
    morning and I found out she used almost all of the ingredients somehow."

    a "Oh my, that certainly is a surprise."

    "Aunt Anna answered slightly wide eyed."

    l "What? Kyla did? Seriously?"

    "Leila was rather bewildered. After all, as far as she knew, Kyla didn’t know how to cook."

    "And she was very much right on that point."

    l "Well, did it at least taste good?"

    "My only response was a blank stare"

    l "Oh, that’s unfortunate..."

    m "On another topic, what’d you get?"

    l "Hm, I got a few Ice cream cones and this cool looking book."

    "She said smugly, but soon dropped it as she noticed the price tag on the book."

    l "Yeah, I might return this one... [name], as much as I like the idea of getting spoiled,
    I don’t want to use your money to buy a random book, especially when you
    need to buy a bunch of groceries."

    m "Y’know, that might be the nicest thing you have ever said today."

    "She answered my compliment with a rude punch to the shoulder."

    m "Ah, dammit! I was just making a joke."

    l "Ah sorry, had to even out the niceness y’know."

    "She said this with the smug look coming back to her face."

    "Yep, this was the Leila I knew."

    "{i}Ah!{/i}"

    "Hearing this, both of us turned out attention to Aunt Annie as she held the book."

    a "It’s been a while since I saw this book. I’ve been hoping to sell it off,
    but I guess today’s still not the day."

    m "Eh? You have been?"

    "I asked."

    a "Yes, this book used to belong to my husband before he passed away.
    And it was left to soak up dust in the attic. So I thought, I might as well
    try to sell it off but I guess today is still not the day. How unfortunate."

    "She said this while shaking her head."

    l "Y’know Mrs. Cruss. If this is some type of selling tactic you’re trying
    to pull off... it’s certainly working."

    "Leila's eyes were now back on the book but she held back as she didn't bring
    her own money and didn't see to want to use mine just to buy it."

    "We bid our goodbye while walking out of the store and headed our own separate ways."

    jump end_first

label later:

    scene bg kitchen 1
    with fade

    "As I was lying on the couch in the living room, I started to feel hungry.
    Kyla was busy in her room doing something, which honestly, could be anything.
    For all I knew she was trying to create a bomb and I wouldn't know."

    "I checked the time on my phone as I had nothing else to do."

    "9:12 PM."

    "Auntie should be closing up in 18 minutes."

    "As I thought this, another thought popped in my head. It was that expensive book
    Leila wanted."

    "Hmm, I wonder if I should buy it for her? She’ll probably like it considering
    how much she wanted it."

    "I laid on the couch for a solid two minutes before finally making up my mind."

    "Damn it."

    "I got off the couch and quickly put on a pair of shoes and grabbed my wallet.
    High-tailing it to Auntie’s store as fast as I can."

    scene bg store 1
    with fade

    m "Ah, Auntie! Wait a minute!"

    "I call out to her as she was just closing the shop."

    show aunt anna 1

    a "Oh, deary. What are you doing at such a late time, [name]."

    "She was slightly be bewildered, Honestly I couldn't blame her. If I was in her
    position, I would be the same."

    m "{i}Hah... hah...{/i} the book..."

    "I breathed out as I tried to catch my breath."

    a "Hm? The book?"

    m "Yeah, the one that Leila wanted. I want to buy it."

    scene bg bedroom 1
    with fade

    "After returning home, I immediately drop onto my bed, the book falling right
    beside me."

    "I regret not buying the book this morning. It was so much more of a pain
    rushing to the store just to buy late at night."

    "I check the time again, it just turned to 10 AM. Man, did time seem to fly."

    jump end_first

label end_first:

    scene bg bedroom 1
    with fade

    "Sitting up on top of my bed, I decided to check the book on what it
    was about in the first place. I kinda wanted to punch myself as I realized
    I bought an expensive book I knew literally nothing about."

    "For all I knew, it could be about dancing gremlins in a galaxy far, far away..."

    "Man, I wish that a certain brand of space films were as good as its predecessors."

    "Shaking the thought from my head, I open the book."

    "Or at least I “\try“\ to, as the book didn’t budge at all. It was almost
    like the pages were glued together."

    m "Please don’t tell me Auntie scammed me."

    "I know it's unlikely that's the case. Hell, it was much more of a Leila thing
    to do this."

    "God, and it was for so much money as well."

    "Well, this was a problem for future [name], I'll cross that bridge when
    I get there."

    "And with that, I fall asleep."

    "Unknowingly to [name], the book began to shine as it laid in his arms."

    jump chapter1
