
Scale.default.set('minorPentatonic') 
tuning='ET12'
Root.default.set(-2)

d1 >> play("x-o- ").every(3, "stutter", cycle=5)
kk >> keys((P[0:4],2+P[0:4],4+P[0:4]),amp=0.8,oct=3,dur=P[3,1,3,1,1])
