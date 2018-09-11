

bp >> dub(-14, sus=8, dur=PDur(5,16)/var([1,6],4),amp=0.5)

k1 >> play("X(  * )",sample=var(P[1:9],1) , dur = 1/2**1,lpf=200)  

c1 >> play("---(-----9)", sample=var([0,1,2],1), dur=PDur(7,9)|rest(2))

Scale.default.set("justMajor")
i=24
m1 >> marimba((P[0:i],P[0:i]*-2,P[0:i]*-4) )

l1 >> razz(P(P[0:i]-24,(P[0:i]-24)*2), dur=rest(1/4)|P[1/2]|PDur(3,5))

ma >> bass(-12,lpf=500, dur=PDur(7,17), delay=0)
x1 >> play("A-  O", dur=PDur(7,19), amp=1, echo=4)
