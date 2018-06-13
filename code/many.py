# beats

Clock.update_tempo(124)
d2 >> play(" .n (h ) ", dur=PDur(3,8))
d1 >> play("[x-]", dur=PEuclid(5,8))
p1 >> marimba([P/(0,2,4,7)]-P[12], dur=2)
Clock.stop()
print(SynthDefs)

Clock.update_tempo(119)
d0 >> play("  s ", sample=8, dur=1)
d1 >> play("x-(o o[-a])",sample=var([1,2,3],0.23))

d2.stop()
d2 >> play(" o(* *[ai])",sample=0,dur=PDur(2,9))
