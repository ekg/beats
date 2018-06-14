Clock.bpm=122
b1 >> play(P["x "].amen(), sample=8, dist=PDur(4,1), amp=1.5)
b9 >> play(P["X "], sample=2, amp=1)
b5 >> play(P["  * "], spin=var([1,2,7],1), sample=4)
b6 >> play(P["  o "], spin=var([1,2,0],1), sample=4)
b2 >> play(P["  O "], spin=var([1,8,0],0.7), sample=2)
b3 >> play(P[" -"].bubble(), sample=1)
b4 >> play(P[" -"].shuffle(), dur=PDur(7,8), sample=3)
p1 >> blip(P[0,P*[2,2,7],4,rest(1)]-16, amplify=var([1,0,1,0],[7,1,2])*5, dur=var([PDur(3,8),PDur(3,6)],[7,1]), echo=var([0,1.75],3))

p2 >> star([(0,2,4)]+P[:4]+8, dur=var([PDur(3,16)*2,PDur(7,8)*2],[7,1]), amp=var([1,0,1,0],[4,1,3,1])*0.7, room=10, lpf=linvar([800,1200],32))
p3 >> viola([(0,2,4)]+P[:4]+16, dur=var([PDur(3,16)*2,PDur(7,8)*2],[7,1]), amp=var([1,0,1,0],[4,1,3,1]), room=10, echo=5, hpf=3000, lpf=5000)

p2.stop()
Clock.clear()

print(P["X "].amen())

print(sorted(list(Player.get_attributes())))

print(SynthDefs)
print(FxList)
