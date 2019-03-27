Clock.nudge=0 #var([0,0.05,0,0.1,-0.05,0.07,0,0.05], 1/8)
print(SynthDefs)
Scale.default="minor"
p1 >> play('x-(******* )(-------=)', lpf=linvar(200,1000,32)).every(32, 'reverse')
bb >> bass(P[:2][:4][:5], oct=4, dur=PDur(3,16)).every(32, 'reverse')
bb.stop()
kk >> keys(bb.pitch+P(0,2,4), dur=PDur(5,8), amp=PEuclid(3,8), sus=1)
kk.stop()
Clock.clear()

pp >> play('<x ><  o >', sample=[2,1,1,1], dur=PDur(11,16), amp=0.7)
b2 >> play('X-')
