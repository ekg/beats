dd >> dub(P[-1,-3,-2,0,0],dur=P[2/3,1/5,1/2,1/8],amp=PEuclid(7,16)*1/8)

pp >> play('<,..>-<.e>--',amp=1,crush=18,PDur=(5,16)).every(15, "stutter", 1/3)
fd >> star(0,dur=var(1,2,3,4),amp=1/2)

fd.stop()

mm >> keys(P[0,[2,3],7,[-1,4,4]], delay=0.5, amp=2, dist=0.9, sus=1, dur=PDur(7,16)).penta()

mm.stop()

Clock.bpm=180
xx >> play('X-(*ooo(o*e))-', sample=P[3,3,4,7,8,9], crush=0, amp=0.7)
qe >> play(' - [-=] - = -', dur=PDur(3,8))
ww >> play('x-O-', dist=0.5, amp=0.5, dur=1)
wo >> play('X-(0 9a 2 O)-', sample=9)
Clock.clear()

gg >> play('-.-.-.-.-.')

no >> play('nikete licks yum')
v2 >> play('X(p u S e y)o-')

q2 >> lazer(P[0:9][0:3][0:5].reverse(),dur=PDur(7,17)|rest(8),sus=var(PDur(7,17))).penta()

print(SynthDefs)
