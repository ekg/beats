riddim=P["PARKSEX"]
b0 >> play(P["x-v-"].stretch(len(riddim)))
b1 >> play(riddim, amp=PDur(6,7))
Scale.default="minorPentatonic"
p1 >> piano(P(0,[3,2,5],[4,6,3])+P[:4].stretch(len(riddim)), delay=0, oct=5, dur=PDur(3,len(riddim)), sus=1.2,amp=PEuclid(5,len(riddim))*0.8, bit=0.1)
