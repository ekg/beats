k1 >> keys(P[(0, 2, 4), (0, 3, 5), (2, 4, 6), (4, 6, 8)].bubble(), dur=[2,1/2,1,1/2], amp=1, lpf=420).every(6, "reverse").every(8, "rotate", ident=1)

Scale.Root = -2

print(dir(Tuning))
Clock.clear()
Clock.bpm=95

Scale.default.set("minor", tuning=Tuning.just)
Scale.default.set("")

x8 >> pluck(P[(0,2,4),(0,3,6),(4,-2),(1,3),(3,5)], dur=8, lpf=1200, amp=0.2, room=1, echo=7,tremolo=1).every(6, "stutter", cycle=7)
x8 >> pluck(P[(0,2,4)], dur=8, amp=0.2, room=1, echo=7,tremolo=1)


l1 >> star(P[1:8].invert().bubble()*P(0,2,4), amp=0.15, room=0.5, mix=1)
d1 >> play("[(XXXXXXXXeoX)(xxxox)]-o-", amp=0.3, sample=P[0,2,0,0,0,3,0,1,5]).every(6, "stutter", cycle=8)
d1 >> play("[X(xxxox)]-o-", amp=0.3).every(6, "stutter", cycle=8)

print(SynthDefs)

