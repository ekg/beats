dd >> dub(P[0,2,4], dur=[4,2,2],lpf=200, sus=1)

pp >> play('<,..>-<./>--',amp=1,crush=18,PDur=(7,16)).every(16, "stutter",1/2)


fd.stop()

mm >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=2, dist=0.9, sus=1, dur=PDur(7,16)).penta()


m1 >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=2, dist=0.9, sus=1, oct=5, dur=PDur(5,16)).penta()

m1.stop()

xx >> play(P[OO'[Vvp] '].stretch(32)|P['X-X_OE'], sample=3, crush=8, amp=1)

Clock.swing = var(1,2)

Scale.root = var([4,4,4,2,2,4,5],16)

Clock.nudge = var([0,0.1,0,0.05,0,0.1,-0.05,0.1],1/3)
ii >> play('X--[--]V -',dur=PDur(5,16))
ii.stop()
ga.stop()
Clock.clear()
ga >> play(P['X--[///////--]',rest(4)])


d1 >> dbass(P[0,1,2,5,4,2,1,0,1,0,-2,-3,-2,-3],tremolo=0,dur=P[6,1,1,3,3,1,1,6,1,1,3,3,1,1],sample=1)

d1 >> dbass(P[0,7,6,5.5,4,3.5,3,-0.5,
              0,1,2,3,3.5,5,2,2.5,
              3,4,5,9,10,6.5,6,5,
              0,1,2,3,4,3.5,3,0,
              -2,0,1,2,-3,-0.5,2,0.5,
              0,7,3.5,3,2,1,0,-1
    ],tremolo=0,dur=P[3],sample=0)

theme_durs = P[2,2,1,2,4,1,1/2,1/2,1,1/2,1/2,1]
son_accent = []
N_hits = len(son_durs)
p2 >> play(P["p"].stretch(N_hits),dur=son_durs,sample=4,pan=(1,-1),amp=son_accent)
p3 >> play(P["t"].stretch(N_hits),dur=son_durs,sample=4,amp=son_accent)

Root.default =0
Scale.default = 'minor'

d1 >> bass(P[0,0,-1,0,2,0,3,2,0,-1,0,0,0,-1,0,3,0,3,2,0,-1,0,],tremolo=0,dur=theme_durs).spread()
Clock.clear()

no >> play('nikete licks [cum]',dur=PDur(5,16),amp=var([0,1,0]))
no >> play('(erik) sucks (dicks) (yum)',dur=PDur(5,16))
v2 >> play('X(p u S e y)o-',dur=PDur(7,16))
v2 >> play('[X(XxoxxXxV)](pusey)')


no.stop()
v2.stop()

q2 >> pasha(P[0:9][0:3][0:5].reverse(),dur=PDur(7,17)|rest(8),sus=var(PDur(7,17))).penta()
q2.stop()
print(SynthDefs)

kk >> varsaw(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=var([0.1,.5],32), lpf=var([50,1500],0.5), dist=0.9, sus=15, dur=PDur(7,16)).penta()


Scale.default="minor"

tt >> blip(P[P(0,2,4),P(0,3,4),P(0,-8)]+d1.pitch, dur=PDur(3,8), room=2,rev=2,wet=2)
tt >> blip(P(0,2,4)+d1.pitch, dur=PDur(3,8), room=0.2, rev=0.2, wet=0.2, oct=3, amp=1, lpf=500, delay=0, sus=4)


kk.stop()

pp >> rave('(P  


Scale.default = "minor"
Scale.root = var([0,0,4,4,-4,-2,-2,4,5],4)
Clock.nudge = 0
Clock.nudge = var([0,0.1,0,0.05,0,0.1,-0.05,0.1],1/4)
Clock.nudge = var([0,0.1,-0.07,0.15,0,0.1,-0.05,0.1],1/4)
Clock.bpm = 120

ss >> play('x-')

ph >> play('er[ o]t. ro)')



