Clock.bpm=118
#Root.default=var(P[0,2,4,0],8)
Root.default=var(P[0,2,4,0,-8,-6,-4,0],16)
c=var([1,0],[28,4])
p1 >> keys([(0,2,4)], dur=PDur(9,11)*3, sus=PDur(3,8), room=10, echo=0, amp=c*1.2)
p2 >> blip(P[8,4,2,0,rest(2)], dur=PDur(9,11), room=10, amp=1.5, sus=0.5)
p3 >> bass(P[0], delay=0.5, amp=0.5)
b1 >> play(P["x "], dur=1/2, sample=1, amp=1.5)
b2 >> play(P["-"], dur=PDur(9,11), amp=linvar([0.5,0.8],1/2)*c, room=10, pan=linvar(P[-1,1]*0.5,9/7))
b3 >> play(P["  o "], room=0.5, sample=3, amp=c*0.6)
b4 >> play(P["-"], delay=0.75, amp=PEuclid(11,16)*c*0.85, sample=9, room=8)

Clock.clear()
print(SynthDefs)
