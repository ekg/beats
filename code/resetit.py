d1 >> bass(P[0,0,2,-2]-12,dur=[4,2,1], amp=[0,1,0], lpf=60)
d1.stop()
p1 >> play("x ", dur=PDur(3,8))
p2 >> play(P[P["X-X "]|P["- -[---]"]].bubble(), hpf=linvar(5000,7000,12))
p4 >> blip(P[-24,-22].bubble(), amp=linvar([1,0,0],1)*0.2, delay=0.3)
x1 >> blip(P[-12], dur=PDur(7,8),lpf=180)

k1 >> marimba(P[(0, 2, 4), (0, 3, 5), (2, 4, 6), (4, 6, 8)].bubble(), dur=[2,1/2,1,1/2], amp=0.8, lpf=700, room=0.5, mix=0.2).every(4, "reverse").every(8, "rotate", ident=1)

Scale.Root = -2


Clock.bpm=80

Scale.default.set("major", tuning=Tuning.ET12)

x8 >> pluck(P[(0,2,4)], dur=8, amp=0.4, echo=4,tremolo=2)

l1 >> charm(P[0:8].invert().bubble()*P(0,2,4)-12, amp=0.4, room=0.95, mix=0.5)
d1 >> play("x-o-", amp=0.3).every(6, "stutter", cycle=8)

print(SynthDefs)


x0 >> play(" (- )  ", sample=P[0,1,3,8,9]+P*(0,2), amp=0.5)
m1 >> play(P["(S-E-X) (B.O.T.S.) "], amp=0.8,lpf=272)
r1 >> sinepad(P[0,-0.015,P*[4,4,5,2],-2,-1.013], dur=PDur(2,5), amp=1)

Clock.bpm=112

w1 >> play("x--x-", sample=[1,3,7])

d1 >> play("x-o-", dur=1/2).every(6, "stutter", dur=3,n=3).every(8, "rotate", ident=1)

b1 >> bass(-12, delay=0.5, dur=1)

k0 >> keys(P[0:5], dur=PDur(4,5)|rest(10), room=1, mix=1)

e1 >> keys(P(0,1,3)-12+P[1:5], amp=PEuclid(11,15), dur=P[1/2,1/4,rest(1/2),1/2,rest(1/4),1/4].stretch(15))
e2 >> play("x - o-",lpf=1122)
e3 >> blip(P[-12,-16,-8].stretch(10).stutter(10),delay=0.5,dur=[1,rest(5)])


p1 >> pluck([0,1,2,3],amp=0.5)
p1.stop()
w0 >> sinepad(P[0], amp=PEuclid(3,8).bubble())

