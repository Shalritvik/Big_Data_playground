#!/usr/bin/env python
import sys

# --------------------------------------------------------------------------
# Generate a random combination of titles and viewer counts, or channels
# --------------------------------------------------------------------------
chans   = ['ABC','DEF','CNO','NOX','YES','CAB','BAT','MAN','ZOO','XYZ','BOB']
sh1 =['Hot','Almost','Hourly','PostModern','Baked','Dumb','Cold','Surreal','Loud']
sh2 =['News','Show','Cooking','Sports','Games','Talking']
vwr =range(17,1053)

chvnm=sys.argv[1]  #get "view number/channel" argument
#if "n", output channels,
#if other letter, output view number

lch=len(chans)
lsh1=len(sh1)
lsh2=len(sh2)
lvwr=len(vwr)
ci=1
s1=2
s2=3
vwi=4
ri=int(sys.argv[3])#random seed
for i in range(0,int(sys.argv[2])):#get "number of lines" argument
    if chvnm=='n': #channel
        print('{0}_{1},{2}'.format(sh1[s1],sh2[s2],chans[ci]))
    else:#viewer number
        print('{0}_{1},{2}'.format(sh1[s1],sh2[s2],vwr[vwi])) 
    ci=(5*ci+ri) % lch   
    s1=(4*s1+ri) % lsh1
    s2=(3*s1+ri+i) % lsh2
    vwi=(2*vwi+ri+i) % lvwr
    if (vwi==4): 
        vwi=5
 