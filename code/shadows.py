b1 >> bass(-12, delay=0.5, dur=2)
e1 >> keys(P(0,1,3)-12+P[1:5], amp=PEuclid(11,15), dur=P[1/2,1/4,rest(1),1/4])
e2 >> play("x--o-",lpf=1122)

