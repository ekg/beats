pp >> play('X-X-',dur=PDur(5,16))
p2 >> play('/',dur=4,lpf=200)

print(SynthDefs)

dd >> dbass(P[0,[1,  2],3,4,5], lpf=100, dur=PDur(5,16))

print(P[0:6]+P[3:5][8:16])

tt >> bass(P[0:6], lpf=500, dry=2, oct=4, dur=PDur(5,16))

ss >> ambi(P[P[0,2,2,4], [1,2], 3, 4, 5], lpf=1000, sus=0.1,amp=0.7, dur=PDur(5,16), oct=3, crush=1, dist=0)

zz >> pluck(P[P[0,2,4],1,2,3,4], lpf=5000, sus=8, amp=0.2)
z1 >> pluck(P[P[0,2,4],P[2,4,6],3,4], lpf=500, sus=8, amp=0.2)

ty >> play('X-o-', amp=0.2)

zy >> pluck(P[1])

zz.stop()

Clock.bpm=150
Clock.nudge=var([0,0.1,0,0.15], 1/4)

e2 >> play('x-ox-', sample=P[:8], amp=0.2, lpf=400).every(32, 'stutter')
e3 >> play('X   O', sample=P[:9], amp=0.2, lpf=300)
e4 >> play('O    ', amp=0.2, lpf=200)

y3 >> play('x o x o X ', amp=0.9, lpf=900,dur=PDur(6,17))

e2.stop()
e3.stop()
e4.stop

bb >> play('<    -   ><<xXx>><(%^@^) >',dur=PDur(4,16), sample=[2,3],amp=0.4, room=4, echo=4)
dx >> bass(P[8,7,6,4,5,2,2,2,1,1,1,0,0,0,0,0,0], delay=0.5, dur=1, lpf=200, oct=4, sus=1.5,)


dd >> keys(P[0:7])

print(Clock)

Root.default = 0

Scale.default = 'dorian'

print(Clock)
print(SynthDefs)

k0 >> saw(P(0,2,4,6,7)+dx.pitch, oct=3, sus=8, dur=4,lpf=500)

gu >> blip(P(0,3,7)+dd.pitch, dur=3, oct=3, delay=3)

kk.stop()

tt.stop()

y1 >> lazer(P[0,[1,  2],6,4,2],lpf=400,sus=var([.7,5.9],4), dur=PDur(15,16),pan=var([-1,1],1))

y2 >> arpy(P[0,[1,  2],6,4,2],lpf=4000,sus=var([.7,5.9],4), amp=0.6 dur=PDur(15,16),pan=var([-1,1],1))


print(PDur(15,16))

print(Clock)



