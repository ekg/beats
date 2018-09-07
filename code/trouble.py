
Scale.Root = -2


Clock.bpm=100

Scale.default.set("major", tuning=Tuning.just)


x0 >> play("-")
x0.stop()
m1 >> play(P["SEX BOTS"].bubble(), amp=1,lpf=472)
r1 >> sinepad(P[0,-0.015,P*[4,4,5,2],-2,-1.013], dur=PDur(2,5), amp=1)


x0 >> play("-", sample=P[0,1,3,8,9]+P*(0,2), amp=0.5)
x0 >> play(" (- )  ", sample=P[0,1,3,8,9]+P*(0,2), amp=0.5)
m1 >> play(P["SEX B.O.T.S."]., amp=1,lpf=472)
r1 >> sinepad(P[0,-0.015,P*[4,4,5,2],-2,-1.013], dur=PDur(2,5), amp=1)


x0 >> play(" (- )  ", sample=P[0,1,3,8,9]+P*(0,2), amp=0.5)
m1 >> play(P["S-E-X B.O.T.S."], amp=0.8,lpf=272)
r1 >> sinepad(P[0,-0.015,P*[4,4,5,2],-2,-1.013], dur=PDur(2,5), amp=1)

