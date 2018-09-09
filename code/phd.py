du >> dub([-2,0,0,-12],dur=[1/4,1,1/4,1/4,rest(1/2)], amp=0.3)

h1 >> play("x-(o*o a)(--[--] )")
h2 >> play(P["PHD PHD BABY"].bubble(), delay=0.5, dur=[4,2,2,4,4,4,1,1,1,1,1])
h3 >> play("FUCK ME IN THE THESIS YEAHHH", sample=2, dur=P[1/4, rest(9)])

k1 >> blip(P(0,2,4)+P[0,-7,4], dur=PDur(3,8)|P[rest(7)], room=1, mix=1)

Scale.root = -2
