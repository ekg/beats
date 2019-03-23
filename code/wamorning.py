Clock.bpm=93
x1 >> play("x(-[---]-[--][^8a ])*-")
x2 >> play("(Xx o)( *; q)V ", sample=3, amp=0.86)
b1 >> blip(P[-12,-14,-16].stutter(8), delay=0.5)
q1 >> keys(P(0,-2,-4), dur=PDur(3,8)|rest(8), delay=0.5, echo=0, amp=1, room=0, mix=0, lpf=2000)
z1 >> donk(P[0,-2,-4]+4,delay=PDur(3,8))
p1 >> sinepad(P[0,-2,-4],dur=8)

print(SynthDefs)
