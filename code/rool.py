Clock.bpm=120
p1 >> play("x-o-", sample=[0,0,0,0,3,1,7])
p2 >> play("-  -  -  - -  ", sample=P[4].stretch(8)|P[7,8,2])
b1 >> play("V ")
p4 >> play("  *(   YEAH)", sample=8)
Root.default=-8
b0 >> bass(P[0].stretch(13)|P[0.5,0.75,P[1,4,P[1,1,1,7]]], delay=0.5, lpf=350)


p1.stop()
p2.stop()
b1.stop()
p4.stop()
b0.stop()
Clock.clear()
