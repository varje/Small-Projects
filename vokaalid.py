def topeltvokaalide_arv(sõne):
    s='_'+sõne+'_'
    i=0
    a=0
    for i in range (len(sõne)):
        if s[i] in 'aeiouõäöü' and s[i]==s[i+1] and s[i]!=s[i-1] and s[i]!=s[i+2]:
            a+=1
    return a
print(topeltvokaalide_arv("kapsas"))
print(topeltvokaalide_arv("piiripiiga"))
print(topeltvokaalide_arv("puuõõs"))
print(topeltvokaalide_arv("bäää"))
    