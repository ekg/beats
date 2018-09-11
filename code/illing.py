p2 >> play('-x-o', sample=var([1,2,3]), amp=0.8)
p2.stop()
b1 >> space(P[0,2,4,0,6]-8,echo=0.5, delay=2, amp=0.2)
q1 >> keys(P(0,2,4)+P[1:6], dur=PDur(3,16)|rest(10), echo=1,amp=0.8)

Root.default = -14

Scale.mode 

p2 >> play('-(Xi) (A*o)', sample=var([1,2,3]), amp=0.8)
b1 >> space(P[0,2,4,0,6]-4,echo=0.5, delay=2, amp=0.2)
q0 >> bass([0,3,4],dur=[4,2,2,rest(8)],amp=0.8)
q1 >> keys(P(0,3,4)+P[1:4], dur=PDur(7,8)|rest(4), echo=5,amp=0.8)

p3 >> play(P['X-V(-----s-#-)'].bubble())
p0 >> play(P['  - '])
p0.stop()

p2 >> play('-(Xi) (A*o)', sample=var([1,2,3]), amp=0.8)
b1 >> space(P[0,2,4,0,6]-4,echo=0.5, delay=2, amp=0.2)p3 >> play(P['X-V(----(*&)-s-)'], dur=1/2)

p3 >> play(P['X-V(-----s-#-)'].bubble())
p0 >> play(P['  - '])
p0.stop()
p3 >> play(P['X-V(----(*&)-s-)'], dur=1/2)

z1 >> play(P['x--xb--'])
