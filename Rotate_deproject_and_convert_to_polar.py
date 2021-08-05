#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from astropy.modeling import models, fitting
import matplotlib.pyplot as plt
from astropy.io import fits
from scipy.optimize import curve_fit
import math
import os
from scipy.interpolate import interp2d
from scipy import ndimage, misc


# In[ ]:


def tand(x):
    return math.tan(x * math.pi / 180)

def sind(x):
    return math.sin(x * math.pi / 180)

def cosd(x):
    return math.cos(x * math.pi / 180)


# In[ ]:


def converting(img,PA=0,inclination=0,center=None, final_radius=100,pw=360,r0=40,times=2):
    
    theta_ , R_ = np.meshgrid(np.linspace(0, 2*np.pi, pw), 
                            np.arange(0, final_radius))
    if center=None:
        center=[len(img)/2,len(img)/2]
    
    x=np.linspace(0, len(img)-1,len(img), dtype=int)
    y=np.linspace(0, len(img)-1,len(img), dtype=int)
    f=interp2d(x,y,img,kind='cubic')
    z2=[[[]for i in range(pw)]for i in range(final_radius)]
    theta=0
    while theta<90:
        r=1
        while r<final_radius:
            rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
            x=rr*cosd(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+PA)+center[0]
            y=rr*sind(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+PA)+center[1]
            z2[r][theta]=float(f(x,y))*((rr/r0)**times)

            r+=1
        theta+=1
    theta=90
    r=1
    while r<final_radius:
        rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
        x=(r*(cosd(inclination))*cosd(90+PA))+center[0]
        y=(r*(cosd(inclination))*sind(90+PA))+center[1]
        z2[r][theta]=float(f(x,y))*((rr/r0)**times)
        r+=1


    theta=91
    while theta<=180:
        r=1
        while r<final_radius:
            rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
            x=rr*cosd(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+180+PA)+center[0]
            y=rr*sind(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+180+PA)+center[1]
            z2[r][theta]=float(f(x,y))*((rr/r0)**times)

            r+=1
        theta+=1

    while theta<270:
        r=1

        while r<final_radius:
            rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
            x=rr*cosd(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+180+PA)+center[0]
            y=rr*sind(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+180+PA)+center[1]
            z2[r][theta]=float(f(x,y))*((rr/r0)**times)

            r+=1
        theta+=1

    theta=270
    r=1
    while r<final_radius:
        rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
        x=-(r*(cosd(inclination))*cosd(90+PA))+center[0]
        y=-(r*(cosd(inclination))*sind(90+PA))+center[1]
        z2[r][theta]=float(f(x,y))*((rr/r0)**times)
        r+=1
    theta=271
    while theta<360:
        r=1
        while r<final_radius:
            rr=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)
            x=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)*cosd(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+PA)+center[0]
            y=(r*((sind(theta)*cosd(inclination))**2+(cosd(theta))**2)**0.5)*sind(np.arctan(tand(theta)*cosd(inclination))*180/math.pi+PA)+center[1]
            z2[r][theta]=float(f(x,y))*((rr/r0)**times)
            r+=1
        theta+=1


    r=0
    theta=0
    while theta<360:
        z2[r][theta]=float(f(center[0],center[1]))
        theta+=1
    plt.imshow(z2, cmap= 'gray',origin='lower')
    return z2


# In[ ]:




