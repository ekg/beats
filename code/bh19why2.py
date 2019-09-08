p1 >> play("MD5FE68960B38BBA43744D4EEF4F4A1CAC5")
Clock.bpm=134
g2 >> bass(P[-2,4,5],dur=[2,r,2,1],lpf=300,amp=1.4, tremolo=2)
s2 >> bell(P[0,3],amp=2.2,dur=[4,2],lpf=400)
p0 >> play("x-o-").every(4, "stutter", 2, dur=1/4, pan=[-1, 1], rate=2)
Scale.default="minorPentatonic" 
e2 >> gong(P[0,1,2,4],dur=PDur(2,3),blur=6,pan=[-1,1],amp=PEuclid(2,7)*2, bend=1)
p1.stop() 
q0 >> play("X ")    
                          
b1 >> bass(P[:2]|P[:3],lpf=linvar([200,500],7/8))                           
                            
m6 >> play("-x--x------x-x-x----x-x-----x-x-x------x-x")
                                             
Clock.bpm=100 
Clock.nudge=0
Clock.nudge=var([0,0.05,-0.01,0.03,0,-0.02], 1/8)                                           
                                                
p3 >> keys(P([0,(2,3),4,6],[2,(4,3),(4,5,6)],[(6,4),7])+P[:1].stretch(29),amp=P[0.9,1.2])
Clock.bpm=20 
b3 >> marimba(P*[P*[0,2,4]+P(1,3,4,7)]+P[1,2,6].amen(=).stretch(me
ter).palindrome(),amp=PEuclid(int(meter/4),meter).rotate(3)*2, room=8, dur=PDur(int(meter/4),meter), echo=P[0.25,1.75,1.25,0.5],pan=(-1,1))

b3 >> play(P["ITS(RELATIONAL)OK(OR)NOT"].zip(" ").stretch(meter), sample=var([0,5],[meter*1,meter]))

h9 >> play('<X ><  + ><[ -&]><  * >', amp=[0.7,0.8,0.9,0.7,0.8,0.9])
Clock.bpm=123

x1 >> play("BIOHACKERS2019YESSSSSSSSSSSSSSSSSS",sample=P[8,1,1,1,0,2])
x1.stop()

Scale.default="dorian"
m6.stop()

s1 >> play("Genome Graph!")

m9 >> play("X---x*x-(9-8)---x**x---",dur=1/16,amp=0.5)

t3 >> bass(P[0,[1,3],[3,4]].arp([1,2,4,6,8]),dur=P[2,1,1],lpf=220,amp=1,sus=[1,2,1] )

t8 >> donk(t3.pitch, dur=8, sus=4, room=1, oct=5, amp=0.9) + [0,0,0,P*(2,4,3,-1)]

v1 >> varsaw([0,2,6,4], dur=1, sus=8, amp=3/4, rate=PRange(8)/8, chop=13, pan=linvar([-1,1],12), hpf=linvar([0,4000],[32,0], room=0.5 ))
t8.stop()

Clock.bpm=linvar([84,100],64)
print(SynthDefs)
print(Clock)

r1 >> play("some*2tH3iNG SEx-Y",PDur=(9,16))
k0 >> play("Xm*m",amp=2)
k3 >> play("V ",amp=2)

t3.stop()
k1 >> blip(P[:8].reverse()+P(0,7),dur=PDur(9,16))

print(Clock)
Clock.clear()

Clock.clear()

m2 >> swell([0],amp=1, dur=meter,oct=3)
m1 >> pluck()
m1 >> play('XX X  X')
m1 >> bass(P[0])
Clock.bpm=127
print(SynthDefs)
m1.stop()
p1.shuffle()
