




# 

# happy days

Scale.default.set('minor', tuning=ET12)
Cm9 = P(0)
Dm7 = P(1)
Gm7 = P(4)
Am7 = P(5)

k1 >> keys(P[(0,2,4,6),1,4,5])  #Cm9,Dm7,Gm7,Am7])

m1 >> marimba(-12)
print(SynthDefs)

o1 >> play(P["X*-- "].bubble(),dur=PEuclid(5,16))
o1.solo(0)

g1 >> bug(P[0,2],dur=[2,2],amp=2)

g2 >> bass(P[-2,4,5],dur=[2,r,2,1],lpf=300,amp=1.4, tremolo=2)

r = rest(1)
s = rest(2)
g1 >> nylon(P[0,1,5,13,7],dur=[1,2,r],amp=1.6,tremolo=2,lpf=800)
g1.stop()


s2 >> bell(P[0,3],amp=2.2,dur=[4,2],lpf=400)

print (ArgDefs)

print(SynthDefs)

l1 >> lazer(P[0,3,13,5,7,11]-12, dur=PDur(1,33))

g3 >> keys(P[12,0,4,12],dur=1,amp=4,tremolo=1)

g4 >> play("ETHNIC SLUR",sample=8)

r2.solo()

print (SynthDefs)

p0 >> play("x-o-", sample=linvar([1,8], 1/3))
p3 >> play("a\  e c   >9    **&", amp=linvar([1,8]), sample=linvar([1,10],1/7))

p2 >> play("F -", amp=1, sample=[4,3,5], dur=[2,rest(9),1/4,rest(3/4)])

p2.stop()


p0 >> play("x-o-").every(4, "stutter", 2, dur=1/4, pan=[-1, 1], rate=2)


g1 >> play("-*-*-", dur=PEuclid(7,9))