s1 >> play("(XxXo0)-x*-")
s4 >> play("&&9a0", sample=0, chop=8)
s2 >> play("ROSES SMELL like POOP", sample=P[1:3], amp=0.7, dur=PDur(7,11)|rest(8))

p1 >> blip(P[-12:-11],delay=2)
p7 >> pluck(-8,delay=0.5,volume=5)

p3 >> pluck(P[-8,-4,-16,-8], dur=4, delay=0.5, slide=1, slidedelay=0.5)
p2 >> bass(P[2:7],delay=1.25,sex=2, dur=P[0.25].stutter(15)|rest(1), amp=0.8, lpf=200)

s2 >> blip(P[-4:8], delay=0.5)

o3 >> bass(P[-12,-8,-7,-16].stutter(8))
o1 >> keys(P[-12,-8,-7,-16].stutter(8))



