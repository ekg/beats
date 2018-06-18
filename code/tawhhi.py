Clock.bpm=66

p0 >> play("<    ><  * >")
p1 >> play("(-    -ox)-o-", sample=P*[1,4,10,4,1], dur=2*PDur(len("pussy"),len("dick")))

p3 >> play(P["- o -(o-,o0)"].bubble(), dur=PDur(5,16))

b1 >> bass((P[:4]|P[0,-2,1]).stretch(16).palindrome(), dur=PDur(2,8), amp=PEuclid(5,8))

Root.default = -2

p0.stop()
p1.stop()

p3.stop()

b1.stop()

d1.stop()
d1 >> play("x-([--]oo-)-*---", dur=PDur(3,8),amp=PEuclid(2,7))
d1.stop()

f2 >> play("V(z L**)",sample=[0,1,1,3,8])

Scale.default="minor"

Clock.bpm=85
z2 >> bass(P[:2].stretch(meter),dur=PDur(int(meter/2),meter))
z2.stop()
meter=24
f0 >> play(P["(X-o(-V-O))-"].stretch(meter), sample=7)
f0.stop()
o1 >> play(P["X-(xV)s"].stretch(meter))
z1 >> zap(P[:2]+P(0,2,4).stretch(meter),dur=PDur(3,meter),amp=PEuclid(int(meter/3),meter)*2)



f0.stop()
e0 >> play(P["(x VX)( - E)(v_Sm)-"], sample=[3,5,1])
e1 >> play(P["-  -[  --]"],sample=P[:3].shuffle())
b2.stop()



b2 >> swell(P[-8,0].stutter(3), dur=PDur(3,8)*16, amp=PEuclid(3,8))