p1 >> play("hXllxx nktV",sample=6 ,amp=1/2)
Clock.bpm = 102
p2 >> play(P["wake u(pm)"].pivot(int(var([1,2,3],2))), dur=PDur(7,9), amp=0.8)
k1 >> blip(P(0,4,3)+P[0,1,2,3].stutter(2).stretch(12).pivot(7),oct=2,dur=PDur(4,9))
k2 >> pulse(P[0,4,3].stretch(19).shuffle(), delay=0.25, oct=3, echo=1.75, hpf=100, hpr=0.1, amp=PEuclid(7,19)*10, dur=PDur(4,9), chop=1.5)
k2.stop()
k3 >> pulse(P[0,4,3].stretch(19).shuffle(), delay=0.25, oct=5, echo=1.75, hpf=100, hpr=0.1, amp=PEuclid(7,19)*10, dur=PDur(4,9), chop=1.5)
Clock.clear()
print(var([1,2,3],1))