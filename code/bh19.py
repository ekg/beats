p1 >> play('x-*&-')
p2 >> play('V  V ', sample=P[3,2,1], amp=0.8)
p3 >> blip(P[0,3,0,4,2]+P(0,2,4), dur=P[3/4,1/4,3/4,P[1/4,7/4]], pan=linvar([-1, 1], 8), lpf=linvar([800,1200], 9), room=P[0.3,0.5,0.3,0.5,0.9])
b1 >> bass(P[0,0,0.5,0,P[1,0.5,2,7]], dur=1, delay=0.5, lpf=400, amp=0.7)

p1.stop()
p2.stop()
p3.stop()
b1.stop()

Clock.clear()

p0 >> play("V ")
p1 >> play("x- -", dur=P[1/4].stretch(7)|P[1], sample=P[2,4,4,1,0,1])
p2 >> play("  + + [ +]", room=0, mix=0)
p3 >> pluck([0, 1, 2, 3, 4, 5], oct=P[3].stutter(7)|P[1]|P[2].stutter(8), delay=0.5, lpf=400).every([6, 2], "reverse")
d1 >> keys([0, 1, 2, 3, 4, 5], dur=1/4, delay=0.5, oct=4, chop=4, sus=2, lpf=linvar([400,800,700,1200],8)).every(8, "reverse").every(5, "reverse", ident=1)

print(SynthDefs)
