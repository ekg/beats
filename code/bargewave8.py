Clock.nudge=var([0,0.05,0,-0.01,-0.05,0.07,0,0.02,0,0.05,0,0.06], 1/6)

oo >> play('(XxxXxxxXxx) ', sample=8)
p1 >> play(' -(o*O**E8o8e88****)-', sample=[1,0,3,5,3])
kx >> keys(P(0,2,4)+bb.pitch, dur=P[rest(0.5),0.5], amp=P[1,0.7,1,1], dirt=P[0,0.3,0,0,2],room=2)

Scale.root=var([3,-2],16)

bb >> dub([0,2,5],dur=[8,4,4],amp=0.2)


pp >> play('V V xV(oo0)',dur=PDur(7,16))
dd >> play('X-O--',dur=PDur(5,16))

Clock.bpm=120
Clock.nudge=var([0,0.03],1/8)

Scale.root = var([-3,4],16)

bb >> bass([0,4], amp=0.6, lpf=200)

Clock.nudge = var([0,0.1,0,0.05],1/4)

Clock.nudge=var([0,0.1,-0.01,0.05], 1/8)-0.25
Clock.clear()
xx >> play('(Xx)-(oO)-')
xx.stop()

bb >> dub([0,2,4],amp=[0.5,0.1,0.1],dur=[4,2,2])
bb.stop()
print(SynthDefs)

e0 >> play('V(---o--*)')
e0.stop()
e1 >> play('pp uU SS eY', sample=P[:7], amp=0.5, hpf=1000, dist=0.1)
e1.stop()
h1 >> play('x-o[-(_ - \ oo  - ,)]').every(32, 'stutter')
h1.stop()
h2 >> keys(P[:3].reverse()+P(P[0,0,0,-1,0,-4],2,P[4,6,4,4,7,8,4]), dur=PDur(9,16), room=0.5, echo=0.5, sus=0.25, amp=0.7, crush=8, lpf=linvar(500,1200,1/2), oct=4)
h2.stop()

jq >> blip(P(-12,P[-9,-9,-9,-9,-3,-9,-7,-7],-4)+P[:3][:2], dur=PDur(18,32), sus=4, lpf=300)
jq.stop()



Clock.bpm=105

Scale.root = 0

  #var([-3,4],8)

kk.stop()


kp >> pads(P(0,2,4)+P[0:2], oct=3, dur=PDur(7,16), amp=0.5, sus=4)


Clock.nudge=var([0,0.1,-0.01,0.05], 1/8)-0.25
Clock.clear()
xx >> play('(Xx)-(oO)-')
xx.stop()

bb >> dub([0,2,4],amp=[0.5,0.1,0.1],dur=[4,2,2])
bb.stop()
print(SynthDefs)

e0 >> play('V(-o-*)')
e0.stop()
e1 >> play('pp uU SS eY', sample=P[:7], amp=0.5, hpf=1000, dist=0.1)
e1.stop()
h1 >> play('x-o[-(_ - \ oo  - ,)]').every(32, 'stutter')
h1.stop()
h2 >> keys(P[:3].reverse()+P(P[0,0,0,-1,0,-4],2,P[4,6,4,4,7,8,4]), dur=PDur(9,16), room=0.5, echo=0.5, sus=0.25, amp=0.7, crush=8, lpf=linvar(500,1200,1/2), oct=4)
h2.stop()

jq >> blip(P(-12,P[-9,-9,-9,-9,-3,-9,-7,-7],-4)+P[:3][:2], dur=PDur(18,32), sus=4, lpf=300)
jq.stop()



Clock.bpm=105

Scale.root = -3

  #var([-3,4],8)

kk.stop()


kp >> pads(P(0,2,4)+P[0:2], oct=3, dur=PDur(7,16), amp=0.5, sus=4)

xo >> play('= <o--p>', dur=1, sample=var(P[1,2,8,8,2,3],1/4))
xe >> play('(xxxxxXxx)(--- --*-)')
xo.stop()

pp >> play('X-o-', sample=4)
Scale.default = "minor"
qo >> keys(P(0,7)+xq.pitch, dur=PDur(3,8), oct=3)

xq >> pluck(P(0,3,8)+P[:4]|P(0,2,7)+P[:4].reverse(), oct=3, dur=4, lpf=1000)

ss >> ambi(P(0,2,7), oct=P[3,3,3,3,4,4,2,5], dur=16, amp=0.7)
qs >> feel(P/[0,7,-5,1,2], dur=PDur(5,16), oct=P[4,3,2,4,4,3,4,2],amp=0.5)
zz >> prophet(P[:2], dur=rest(1)|P[1,2]|PDur(3,4),sus=1/4, lpf=400)

print(SynthDefs)

Clock.nudge=var([0,0.05,-0.01,0.07,0,0.07], 1/8)-0.25
Clock.nudge=var([0,0.05,-0.01,0.07,0,0.07], 1/3)-0.25





Clock.nudge=var([0,0.1,-0.01,0.05], 1/8)-0.25
Clock.clear()
xx >> play('(Xx)-(oO)-')
xx.stop()

bb >> dub([0,2,4],amp=[0.5,0.1,0.1],dur=[4,2,2])
bb.stop()
print(SynthDefs)

e0 >> play('V(-o-*)')
e0.stop()
e1 >> play('pp uU SS eY', sample=P[:7], amp=0.5, hpf=1000, dist=0.1)
e1.stop()
h1 >> play('x-o[-(_ - \ oo  - ,)]').every(32, 'stutter')
h1.stop()
h2 >> keys(P[:3].reverse()+P(P[0,0,0,-1,0,-4],2,P[4,6,4,4,7,8,4]), dur=PDur(9,16), room=0.5, echo=0.5, sus=0.25, amp=0.7, crush=8, lpf=linvar(500,1200,1/2), oct=4)
h2.stop()

jq >> blip(P(-12,P[-9,-9,-9,-9,-3,-9,-7,-7],-4)+P[:3][:2], dur=PDur(18,32), sus=4, lpf=300)
jq.stop()



Clock.bpm=105

Root.default.set('D#')

  #var([-3,4],8)

kk.stop()


kp >> pads(P(0,2,4)+P[0:2], oct=3, dur=PDur(7,16), amp=0.5, sus=4)

xo >> play('= <o--p>', dur=1, sample=var(P[1,2,8,8,2,3],1/4))
xe >> play('(xxxxxXxx)(--- --*-)')
xo.stop()

pp >> play('X-o-', sample=4)
Scale.default = "minor"
qo >> keys(P(0,7)+xq.pitch, dur=PDur(3,8), oct=3)

xq >> pluck(P(0,3,8)+P[:4]|P(0,2,7)+P[:4].reverse(), oct=3, dur=4, lpf=1000)

ss >> ambi(P(0,2,7), oct=P[3,3,3,3,4,4,2,5], dur=16, amp=0.7)
qs >> feel(P/[0,7,-5,1,2], dur=PDur(5,16), oct=P[4,3,2,4,4,3,4,2],amp=0.5)
zz >> prophet(P[:2], dur=rest(1)|P[1,2]|PDur(3,4),sus=1/4, lpf=400)

print(SynthDefs)

Clock.nudge=var([0,0.05,-0.01,0.07,0,0.07], 1/8)-0.25
Clock.nudge=var([0,0.05,-0.01,0.07,0,0.07], 1/4)-0.25


Clock.nudge=var([0,0.01,-0.01,0.01], 1/8)-0.09

Clock.bpm = 105

px >> play('<X>(- --- -)(ooo*oo*ooo)', sample=P/[2,3], room=0.5)
px >> play('X-o( -- - o)', sample=P/[2,3], echo=1.25, amp=0.7)
px.stop()
pq >> play('p u s e y').every(8, "stutter")
p1 >> play('x - ')

q9 >> play(' - -c', delay=1/3)
q3 >> play('V ', sample=[4,8,2], amp=linvar([0.6,0.9],32), lpf=300)

bb >> play('X-(oO)x-',amp=0.6,dur=PDur(5,16))

bb >> play('X-(k*O*)-',amp=0.6)

bb >> play('(VXVXVXO)-(k*O*)-',amp=0.6)
ee >> feel(P(P[1,2,1],P[7,7,7,3,0,2,5,8]), crush=11, room=4, sus=0.05, amp=0.9, lpf=500, dur=PDur(3,8), echo=1).penta()
b1 >> play('-( e)- ([o--]-)', pitch=-12 ,sample=2, dur=PDur(3,8), amp=0.7)

xx >> pasha(P[0,3,4]-3, dur=PDur(9,16),lpf=400)

cc >> dub()
cc.stop()
g0 >> viola(P[0,0,0,4,0,8]+P(0,4)-4,sus=2,delay=0.2,dur=PDur(3,8),lpf=250).every(8,'stutter')

oh >> play('X-*-')

x2 >> play('<x  x x  x  >< --->')
e1 >> pluck(P/[0,0,2,0,3,0], dur=PDur(7,32), oct=2, lpf=500)
e2 >> keys(P/(0,2,4)+e1.pitch, hpf=1000)

Clock.nudge=var([0], 1/4)-0.35
bu >> play('<x  ox x >< - - - [---]>')
bo >> play('  o ', sample=3)

Clock.bpm=110
bx >> play('X - ')
bq >> 
