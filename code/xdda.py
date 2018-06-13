Clock.update_tempo(103)
b1 >> play(P["(x-)(y-)"].bubble())
d1 >> play(P["V  V"] & P[" *  "] & P["[ m] "])
p1 >> keys([(0,2,5)]+[1,3], dur=[rest(2),2]) # needs work
p2 >> blip(PTri(8), dur=PDur(3,8).stretch(8)|P[rest(1)])

b1.stop()
d1.stop()
p1.stop()
p2.stop()

# modulations
p1 >> piano(P[(0,2,5)]|[1,3], dur=[rest(2),2], amp=0.8, echo=3)
p1 >> piano([(0,2,5)]+[1,3], dur=P[rest(2)]|PDur(3,8), amp=0.8, echo=3)
p2 >> blip(PTri(8), dur=PDur(3,8).stretch(8)|P[rest(1)], echo=1.75)

print(PDur(3,8)|P[rest(1)])
print(PDur(3,8).stretch(7)|P[rest(1)])
p1.stop()
print([(0,2,5)]+[1,3]+[5])

#print(P["(x-)(y-)"].amen())
Clock.clear()

print(SynthDefs)

print(Player.get_attributes())

# notes
print(BufferManager())

# Angle brackets combine patterns to be play simultaneously

# You can layer two patterns together
d1 >> play(P["x-o-"] & P[" ** "])

d1.stop()


# And change effects applied to all the layered patterns at the same time
d1 >> play(P["x-o-"] & P[" **"], room=0.5)

d1 >> play("x[--]xu[--]x", sample=(d1.degree=="x"))
d1 >> play("x[--]xu[--]x", sample=(d1.degree=="x")*2 + (d1.degree=="-")*5)
