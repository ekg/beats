dd >> bass([0,0,0,2,2,0,3,3,4],dur=PDur(7,16)*2).sometimes('reverse')

pp >> play('ppp',dur=PDur(3,16)).sometimes('reverse')
pp >> play('ooooo',dur=PDur(5,16)).sometimes('reverse')
pp >> play('X-[- ][- ][- ][- ][- ]',dur=PDur(7,19)).sometimes('reverse')

print(SynthDefs)

Clock.bpm = 60

ee >> keys(P(0,3)-6, oct=4,amp=3)

kx >> marimba(P(0,2,4)-12,dur=1/4*PDur(7,132))
ky >> marimba(P(0,2,4)-P[16,14,16,16], delay=0.5)


tt >> squish(P[0,2,4],lpf=200,dur=PDur(3,16)).sometimes('reverse')

kk >> glass([[0,2,4]]).sometimes('reverse')

zz >> scatter([0,2,4],dur=[4,2,2])
zz.stop()
qq >> creep([[0,2,4]],sus=2, amp=0.05)
qq.stop()
ss >> blip([P(0,2,4), P(0,3,5)], sus=2, amp=0.2)

qq.stop()
