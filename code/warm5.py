e1 >> keys(P(0,1,3)-12+P[1:5], amp=PEuclid(11,15), dur=P[1/2,1/4,rest(1),1/4])
e2 >> play("x--o-",lpf=1122)
e3 >> blip(P[-12,-16,-8].stretch(10).stutter(10),delay=0.5)


e1 >> keys(P(0,1,3)-12+P[1:5], amp=PEuclid(11,15), dur=P[1/2,1/4,rest(1/2),1/2,rest(1/4),1/4].stretch(15))
e2 >> play("x - o-",lpf=1122)
e3 >> blip(P[-12,-16,-8].stretch(10).stutter(10),delay=0.5,dur=[1,rest(5)])


