Clock.bpm=84
p1 >> play("x   o  -", sample=4)
p2 >> play("x---*---").every(8, 'shuffle')
k1 >> karp(P(0,2,5)+P[0,3,4,2], delay=0.5, dur=0.25, amp=0.6)
x1 >> keys()
print(SynthDefs)

p1.stop()
Clock.clear()

Clock.bpm=116
Root.default = 3 #alternate with -2
Scale.default = 'minor'
d2 >> play(P["x "] & P[" -"], sample=P[4,4,4,6,4,4,4,7,4,4,4,2], room=0.5, amp=0.7)
#d0 >> play(P["X * X o "], amp=0.6)
d1 >> play(P[" [ --] -"].layer("amen").layer("mirror"), pan=(-0.25,0.25), dur=PDur(5,16), amp=0.4, echo=0, room=0, decay=3/2, sample=P[1:3].layer("bubble"))
p0 >> play(P["<(XXXXXXXXXXXXXXX )-><  * >"], sample=2, amp=0.85)
k1 >> keys(P[[P(0,2,7,x) for x in range(0,12)]].layer("mirror"), delay=0.5, dur=PDur(3,16), drive=0.8, amp=0.2, lpf=200, room=0.5, sus=0.7)
b1 >> pasha([P(0,2,7,x) for x in range(0,12)], delay=0.5, dur=PDur(5,8), drive=0.05, amp=0.7, lpf=500, room=0.5)
q1 >> blip([P(0,2,7,x) for x in range(0,16)], delay=0.5, dur=PDur(3,15), drive=0.04, amp=0.7, lpf=1000, room=0.9, sus=2)
s1 >> swell([P(0,2,7,x) for x in range(0,16)], delay=0.5, dur=PDur(17,29), drive=0.04, amp=0.7, lpf=1000, room=0.9)
x1 >> dbass(var([0,2,7,2],[12,4]), dur=PDur(3,8,[0,2]), sus=2, chop=4, rate=4, lpf=350, drive=0, amp=0.8)

Clock.clear()

print(P(0,2,7).stretch(16))

print(P(0,2,7)+P[0]*P[10])
b1 >> bass(P[0,2,(3,6)],dur=P[4,2,2],lpf=120,amp=0.7 )
b1.stop()
p1 >> keys(dur=1, amp=0.5).follow(b1) + [(0,2,4),(1,3,5,6)]
p1.stop()

Clock.bpm=120
Root.default = 3
Scale.default = 'major' 

d1 >> play(P[["X-p-X-p-X-p-X-p-"]],pan=(-1,1), dur=PDur(7,16),amp=0.4, room=0.25, mix=0.8)     
ff >> play(P[["x-o-","o-x-"]], dur=PDur(5,16),amp=0.8, room=0.25, mix=0.6).every(8, "amen")
b1 >> bass(P[0,[1,3],[3,4]].arp([1,2,4,6,8]),dur=P[2,1,1],lpf=120,amp=.5,sus=[1,2,1] )
p1 >> swell(dur=4, amp=0.5 , room=1, mix=0.5, oct=3).follow(b1) + [(1,4,5),(5,4,1),(3,6,7)]



Clock.bpm=100
Root.default = 3
Scale.default="minor"
p1 >> keys([0,-1,-2,-3], dur=8, lpf=480, lpr=0.1, crush=8) + (0,2,4,const(6))
p3 >> donk(p1.pitch, dur=8, sus=4, room=1, oct=5, amp=0.9) + [0,0,0,P*(2,4,3,-1)]
p2 >> blip(P[:5][:9][:16], dur=4, oct=var([3,4],[12,4])).penta()
d1 >> play("(x )( x)o{ vx[xx]}", crush=16, rate=.8).every([24,5,3], "stutter", 4, dur=3)
d2 >> play("<-s>< ~*~>").every(30.5, "jump", cycle=32)

Clock.clear()
z1 >> play("(xx )( x)o ").every([8], "stutter", 4, dur=3)
f1 >> donk(P[:5][:7][:32], oct=5, crush=8, sus=0.5, dur=PDur(7,15)).every([8,24,7], "stutter", 4, dur=3)


print(SynthDefs)
