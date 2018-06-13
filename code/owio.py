Clock.bpm=108
Scale.default.set("minor")
p1 >> soft(P[0,3,[4,5]].reverse()-16+P[0,2,8], dur=PDur(2,7))
p2 >> pads(P[0,1]-12, dur=PDur(3,8))
b1 >> play(P["x"], dur=PDur(6,16)*2)
b2 >> play(P["t --"].shuffle(), dur=PDur(3,7), sample=9)
b3 >> play("x   ", sample=1)
b4 >> play(P[" - o"].amen(), sample=3, lpf=2000, vibrato=0.1)

Clock.clear()
