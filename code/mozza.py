meter=7
Root.default=-8
Clock.bpm=80
m0 >> play("X-".stretch(meter).palindrome())
i1 >> blip(P*[0,3,4].reverse().palindrome().stretch(meter).amen(), amp=PEuclid(int(meter/5),meter)*0.9, dur=0.5, dist=0.1, lpf=200).spread()


meter=33
j0 >> play(P["pppP(PuWuM)"].stretch(int(meter/1.5)), amp=linvar([0,1,0.5],1))
j1 >> play(P["--*  (o )"].stretch(meter))
d1 >> play(P["V        "].zip(" (-Oo)").stretch(meter), sample=var([0,5],[meter*1,meter]), pan=(-1,1), amp=PEuclid(int(meter/3),meter)).spread()
i1 >> blip(P[0,3,4].reverse().palindrome().stretch(meter).amen(), amp=PEuclid(int(meter/5),meter)*0.9, dur=0.5, dist=0.1, lpf=200).spread()
Clock.bpm=130



Clock.bpm=134
Root.default = -8
meter=17
a7 >> play(P["(-- [o-]-[-x-])"].stretch(meter).bubble())
a1 >> play(P["    (o x)(xo )"].stretch(meter), sample=var([0,3],1))
a0 >> play(P[" -(xoO)-"].stretch(meter))
a2 >> play(P["FUCKPUSSY"].zip(" ").stretch(meter), sample=var([0,5],[meter*1,meter]))
a3 >> dbass(P[0,1,3].stretch(meter), dur=3, amp=PEuclid(1,int(meter)) )#lpf=400)
a4 >> pulse(P*[P*[0,2,4]+P(1,3,5)&P[3,2,1]]+P[3,5,7].stretch(meter).palindrome(),amp=PEuclid(int(meter/4),meter).rotate(3), oct=3,room=8, dur=PDur(int(meter/4),meter), echo=P[1.25,0.5,0.25,0.5], hpf=var([2000,300],[meter-5,5])).offbeat()
a5 >> marimba(P*[P*[0,2,4]+P(1,3,4,7)]+P[1,2,6].amen().stretch(meter).palindrome(),amp=PEuclid(int(meter/4),meter).rotate(3)*2, room=8, dur=PDur(int(meter/4),meter), echo=P[0.25,1.75,1.25,0.5],pan=(-1,1))



Clock.bpm=120

how_long=29
x0 >> play(P["(-x-[ o-])"].stretch(how_long), amp=PDur(9,17),sample=3)
x1 >> play(P["(xXo)(o  )"].bubble().stretch(how_long), sample=2)
x2 >> play(P["V   xx O"].stretch(how_long))


b1 >> dbass(formant=var(P[:9],1))


Clock.bpm=173

s1 >> dbass([0],dur=32,amp=4, pan(-1,1),bit=0.5,dist=2,lpf=200)

x9 >> play(".V. ", sample=8)

s2 >> swell([0],amp=1, dur=meter,oct=3)

s2.stop()
s1.stop()

riddim=    P["     x   "].stretch(32)
b0 >> play(P["v      - "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(0,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="dorian"
Root.default = -2

b0.stop()
b1.stop()
p1.stop()
x0.stop()
e1.stop()


p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), oct=var([4,5],9), dur=PDur(3,4)*4)
x9 >> play(P[" (-- [--])"]&P[" (-- [--])"].amen(), amp=linvar([0.5,1],8))
y1 >> play(P["(Xxp)(--- [-o])"]&P["(Xx)(-- [--])"].amen(), amp=linvar([0.5,1],8))

y2 >> play(P["<(VxVVX) ><  (*o*) >"], sample=var(P[:3].pivot(3),1))







