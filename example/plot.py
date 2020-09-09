#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 14:58:21 2018

@author: bruce
"""

import matplotlib.pyplot as plt
plt.switch_backend('agg')
import numpy as np
import pandas as pd
import sys
sys.path.append('/home/zwu/Dropbox/code/research/ResearchPlot/')
import ResearchPlot
import sys

@ResearchPlot.aps
def plot_example():

    #colors=ResearchPlot.Roma(10)

    data=pd.read_csv("test_data.csv",header=None,sep="\s+",skiprows=1)

    linestyle_MD=ResearchPlot.linestyles(hollow_styles=[True],lines=["--"],markeredge=0.5)


    #create the plot object
    fig, ax = plt.subplots(nrows=1)

    #plot data
    for i in range(10):
        ax.plot(data[0],data[1]*(i*10+1),markersize=3,linewidth=1,**next(linestyle_MD),label=str(i))

    #set the plot parameters
    ax.legend(loc="best",ncol=2)
    
    #ax.set_xscale("log")
    #ax.set_yscale("log")
    ax.set_xlabel(r"time [ps]")
    ax.set_ylabel(r"$g_{1}(t)$")
    
    #ResearchPlot.set_locator(ax.xaxis,numticks=10)
    #ResearchPlot.set_locator(ax.yaxis,numticks=5)

    #ax.set_xlim(1e3,1e8)
    #ax.set_ylim(1,1000000)
    fig.tight_layout(pad=0.15) 
    fig.savefig("test_color_Default.png")

plot_example()
