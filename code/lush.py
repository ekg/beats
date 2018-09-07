k1 >> keys(P[(0, 2, 4), (0, 3, 5), (2, 4, 6), (4, 6, 8)].bubble(), dur=[2,1/2,1,1/2], amp=1, lpf=420).every(4, "reverse").every(8, "rotate", ident=1)

Scale.Root = -2


Clock.bpm=100

Scale.default.set("major", tuning=Tuning.just)

x8 >> pluck(P[(0,2,4)], dur=10, amp=0.1, echo=7,tremolo=1)

l1 >> star(P[1:8].invert().bubble()*P(0,2,4), amp=0.05, room=0.5, mix=1)
d1 >> play("x-o-", amp=0.3).every(6, "stutter", cycle=8)

print(SynthDefs)

