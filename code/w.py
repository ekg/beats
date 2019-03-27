xo >> play('x o ', coarse=P[23,47,17,19,1], chop=4, sus=2, crush=4, shape=0.4, echo=0.5, decay=1)
xq >> play('X ')
p1 >> pluck(P(2,3,0), sus=4, lpf=600, formant=P[:19][:2], spin=7, drive=0.05)
Clock.nudge = var([0,0.075,0.05,0],1/4)




dd >> bass([0,0,0,2,2,0,3,3,4],dur=PDur(7,16)*2).sometimes('reverse')

p1 >> play('(- )(- )(- )',dur=1/8*PDur(3,16)).sometimes('reverse')
p2 >> play('ooooo',dur=PDur(5,16),lpf=400,formant=P[8:10][:3]).sometimes('reverse')
p3 >> play('1234567',dur=16*PDur(7,16),amp=1 ,sus=2)

# https://docs.foxdot.org/
# https://docs.foxdot.org/docs/players/player-effects/
# 

p2 >> pluck(P[:9], dur=4, slide=1, slidedelay=0.5)

print(SynthDefs)

xo >> play('x o ', coarse=P[23,47,17,19,1], chop=4, sus=2, crush=4, shape=0.4, echo=0.5, decay=1)
xq >> play('X ',amp=2)
p1 >> pluck(P(2,3,0), sus=4, lpf=600, formant=P[:19][:2], spin=7, drive=0.05, dur=1, delay=0.5)

Clock.nudge = var([0,0.075,0.05,0],1/4)

Clock.bpm = 120

ee >> keys(P(0,3)-6, oct=4,amp=3)

q1 >> pluck(dur=4)
q2 >> play("--oo", drive=1)

d1 >> play("x[--]o(=[-o])")

hh >> play("---(-=)", pan=0.5)


tt >> squish(P[0,2,4],lpf=200,dur=PDur(3,16)).sometimes('reverse')

kk >> glass([[0,2,4]]).sometimes('reverse')
kk.stop()
zz >> scatter([0,2,4],dur=[4,2,2])
zz.stop()
qq >> creep([[0,2,4]],sus=2, amp=0.05)
qq.stop()

p2 >> pluck([0,2,4], dur=[1,1/2,1/2], amp=[1,3/4,3/4])
p2.stop()

b1 >> bass([0,2,3,4], dur=4)

ht >> play("---(-=)", pan=0.5)

d1 >> play("/[--]m(=[-o])")
