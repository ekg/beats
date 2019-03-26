pp >> play('x-x--',dur=PDur(5,16))
p2 >> play('/',dur=4,lpf=2000)

print(SynthDefs)

dd >> bass(P[0:6], lpf=400, dur=PDur(5,16)).sometimes('stutter').sometimes('reverse')

print(P[0:6]+P[3:5][8:16])

tt >> bass(P[0:6], lpf=500, dry=2, oct=4, dur=PDur(5,16))

ss >> ambi(P[P[0,2,2,4], [1,2], 3, 4, 5], lpf=1000, sus=0.1,amp=0.7, dur=PDur(5,16), oct=4, crush=1, dist=0)


ty >> play('pqpqzz--', amp=1)

zy >> pluck(P[1], sus=8, lpf=var([500,400,600,700,200,500,200], 1/4), amp=0.5)

ty.stop()

Clock.bpm=90
Clock.nudge=var([0,0.051,0,0.05], 1/4)




Root.default=var([0,2,4],8)


e2 >> play('x-ox-', sample=P[:8], amp=0.2, lpf=4000).every(32, 'stutter')
e3 >> play('X   O', sample=P[:9], amp=0.2, lpf=3000)
e4 >> play('O     ', amp=0.2, lpf=2000)

y3 >> play('x o x o X ', amp=0.9, lpf=900,dur=PDur(6,17))

e2.stop()
e3.stop()
e4.stop

bb >> play('<    -   ><<xXx>> <(%^ o^) >',dur=PDur(5,16), sample=[2,3],amp=0.42, room=4, echo=4)
dx >> bass(P[8,7,6,4,5,2,2,2,1,1,1,0,0,0,0,0,0], dur=1, lpf=1800, oct=4,amp=1.2)


dd >> keys(P[0:7])

print(Clock)

Root.default =0# var(P[-4:4], 1)

Scale.default = 'prometheus'

print(Clock)
print(SynthDefs)

k0 >> saw(P(0,2,4,6,7)+dx.pitch, oct=3, sus=8, dur=4,lpf=500)

gu >> blip(P(0,3,7)+dd.pitch, dur=3, oct=3, delay=3)

kk.stop()

tt.stop()

y1.>> lazer(P[0,[1,  2],6,4,2],lpf=400,sus=var([.7,5.9],4), dur=PDur(15,16), pan=var(P[-1,1],1))

y2 >> arpy(P[0,[1,  2],6,4,2],lpf=400,sus=var([1.7,15.9],4), amp=0.6, dur=PDur(15,16),pan=var([-1,1],1))
y2.stop()



ox >> blip(P(0,7,3,-7), lpf=P[900,800], dur=PDur(3,8)*8,amp=.6, sus=4, room=2)

print(PDur(15,16))

print(Clock)

p2 >> space([[[0,2],3],4], dur=[6,2], lpf=800, hpf=600, oct=4).spread()

cr >> play("#", dur=32, room=1, amp=2).spread()

gg >> zap(P(0,2,7)+P[:4][:2].stretch(32),sus=8,dur=4,oct=[4,3,4,3,3,4,4])

print(SynthDefs)
print(Clock)

hh >> play('   x  +[ m  m ]-', room=1)
h8 >> play('& &&&&&&#^& X-K-', sample=3, amp=0.5,dur=PDur(9,1009))
h9 >> play('<X ><  + ><[ -&]><  * >', amp=[0.7,0.8,0.9,0.7,0.8,0.9]*0.6, sample=0)

y3 >> varsaw(P[0,[1,  2],6,4,], lpf=1000,sus=1.5,amp=0.8,room=.5, dur=PDur(8,16))


ot >> play('x<--K-------->',lpf=2000)

uu >> play(' qQ', sample=6, amp=0.05)

y4 >> play('o x o x oo', amp=0.2).every(8,"stutter")


y5 >> play('---x').every(8,"reverse")
