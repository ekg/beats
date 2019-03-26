pp >> play('X-o--',dur=PDur(5,16)*1/2)
p2 >> play('/',dur=4,lpf=2000)

print(SynthDefs)

dd >> dbass(P[0,[1,  2],3,4,5], lpf=100, dur=PDur(5,16))

tt >> bass(P[0:6]+P[3:5][8:16],lpf=500,wet=2, oct=4, dur=PDur(7,16)).every(32, 'stutter')

ss >> flute(P[1,2],lpf=1200)

zz >> 

Clock.bpm=120
Clock.nudge=var([0,0.02,0,0.03], 1/8)
e2 >> play('x-ox-', sample=P[:8]).every(32, 'stutter')
e3 >> play('X   O', sample=P[:9])
e4 >> play('O    ')

Scale.default=var(['minor','dorian'],32)
kk >> keys(P(0,2,4), delay=1/2, dur=PDur(7,8))
kk.stop()

tt.stop()

yy >> ripple(P[0,[1,  2],3,4,5], lpf=130, dur=PDur(5,16))

uu >> viola(P[0,[-1,  -2],-3,-4,-5], lpf=130, dur=PDur(5,1))




Clock.bpm=48
Clock.nudge=var([0,0.12,0,0.13], 1/8)
Scale.default = 'dorian'
zz >> pluck(P[P[0,2,4],1,2,3,4], lpf=500, sus=8,amp=0.6)
bb >> play('<    -   ><<xXx>><(%^@^) >',dur=PDur(4,16), sample=[2,3],amp=0.4)
dx >> bass(P[8,7,6,4,5,2,2,2,1,1,1,0,0,0,0,0,0], delay=0.5, dur=1, lpf=200, oct=4, sus=1.5,)
y1 >> lazer(P[0,[1,  2],6,4,2],lpf=400,sus=var([1,5.9],4), dur=PDur(15,16),pan=var([-1,1],1))
kk >> marimba(P[(0,2,4)]+dd.pitch, lpf=linvar([600,1700],32), delay=1/2, dur=PDur(5,16), sus=4, room=4,amp=0.6)



Root.default = 0
Clock.bpm=150
Clock.nudge=var([0,0.1,0,0.15], 1/4)
Scale.default = 'dorian'
y1 >> lazer(P[0,[1,  2],6,4,2],lpf=400,sus=var([.7,5.9],4), dur=PDur(15,16),pan=var([-1,1],1))
bb >> play('<    -   ><<xXx>><(%^@^) >',dur=PDur(4,16), sample=[2,3],amp=0.4, room=4, echo=4)
dx >> bass(P[8,7,6,4,5,2,2,2,1,1,1,0,0,0,0,0,0], delay=0.5, dur=1, lpf=200, oct=4, sus=1.5,)
