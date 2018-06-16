r=rest
Clock.bpm = 122
mantra="JAH MAN"
print(len(mantra))
d2 >> play(mantra, pan=var([-1,1],1), dur=0.5)
d1 >> play(mantra, dur=0.5, pan=var([1,-1],1.5), sample=7)
d2 >> play(mantra, dur=0.5, pan=var([-1,1],2.5), sample=var(P[:6],len(mantra)))
