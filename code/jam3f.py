
Clock.bpm = 96
mantra="W AR T EN BU RG"#"JAH MAN"
bassline = [1,2,3,0]
d2 >> bass([bassline,rest(len(mantra) - len(bassline))], dur=2)
d1 >> play(mantra, dur=1/2, amp=var([0,1],0.5), sample=2)
d3 >> play(mantra, dur=1/2, pan=var([-1,1],2.5), sample=var(P[:6],len(mantra)))


pp >> pads([(0,2,4)]|P/[4,1,5]+PEuclid(5,len(mantra))*P[:len(mantra)].shuffle(), room=0.5, dur=4, amp=0.5, lpf=400)