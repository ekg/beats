
drum_seq = "O   x  (oxX)xX"
p1 >> play(drum_seq,sample=1)
p1.stop()
p3 >> play(P["  (-X)- "].bubble(), sample=3)
p3.stop()
p4 >> play(P["V "], delay=var([1,0.5],[28,4])
p4.stop()

Root.default.set(-2)

Root.default=-2
p2 >> bass(P[0,1,2,4], dur=1+PEuclid(3,16), sus=2, amp=0.8, room=0.8, sample=2)


b1 >> play(P["x( + o)O "],sample=5)
b1 >> play(P["x( + o)O "].amen(),sample=5)

b1 >> play(P["x( + o)O "].stretch(24)|P["x( + o)O "].amen().stretch(8),sample=5)
Clock.bpm=91 #nice
Clock.bpm=120 #party
Scale.default="minor"
k1 >> keys([(0,2,4)]|P/[4,1,5]+PEuclid(5,8)*P[:8].shuffle())
k2 >> blip([(0,2,4)]|P/[4,1,5]+PEuclid(5,8)*P[:8].shuffle()-16, amp=1)
k3 >> pads([(0,2,4)]|P/[4,1,5]+PEuclid(5,8)*P[:8].shuffle()+8, room=0.5, dur=4, amp=0.5, lpf=400)
b2 >> play(" -")


p3 >> play(drum_seq,sample=1)


Clock.clear()

k1 >> keys(P[(0,2,4)]|P*[4,1,5]+PEuclid(5,8)*P[:8].shuffle())


k2 >> saw(P+[:8])


b1 >> play(P["X"].stretch(4)|P["X "].stretch(12),sample=8)
b2 >> play(P["  *"].stretch(12),sample=8)
Clock.bpm=110
k1 >> blip([(0,1,6)]*P[:8].shuffle(324)*PEuclid(7,19)-8)



Clock.bpm=83
d1 >> play(P["x - "].stretch(8).shuffle())
d3 >> play(P["   +"])
d4 >> play(P["  * "])
d2 >> play(P["V   "])
p2 >> bass(P[0,1,2,4], dur=1+PEuclid(3,16), sus=2, amp=0.5, room=0.8, sample=2)
p2.stop()
p2 >> bass(P[:3]*1.5*PEuclid(7,16), dur=0.5+PEuclid(3,16), sus=1, amp=0.5, room=0.8, sample=2)
drum_seq_erik = "sex sex sex sex"
p1 >> play(drum_seq_erik,sample=var(P[1:9].shuffle(),0.5), pan=linvar([-1,1],9), room=PDur(3,8))


