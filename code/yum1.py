Clock.bpm=83

riddim=P["PxR S X"]

b0 >> play(P["x-v-"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))

Scale.default="major"
Root.default = -2

p1 >> piano(P([0,(2,3),4,6],[0,(2,3),(4,5,6)],[0,(6,4)])+P[:4].stretch(len(riddim)), delay=0, oct=5, dur=PDur(4,len(riddim)), sus=1.2, amp=PEuclid(5,len(riddim)), bit=0.1, room=1)

x0 >> play("wo(ah ) ", dur=PDur(7,13),amp=1)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))



riddim=P["Px    RX"]
b0 >> play(P["x -v  -"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,3),4,6],[0,(2,3),(4,5,6)],[0,(6,4)])+P[:4].stretch(len(riddim)), delay=0, oct=5, dur=PDur(4,len(riddim)), sus=2, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

x0 >> play("wo(ah ) ", dur=PDur(7,13),amp=1)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))







Clock.bpm=83

riddim=P["Px    RX"]
b0 >> play(P["x -v  -"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=2, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

x0 >> play("wo(ah ) ", dur=PDur(7,13),amp=1)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))






Clock.bpm=83

riddim=P["Px    RX"]
b0 >> play(P["x -v  -"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

x0 >> play("wo(ah ) ", dur=PDur(7,13),amp=1)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))




Clock.bpm=83

riddim=P["Px    RX"]
b0 >> play(P["x -v  -"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=8, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

x0 >> play("wo(ah ) ", dur=PDur(7,13),amp=1)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))





Clock.bpm=83

riddim=P["Px x-xoRX"]
b0 >> play(P["x -v  -"].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:4].stretch(len(riddim)*3), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=8, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
Root.default = -2

b0.stop()
b1.stop()
p1.stop()
x0.stop()
e1.stop()






Clock.bpm=83

s1 >> swell([0],dur=32)


riddim=    P["Px x-  RX"]
b0 >> play(P[" x -v  - "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
Root.default = -2

b0.stop()
b1.stop()
p1.stop()
x0.stop()
e1.stop()


p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), oct=var([5,6],9), dur=PDur(3,4)*4)
x9 >> play(" (-- [--])")

p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), delay=0, oct=var([2,3],[3,1]), dur=PDur(2,len(riddim)), sus=0.3, amp=PEuclid(5,len(riddim)), bit=0, room=2))












Clock.bpm=83

s1 >> swell([0],dur=32)


riddim=    P["P   x  x"].stretch(29)
b0 >> play(P["v     - "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(4,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
Root.default = -2

b0.stop()
b1.stop()
p1.stop()
x0.stop()
e1.stop()


p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), oct=var([5,6],9), dur=PDur(3,4)*4)
x9 >> play(" (-- [--])")

p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), delay=0, oct=var([2,3],[3,1]), dur=PDur(2,len(riddim)), sus=0.3, amp=PEuclid(5,len(riddim)), bit=0, room=2))









### best yet




Clock.bpm=83

s1 >> swell([0],dur=32)


riddim=    P["xoxoxx--oox"].stretch(29)
b0 >> play(P["v      --- "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(0,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
Root.default = -2

b0.stop()
b1.stop()
p1.stop()
x0.stop()
e1.stop()


p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), oct=var([5,6],9), dur=PDur(3,4)*4)
x9 >> play(P[" (-- [--])"]&P[" (-- [--])"].amen(), amp=linvar([0.5,1],8))
y1 >> play(P["(Xxp)(--- [-o])"]&P["(Xx)(-- [--])"].amen(), amp=linvar([0.5,1],8))


p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29), delay=0, oct=var([2,3],[3,1]), dur=PDur(2,len(riddim)), sus=0.3, amp=PEuclid(5,len(riddim)), bit=0, room=2))





## hardcore start





Clock.bpm=123

s1 >> swell([0],dur=32,amp=40,bit=0.5,dist=2)

s2 >> swell(P[0,3],dur=PDur(7,21),amp=40,bit=0.5,dist=2)


riddim=    P["     x   "].stretch(32)
b0 >> play(P["v      - "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(0,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
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







### WTF





Clock.bpm=123

s1 >> dbass([0],dur=32,amp=4, pan(-1,1),bit=0.5,dist=2,lpf=200)

x9 >> play(".V. ", sample=8)

s2 >> swell(P[0,3],dur=PDur(7,21),amp=40, sus=linvar([0.1,0.2],7), bit=0.5,dist=2,oct=2)
s2.stop()
s1.stop()

riddim=    P["     x   "].stretch(32)
b0 >> play(P["v      - "].stretch(len(riddim)), amp=linvar([0.5,0.1,0.6,0,2],3))
b1 >> play(riddim, amp=PDur(6,7))
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(0,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

p1.stop()

x0 >> play("wo(ah ) ", dur=PDur(7,len(riddim)), amp=PEuclid(7,len(riddim))*0.7)
e1 >> bass(P[0,2,4,4].stretch(7).pivot(3) , dur=4, amp=linvar([0.6,0.4],1.5))

Scale.default="major"
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








##### hot

Clock.bpm=69
Scale.default="dorian"
Root.default = -2
meter=13
a1 >> play(P["x-o-"].stretch(meter))
a2 >> piano(P*[P*[0,2,4]+P(2,3,4,7)]+P[1,3,6].stretch(meter).palindrome(),amp=PEuclid(int(meter/3),meter).rotate(3), room=8, dur=PDur(int(meter/2),meter), echo=P[0.25,1.75,1.25,0.5])


Clock.bpm=67

how_long=29
x0 >> play(P["(-x-[ o-])"].stretch(how_long), amp=PDur(9,17),sample=3)
x1 >> play(P["(xXo)(o  )"].bubble().stretch(how_long), sample=2)
x2 >> play(P["V   xx O"].stretch(how_long))


b1 >> dbass(formant=var(P[:9],1))


Clock.bpm=173

s1 >> dbass([0],dur=32,amp=4, pan(-1,1),bit=0.5,dist=2,lpf=200)

x9 >> play(".V. ", sample=8)

s2 >> swell([0],amp=1, dur=64,oct=2)

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







