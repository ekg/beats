Clock.bpm=110
p0 >> play("V ")
p1 >> play("x-o-",sample=P[:3])
b1 >> bass(P[0,2,0,4,0.5,0].stretch(14)|rest(2),delay=0.5,lpf=200) 
k1 >> keys(P[:5]+P(0,2,4),hpf=linvar([500,100,400,0],16),delay=0.5,amp=1.3)
b3 >> play(P[" - - * -"].bubble(), sample=1)
b4 >> play(P[" -"].stretch(16).shuffle().amen(), dur=PDur(7,8), sample=3)
r1 >> sinepad(P(0,2,4)+P[:5]).every(P[8,7,6,2,1],"reverse")

p0.stop()
p1.stop()
b1.stop()
k1.stop()
b3.stop()
b4.stop()
b4.stop()
Scale.default="minorPentatonic"
r1.stop()

q0 >> play("x-&  ",sample=3)
q1 >> play("V-*-",sample=PEuclid(3,8))
q2 >> play("   x - #BH19",sample=P[:3],amp=0.8)
g1 >> pluck(P[0,0,0,0,0,P[7,2,8,1]]-12,lpf=300)

mm >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=3, dist=0.9, sus=1, dur=PDur(7,16)).penta()
b1 >> play((P["x"]*PEuclid(7,16) & P["o"]*PEuclid(2,16) & P["(d-)"].stretch(19)*PEuclid(11,16)).amen(), sample=5, amp=1.2, room=0.2)

p1 >> marimba(PTri(2)+[0,2,5]*PEuclid(9,16), amp=PEuclid(5,16), dur=PDur(3,8)*4, lpf=linvar([500,2400],32))
p2 >> play("q", lpf=700, dur=PDur(3,8), amp=PEuclid(9,16))
q0 >> snick(P[2])

q0.stop()
q1.stop()
q2.stop()
g1.stop()
mm.stop()
b1.stop()
p1.stop()

print(SynthDefs)

Clock.nudge=var([0,0.01,-0.01,0.01], 1/8)-0.09



x2 >> play("(XVoxxxVo)-[*(&@) ]",sample=P[0,0,0,2,3])
j1 >> jbass(P[:2],delay=0.5,dur=PDur(3,8))
j1.stop()
x2.stop()
x0 >> play("Y(ES*) HACK [M*]",sample=P[:9])
x0.stop()
x1 >> pasha(P[:8],delay=PDur(3,8)).every(3,"stutter")

x1.stop()
x0.stop()

c1 >> play("<X >< (*)>< m>")
q0 >> lazer(P(0,2,4)+P[0,0,1,8,0,0.5,0],delay=0.5,dur=PDur(7,16),amp=P[0.8])

k0 >> play("X-O-",sample=2)
k1 >> blip(P(0,2,4,6)+P[0,0,1,6,0,-5],dur=PDur(3,9)|rest(4),room=1)
x9 >> play(P[" (-- [--])"]&P[" (-- [--])"].amen(), amp=linvar([0.8,1,1.1,0,0.7],8))
g0 >> gong(P[-12,-12,-12,-13,-12,-13.5],delay=P[0.5,0.25,0.5,0],dur=PDur(3,8)|rest(2)|PDur(3,11),amp=linvar([1,0.5],7))

k0.stop()
k1.stop()
x9.stop()
g0.stop()

riddim=    P["     x   "].stretch(32)
p1 >> piano(P([0,(2,4),6], [2,(5,3),(5,6,8)],[(4),7,9])+P[:4].stretch(len(riddim)), delay=0, oct=4, dur=PDur(0,len(riddim)), sus=4, amp=PEuclid(5,len(riddim)), bit=0.1, room=2)

print(SynthDefs)

Clock.clear()
