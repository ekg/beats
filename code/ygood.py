
Scale.default.set('minorPentatonic') 
tuning='ET12'
Root.default.set(-2)


d1 >> play("x - o - ").every(4, "stutter", 8,amp=0.3, rate=[1,2,3,4,5,6,7,8],lpf=200)
bb >> dbass(P[0:4],amp=0.2,dur=[4,1,1,1,1])
kk >> keys((P[0:4],2+P[0:4],4+P[0:4]),amp=0.8,oct=4,dur=P[3,1,3,1,1])
