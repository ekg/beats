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