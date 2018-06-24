r=rest
Clock.bpm = 122
mantra="JAH MAN"
print(len(mantra))
d2 >> play(mantra, pan=var([-1,1],1), dur=0.5)
d1 >> play(mantra, dur=0.5, pan=var([1,-1],1.5), sample=7)
d2 >> play(mantra, dur=0.5, pan=var([-1,1],2.5), sample=var(P[:6],len(mantra)))

x1 >> blip(-4*P[:3]+P(0,2,4).amen(), PDur=PEuclid(5,8)*2, dist=0.1, amp=PEuclid(6,8).amen().rotate(4)*linvar([0.4,0],0.25), pan=(0,1))
k1 >> piano(-8*P[:3].stretch(16), dur=PDur(7,16), delay=0.5, amp=1.3, room=1, lpf=var(PDur(3,8)*900,0.5))

b1 >> bass(P[:4], dur=P[1].stretch(8)|PDur(3,8), amp=PEuclid(3,8))

b2 >> blip(P[3,4,8,12], amp=PEuclid(3,16))

Root.default=0
Clock.clear()
