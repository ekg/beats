Clock.bpm=109
b0 >> play("x- (= (@))(-o)")
b1 >> play(" xx(-) (%#*evag)")
p1 >> play("r rp( am)")
p2 >> play("q", lpf=700, dur=PDur(3,8), amp=PEuclid(9,16))
q0 >> play("i b (b^r)", room=4)

q1 >> play("SeXyAsFuck",bend=1,crush=4,amp=0.8)

k1 >> bass((P[:4]).reverse(),dur=PDur(3,8)*2, sus=1, blur=[2,3], pan=[-1,0,1,0,0], bits=8, fmod=linvar([0,2],8), room=4, amp=PEuclid(5,8)*0.5, lpf=500)

e1 >> play("(XXxVXxV )( -- swa [--]-(==#))")

Scale.default="major"
Scale.default ="minor"
Scale.default="minorPentatonic"

n1 >> pads(P[-12,-13,-14,-15].stutter(6), amp=0.4, delay=0.5)
u1 >> keys(P(0,2,4)+P[0,0,5,3], echo=0.75,decay=6,amp=PDur(5,16))
k2 >> play("X(-m)o(h-)",sample=4)
c0 >> space(P[0:9] + P[6],amp=PEuclid(1,8),sus=4)
gg >> charm()
pp >> snick(P[2])
v0 >> ambi(P[2:7], echo=1.25, decay=3, mix=0.1, dist=0.05)


e2 >> gong(P[0,1,2,4],dur=PDur(2,3),blur=6,pan=[-1,1],amp=PEuclid(2,7)*2, bend=1)
g0 >> keys((P[2,5,3,2,9,3,2,7,3,2] - P[0,2]),crush=19,bits=11,vib=[2,0,4], chop=P[:5], coarse=0.2)

print(P[:3].stutter(4))

n1.stop()
v0.stop()
u1.stop()
q1.stop()
k1.stop()
e1.stop()
e2.stop()
k2.stop()
g0.stop()

print(SynthDefs)
Clock.clear()
