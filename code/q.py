
x1 >> play("V-O-")
k1 >> glass(P*(P*(0,2,4,6,7,9)), dur=PDur(5,16), amp=0.5, lpf=500)
l0 >> pasha(P/(-8,0,7,12)*3|P[1:8].stutter().reverse(),dur=PEuclid(3,16), echo=3, lpf=1100).every(8, "reverse")
e0 >> dbass(P[0,2,4,3,5],lpf=200,dur=PDur(5,16),amp=3,oct=4)
p1 >> play('X-o-', dry=2)
b1 >> play('  ci', dur=PDur(2,8))
q9 >> play(' o -- o eEO ', sample=P*[0,2,4,0,0]).every(31, "stutter")


d2 >> play("(X )( X)N{ xv[nX]}", drive=0.2, lpf=var([0,40],[28,4]), rate=PStep(P[5:8],[-1,-2],1)).sometimes("sample.offadd", 1, 0.75)

cg >> play('x-o-')
oo >> blip(P(-2,4,6)*[-1,-2,0,0,-2,-1], delay=0.5, echo=0.5, room=0.9, dur=PDur(3,8), oct=P[5,4,4,4,3,4,4,5,4,4,2], amp=0.5)
print(SynthDefs)

dd >> dub(P[0],dur=PDur(5,16) )


n8 >> pads(P*(2,0,2), amp=0.5)
n8.stop()

