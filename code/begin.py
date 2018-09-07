d1 >> bass(P[0,0,2,-2]-12,dur=[4,2,1], amp=[0,1,0], lpf=60)
p1 >> play("x ", dur=PDur(3,8))
p2 >> play(P[P["X-X "]|P["- -[---]"]].bubble(), hpf=linvar(5000,7000,12))
p4 >> blip(P[-24,-22].bubble(), amp=linvar([1,0,0],1)*0.2, delay=0.3)
x1 >> blip(P[-12], dur=PDur(7,8),lpf=180)

k1 >> keys([(0, 2, 4), (0, 3, 5), (2, 4, 6), (4, 6, 8)], dur=[8,4,2,2], amp=1, lpf=120)


Clock.bpm=100
