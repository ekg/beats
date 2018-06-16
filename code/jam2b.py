Root.default.set(-2)
d1 >> play("<X ><  * >< -->")
b1 >> bass(P[:3]*PEuclid(1,3).amen(), chop=linvar([1,9],32), dur=2, amp=0.6)
p1 >> play(P["V seX V seV"])
p2 >> keys((P[0,3,5],P[:4],P/[1,2,4]),amp=linvar([1,1.5],2)).spread()

d1.stop()

b1.stop()
p1.stop()
Clock.clear()

print(P["sex"].amen())

Clock.bpm=100
Scale.default="minorPentatonic"
print(P[:8].stretch(19).shuffle())
e0 >> play("(Xx)( - q)", sample=var(P[:8].stretch(19).shuffle(),0.75))
e1 >> play(P["sex-"].amen(), amp=PEuclid(7,8), sample=8, lpf=500, lpr=0.4)
k1 >> keys([(0,2,5)]+P[0,1,0,3].stutter(), amp=PEuclid(9,19))
k2 >> blip(P[P(0,1,2),P*(2,7,-8),P/(2,3,4)]-4, dur=PDur(27,32)*4, amp=PEuclid(7,19))
k2 >> blip(P[P(0,1,2),P*(2,7,-8),P/(2,3,4)]-4, dur=PDur(5,8)*4, amp=0.7, echo=0.75, lpf=2000, lpr=0.5)




print(SynthDefs)
