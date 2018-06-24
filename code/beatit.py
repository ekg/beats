gogo="<x  o><   V  ><  O >"
beatit="ass and titties"

x0 >> play(P[gogo]).stretch(beatit) #.stretch(len(beatit)))
x1 >> play(beatit, sample=var([PEuclid(i,8) for i in range(8)],1)*P[:8], room=10)
b1 >> bass(P[0,2,rest(),4], amp=1, dist=0, dur=PDur(7,16), tremolo=0.2).offbeat(2)
p1 >> saw(P(0,2,3)+P[:3]*PEuclid(5,8), dur=PDur(5,16), amp=PEuclid(3,8), room=0.9, echo=0.5)

k0.stop()
x0.stop()
x1.stop()
b1.stop()
p1.stop()

k0 >> play("V ", sample=4)
