bp >> blip(-14, sus=8, dur=PDur(8,9)/var([1,8],4),lpf=200)
k1 >> play("X ",sample=4)
c1 >> play("---(-----9)", sample=var([0,1,2],1.5), dur=PDur(7,9)|rest(2))
    
