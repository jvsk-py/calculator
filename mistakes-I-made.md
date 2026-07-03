

**24/06/2026**

okay so when I was creating the init-gui func, I ran the script without actually calling the func, and when I added code to call it, i realised my main loop was above most of the initialisation, am i cooked or am i cooked

after fixing all that, I decided to use my own neurons (not artificial ones) and put the loop outside the init function after everything.

when I took root outside, the definition for root was still inside the func, so I decided to put that at the top before everything else

till now I was following this webpage - https://www.pythonguis.com/tutorials/create-gui-tkinter/
but now ive decided to go on da big YT and watch this - https://www.youtube.com/watch?v=6aKmTV6eYt8
maybe it's better

in between the video i decided to remove the stupid function because there's no point and it's ruining everything RRAAAGGGHHH

it's talking bout sum software called PyUIBuilder so ill install that
nvm it's paid i aint paying for that

that video didnt help at all bro what

gonna watch another one - https://www.youtube.com/watch?v=NzSCNjn4_RI

now ima completely overhaul the old code
it's pretty late (around 20:25) so I'm gonna have dinner then chill or sleep, couldn't learn if I wanted to anyway.


**03/07/2026**

hmm, maybe a bit too long of a break..?

anyways I'm resuming the video and basically copying most of the stuff except for the stuff that I know I shouldn't copy down, I've tinkered with the sizes a lot and I'm about to start actually making the functions.

okay added everything, and it works! just that when I divide by 0 and get "Error", and then I start calculating again, it adds to the word, so it keeps on repeating the error. I'm gonna make it so that after like a 0.5s delay, the result_text clears again.

hmm, for some reason it delays before it clears everything, and when I start calculating again, it shows "Error". tryna fix that now.
I tried adding buffers to every step of the function, but it didn't work.. bruh

okay, so maybe the problem is that the root can't refresh before the time.sleep(0.4) function is called. also added calculation="" after printing the calculation and before deleting the entire line.

well, that made progress, although my Error message is gone, it's not added to my new calculation.

so I guessed that tk has it's own sleep function, and it does! it's called after(), and the article specified I shouldn't use time.sleep as I'll have issues (which I do)

and WOW it has the same problem?? whyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy

NO. WAY.
IT'S ALL BECAUSE OF LAMBDA BRO LAMBDA LAMBDA LAMBDA
IDK IF I SHOULD BE HAPPY WITH OR ANGRY AT IT
RRAAAAAGGGGGGGHHHHHHHHHHH
I USED IT IN MY BUTTONS TOO HOW DID I FORGET

anyways

made a few more changes, like the previous result now carries on in your calculations unless u hit clear
division looks a little ugly, but I can't be bothered rn to change that. 

I consider this project finished. 

Good night.

**Finished 22:36 03/07/26**