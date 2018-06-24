b1 >> play(P["(xXV )([--]- o)O-"])
b1.stop()
b2 >> play(P["--&-"], sample=var(P[:7],1))
meter=9
b0 >> play(P["X "].stretch(meter))
e1 >> bass(P[:3].stretch(meter).shuffle(), dur=PDur(3,7), amp=PEuclid(1,7))
p1 >> keys(P[0,1,2,(1,[2,8],3)].rotate(3)&P[8,16].stretch(7)-16, amp=0.9, dur=PDur(16,19))
s1 >> swell(dur=8, formant=var(P[:8],3))

Clock.clear()
