

b1 >> play(P["<x >< -><  o >"], sample=3)


Root.default.set(-2)
Clock.bpm=112
b1 >> play((P["x"]*PEuclid(7,16) & P["o"]*PEuclid(2,16) & P["(d-)"].stretch(19)*PEuclid(11,16)).amen(), sample=5, amp=0.8)
b2 >> play(P["<    x   ><    o   >"] & P["V"]*PEuclid(7,16), sample=4)
Scale.default="minor"
p1 >> spark(PTri(2)+[0,2,5]*PEuclid(9,16), amp=PEuclid(5,16), dur=PDur(3,8)*4, lpf=linvar([500,2400],32))
p2 >> dbass([[0,2],3,4]-4*PEuclid(9,16), dur=PDur(7,16)*2, lpf=800, amp=0.6)

print(BufferManager())
print(SynthDefs)

Clock.clear()
