dd >> dub(P[0,2,4], dur=[4,2,2],lpf=100, sus=1)

pp >> play('<,..>-<./>--',amp=1,crush=18,PDur=(7,16)).every(16, "stutter",1/2)


fd.stop()

mm >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=2, dist=0.9, sus=1, dur=PDur(7,16)).penta()


m1 >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=2, dist=0.9, sus=1, oct=5, dur=PDur(5,16)).penta()

mm.stop()

xx >> play(P[OO'[Vvp] '].stretch(32)|P['X-X_OE'], sample=3, crush=8, amp=1)

Clock.swing = var(1,2)


Scale.root = var([4,4,4,2,2,4,5],16)
Clock.nudge = var([0,0.1,0,0.05,0,0.1,-0.05,0.1],1/8)
ii >> play('X--[--]V -',dur=PDur(5,16))

gg.stop()


ga >> play('X--[///////--]')

d1 >> dbass(P[0,1,2,5,4,2,1,0,1,0,-2,-3,-2,-3],tremolo=0,dur=P[6,1,1,3,3,1,1,6,1,1,3,3,1,1],sample=1)

no >> play('nikete licks [cum]',dur=PDur(5,16),amp=var([0,1,0]))
no >> play('(erik) sucks (dicks) (yum)',dur=PDur(5,16))
v2 >> play('X(p u S e y)o-',dur=PDur(7,16))
v2 >> play('[X(XxoxxXxV)](pusey)')


no.stop()
v2.stop()

q2 >> pasha(P[0:9][0:3][0:5].reverse(),dur=PDur(7,17)|rest(8),sus=var(PDur(7,17))).penta()

print(SynthDefs)

kk >> varsaw(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=.3, dist=0.9, sus=15, dur=PDur(7,16)).penta()


Scale.default="minor"


tt >> blip(P(0,2,4)+d1.pitch, dur=PDur(3,8), room=1)
kk.stop()

pp >> rave('(P  


Scale.default = "minor"
Scale.root = var([4,4,4,2,2,4,5],16)
Clock.bpm = 96
Clock.nudge = var([0,0.1,0,0.05,0,0.1,-0.05,0.1],1/8)
d1 >> dbass(P[0,1,2,5,4,2,1,0,1,0,-2,-3,-2,-3],tremolo=0,dur=P[6,1,1,3,3,1,1,6,1,1,3,3,1,1],sample=1)
kk >> varsaw(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=.3, dist=0.9, sus=15, dur=PDur(7,16)).penta()
ga >> play('X--[///////--]')
tt >> blip(P(0,2,4)+d1.pitch, dur=PDur(3,8), room=1)
