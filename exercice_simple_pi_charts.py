#!/usr/bin/env python
# -*- coding: utf-8 -*-
#===============================================================================
#
# Copyright (c) 2017 <stakeholder> All Rights Reserved
#
#
# File: /Users/hain/ai/matplotlib-get-started/exercice_1.py
# Author: Hai Liang Wang
# Date: 2017-07-05:11:15:01
#
#===============================================================================

"""
   TODO: Module comments at here
   
   
"""

__copyright__ = "Copyright (c) 2017 . All Rights Reserved"
__author__    = "Hai Liang Wang"
__date__      = "2017-07-05:11:15:01"


import os
import sys
curdir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(curdir)
import numpy as np
import matplotlib.pyplot as plt

def exercice_2():
    '''
    Changing colors and line widths
    '''
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=1.0, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="green", linewidth=1.0, linestyle="-")

    # Set x limits
    plt.xlim(-4.0,4.0)

    # Set x ticks
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # Set y limits
    plt.ylim(-1.0,1.0)

    # Set y ticks
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    # Save figure using 72 dots per inch
    plt.savefig("/tmp/exercice_2.png",dpi=72)

    # Show result on screen
    plt.show()

def exercice_3():
    '''
    Setting limits
    '''
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

    # Set x limits
    plt.xlim(X.min()*1.1, X.max()*1.1)

    # Set x ticks
    plt.xticks(np.linspace(-4,4,9,endpoint=True))

    # Set y limits
    plt.ylim(C.min()*1.1,C.max()*1.1)

    # Set y ticks
    plt.yticks(np.linspace(-1,1,5,endpoint=True))

    # Save figure using 72 dots per inch
    plt.savefig("/tmp/exercice_3.png",dpi=72)

    # Show result on screen
    plt.show()

def exercice_4():
    '''
    Setting ticks
    '''
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

    # Set x limits
    plt.xlim(X.min()*1.1, X.max()*1.1)

    # Set x ticks
    plt.xticks( [-np.pi, -np.pi/2, 0, np.pi/2, np.pi])

    # Set y limits
    plt.ylim(C.min()*1.1,C.max()*1.1)

    # Set y ticks
    plt.yticks([-1, 0, +1])

    # Save figure using 72 dots per inch
    plt.savefig("/tmp/exercice_4.png",dpi=72)

    # Show result on screen
    plt.show()

def exercice_5():
    '''
    Setting tick labels
    '''
    # Create a new figure of size 8x6 points, using 100 dots per inch
    plt.figure(figsize=(8,6), dpi=80)

    # Create a new subplot from a grid of 1x1
    plt.subplot(111)

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    # Plot cosine using blue color with a continuous line of width 1 (pixels)
    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")

    # Plot sine using green color with a continuous line of width 1 (pixels)
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")

    # Set x limits
    plt.xlim(X.min()*1.1, X.max()*1.1)

    # Set x ticks
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    # Set y limits
    plt.ylim(C.min()*1.1,C.max()*1.1)

    # Set y ticks
    plt.yticks([-1, 0, +1],
        [r'$-1$', r'$0$', r'$+1$'])

    # Save figure using 72 dots per inch
    plt.savefig("/tmp/exercice_5.png",dpi=72)

    # Show result on screen
    plt.show()

def exercice_6():
    '''
    Moving spines
    '''
    plt.figure(figsize=(8,5), dpi=80)
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-")


    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min()*1.1,C.max()*1.1)
    plt.yticks([-1, 0, +1],
        [r'$-1$', r'$0$', r'$+1$'])

    plt.show()

def exercice_7():
    '''
    Adding a legend
    '''
    plt.figure(figsize=(8,5), dpi=80)
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
    plt.legend(loc='upper left', frameon=False)

    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min()*1.1,C.max()*1.1)
    plt.yticks([-1, 0, +1],
        [r'$-1$', r'$0$', r'$+1$'])

    plt.show()


def exercice_8():
    '''
    Annotate some points
    '''
    plt.figure(figsize=(8,5), dpi=80)
    ax = plt.subplot(111)

    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")
    plt.legend(loc='upper left', frameon=False)

    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
        [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min()*1.1,C.max()*1.1)
    plt.yticks([-1, 0, +1],
        [r'$-1$', r'$0$', r'$+1$'])

    t = 2*np.pi/3
    plt.plot([t,t],[0,np.cos(t)], color ='blue', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.cos(t),], 50, color ='blue')

    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                xy=(t, np.sin(t)), xycoords='data',
                xytext=(+10, +30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t,t],[0,np.sin(t)], color ='red', linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.sin(t),], 50, color ='red')

    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                xy=(t, np.cos(t)), xycoords='data',
                xytext=(-90, -50), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.show()

def exercice_9():
    '''
    Devil is in the details
    '''
    plt.figure(figsize=(8,5), dpi=80)
    ax = plt.subplot(111)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
    C,S = np.cos(X), np.sin(X)

    plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
    plt.plot(X, S, color="red", linewidth=2.5, linestyle="-",  label="sine")


    plt.xlim(X.min()*1.1, X.max()*1.1)
    plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
            [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

    plt.ylim(C.min()*1.1,C.max()*1.1)
    plt.yticks([-1, +1],
            [r'$-1$', r'$+1$'])

    plt.legend(loc='upper left', frameon=False)

    t = 2*np.pi/3
    plt.plot([t,t],[0,np.cos(t)],
            color ='blue',  linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.cos(t),], 50, color ='blue')
    plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
                xy=(t, np.sin(t)),  xycoords='data',
                xytext=(+10, +30), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    plt.plot([t,t],[0,np.sin(t)],
            color ='red',  linewidth=1.5, linestyle="--")
    plt.scatter([t,],[np.sin(t),], 50, color ='red')
    plt.annotate(r'$\cos(\frac{2\pi}{3})=-\frac{1}{2}$',
                xy=(t, np.cos(t)),  xycoords='data',
                xytext=(-90, -50), textcoords='offset points', fontsize=16,
                arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

    for label in ax.get_xticklabels() + ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=1 ))

    plt.savefig("/tmp/exercice_9.png",dpi=72)
    plt.show()

if __name__ == '__main__':
    exercice_9()