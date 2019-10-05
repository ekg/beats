hh >> play("------[-----]",sample=P[1,2,3,4,5].every(32,"reverse")).every(8,"amen")
bd >> play("X", dur=[4], amp=2,sample=[1,2,3],   room=0.8, mix=0.8)
bs >> dbass([0,-2], dur=[2,8], amp=0.7, crush=linvar([1,32],4), bits=16, drive=2, lpf=linvar([100,960],5))
ne >> arpy(P[-12,-12,0,-4], delay=0.5, dur=PDur(3,9), hpf=P[800,388,90])
pi >> keys(P(0,2,4,-8)+P[0,0,4,0,-2], dur=P[rest(8),2], slide=[1,2],  blur=[1, 2])

hh >> play("------[-----]",sample=P[1,2,3,4].every(3,"reverse")).every(8,"amen")
bd >> play("X", dur=[4], amp=3,sample=[1,2,3],   room=0.8, mix=0.8)
bs >> donk([-12,-14], dur=P[2,8], amp=4, crush=linvar([1,32],4), bits=16, lpf=linvar([100,700],5), room=0.8)

ne >> arpy(P[-12,-12,0,-4]+[0,12], delay=0.5, dur=PDur(5,9))
pp >> pads(P(0,3,4)+P[:3],dur=8,slide=12,hpf=0, bits=8, amp=0.3, delay=[0.5,0,0.5])
pi >> keys(P(0,2,4,-8)+P[0,0,4,0,-2], dur=P[rest(8),2], slide=[1,2],  blur=[1, 2])
