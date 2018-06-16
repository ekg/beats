
drum_seq = "O   x  (oxX)xX"
p1 >> play(drum_seq,sample=1)
p1.stop()
p3 >> play(P["  (-X)- "].bubble(), sample=3)
p3.stop()
p4 >> play(P["V "], delay=var([1,0.5],[28,4])
p4.stop()

Root.default.set(-2)

Root.default=-2
p2 >> bass(P[0,0,2,1], dur=2+PEuclid(3,16), sus=2, amp=0.8, room=0.8, sample=1)
p2.stop()

b1 >> play("x( + o)O ",sample=5)
Scale.default="dorian"
k1 >> keys([(0,2,4)]|P/[4,1,5]+PEuclid(5,8)*P[:8].shuffle())


k1 >> keys(P[(0,2,4)]|P*[4,1,5]+PEuclid(5,8)*P[:8].shuffle())


