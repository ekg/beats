Clock.bpm=100
Clock.nudge=var([0,0.1,0,0.15], 1/4)
#Root.default=var([0,2,4],8)
Root.default = 0
Scale.default = 'dorian'
h9 >> play('<X ><  + ><[ -&]><  * >', amp=[0.7,0.8,0.9,0.7,0.8,0.9])
dx >> bass(P[8,7,6,4,5,2,2,2,1,1,1,0,0,0,0,0,0], delay=0.5, dur=4, lpf=800, oct=4, sus=1.5,amp=0.6)
