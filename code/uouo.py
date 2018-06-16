Clock.bpm=84
Scale.default="mixolydian"
b1 >> play(P["x   "], pan=linvar(P[-1,1]*0.25, 1.5)).spread()
b2 >> play(P["---(-d)"].bubble(), dur=PDur(5,8), delay=0, pan=linvar(P[-1,1]*0.5,0.75)).spread()
b3 >> play(P["  o "])
b4 >> play(P["  s "])
b5 >> play(P[rest(12),"  V "], amp=0.7).spread()
p = P[2,0,6,4,0,2,0,1]
p2 >> pads(p-16, dur=PDur(11,16), amp=PEuclid(3,8)*0.6, sus=0.7).spread()
p1 >> pasha(p+(0,2,4), dur=PDur(11,16), amp=PEuclid(5,8)*1*PEuclid(13,16)*1.1*PEuclid(3,4).stutter(8), room=0.8, lpf=1800, hpf=400, pan=linvar(P[-1,1]*0.5,0.75))
p3 >> squish(p+(0,2,4), dur=PDur(11,16), amp=PEuclid(5,11)*1*PEuclid(3,8), room=0.5, lpf=1200, hpf=800)


p1.stop(); p2.stop()
print(PEuclid(3,4).stutter(4))
Clock.clear()

print(SynthDefs)
print(FxList)
print(Player.get_attributes())
