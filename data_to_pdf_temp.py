# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 18:43:29 2021

@author: Thomas Phelan

This will take input data as a CSV or TXT from LTSpice. 
It will generate a bare bones LaTEx report with the data visaully represented
for furhter editing in Tex.

DO NOT CHANGE ANY CODE EXCEPT FOR THE MANUAL INPUT VARIABLES AT THE BOTTOM
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylatex
from pylatex import Document, Section, Subsection, Tabular
from pylatex import Math, TikZ, Axis, Plot, Figure, Matrix, Alignat
from pylatex.utils import italic, bold
import os

def round_off(number, sigfigs=4):
    """
    rounds off 
    """
    return('{:g}'.format(float('{:.{p}g}'.format(number, p=sigfigs)))) 

def tidy_up(df, sigfigs=4):
    """

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
        
def render_plot(df, x_axis, Title, Intro, Caption):
    """
    Generates a line plot from the dataframe, saves as .png
    
    """   
    plt = df.plot.line(x=x_axis, title = Title)
    fig = plt.get_figure()
    fig.savefig(Title+' plot.png')

def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
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
    return ax.get_figure(), ax

def PDF_gen(df, Title, Intro, Caption, Graph, Table):
    """
Saves a PDF and TEX file to the directory

    """
    doc = Document(documentclass='report')
    geometry_options = {"tmargin": "2cm", "lmargin": "3cm", "rmargin": "3cm"}
    doc = Document(geometry_options=geometry_options)

    with doc.create(Section(Title+' table')):
        doc.append(Intro)
    if Table:
        fig,ax = render_mpl_table(df, header_columns=0, col_width=2.0)
        fig.savefig(Title+ " table.png")    
        with doc.create(Subsection('Tabulated Data')):
            with doc.create(Figure(position='h!')) as rxplot:
                rxplot.add_image(Title+' table.png', width='250px')
                rxplot.add_caption(italic(Caption))
    if Graph: 
        render_plot(df, x_axis, Title, Intro, Caption)
        with doc.create(Subsection('Graphical representation of data')):
            with doc.create(Figure(position='h!')) as rxplot:
                rxplot.add_image(Title+' plot.png', width='250px')
                rxplot.add_caption(italic(Caption))

    return(doc.generate_pdf(Title, clean_tex=False, compiler='pdflatex'))
     
##############################################################################
##########################################################
#                                                        #
# MANUALLY FILL IN THE VARIABLE FIELDS WITH DESIRED DATA #
#                                                        #
##########################################################

 ### FILENAME - FILE MUST BE IN THE WOKRING DIRECTORY ### 
Filename = 'Lab 1_5.txt'

Table = True ##True/False - do you want a table?
sigfigs = 4
Graph = True ##True/False - do you want a graph?
x_axis = "v1" ##If graph - What is the x axis?(must match dataframe label)
              ##Xaxis default can be none

df = make_df(Filename)
df = tidy_up(df, sigfigs)

### CHANGE DATAFRAME COLUMN NAMES USING RENAME CODE IF REQUIRED
df.rename(columns = {'Old':'New','Old':'New'}, inplace = True)              

### Following strings are used when generating the new PDF and TEX files
Title = 'Lab 1_5'
Intro = "big ol chunk of exlpainy about the data"
Caption = "Caption"
##############################################################################
### DO NOT CHANGE THE FOLLOWING CODE

PDF_gen(df, Title, Intro, Caption, Graph, Table)        