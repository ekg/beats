r=rest
Clock.bpm = 91
d1 >> play(P["(V,x)-o- "].bubble(), amp=0.9) #,amp=var([1/2,0.3,0.3,0.2]*2,5/9))
b1 >> bass([1,2,rest(1),3,rest(1)], amp=[1,1/2,1/2,1/2,1/2])
b2.stop()
b2 >> pluck(P[0,4,rest(2),2]-24&P[1,2,3],pan=linvar([-1,1],0.5), sus=8, lpf=2000, amp=0.2*PEuclid(6,13))
b3 >> sitar([0,2,rest(1),4,2],pan=linvar([1,-1],0.5), sus=8, dur=1, vibrato=5, room=4, amp=0.3*PEuclid(6,13),lpf=2000)
