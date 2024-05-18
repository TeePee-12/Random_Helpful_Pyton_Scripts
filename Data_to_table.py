# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:43:29 2021

@author: Thomas Phelan

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def round_off(number, sigfigs=4):
    """
    rounds off 
    """
    return('{:g}'.format(float('{:.{p}g}'.format(number, p=sigfigs)))) 

def tidy_up(df, sigfigs=4):
    """
    Calls roundoff to work on the dataframe
    """
    for i in (range(len(df.columns))):
        for j in (range(len(df))):
            df.iat[j,i] = round_off(df.iat[j,i], sigfigs)
    return(df)        

def make_df(Filename):
    """
Builds the dataframe

    """
    if Filename[-3:] == 'txt':
        return(pd.read_csv(Filename, delimiter = "\t"))
    elif Filename[-3:] == 'csv':
        return(pd.read_csv(Filename))
    else:
        assert Filename[-3:] == 'csv' or Filename[-3:] == 'txt', 'Only Accepts .TXT or .CSV'
        


def render_mpl_table(data, Title, col_width=3.0, row_height=0.625, font_size=14,
                     header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
                     bbox=[0, 0, 1, 1], header_columns=0,
                     ax=None, **kwargs):
    """
    Takes a dataframe and turns it into a visually appealling table
    
    """
    if ax is None:
        size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
        fig, ax = plt.subplots(figsize=size)
        ax.axis('off')
    mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
    mpl_table.auto_set_font_size(False)
    mpl_table.set_fontsize(font_size)

    for k, cell in mpl_table._cells.items():
        cell.set_edgecolor(edge_color)
        if k[0] == 0 or k[1] < header_columns:
            cell.set_text_props(weight='bold', color='w')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
        fig.savefig(Title+ " table.png")
 
##############################################################################
##############################################################################

Filename = 'lab2_vin_vs_vout.csv'
sigfigs = 4

df = make_df(Filename)
df = tidy_up(df, sigfigs)
df.rename(columns = {'Old':'New','Old':'New'}, inplace = True) 

render_mpl_table(df, Filename[:-4], header_columns=0, col_width=2.0)