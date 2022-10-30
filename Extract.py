import pdfplumber
import os
import camelot
import pandas as pd
import numpy as np
from pathlib import Path



class Extract:
    def __init__(self, filename, page):
        self.filename = filename
        self.page = page

    def find_Tabs(self):
        pdf = pdfplumber.open(self.filename)
        p0 = pdf.pages[int(self.page) - 1]
        tables = p0.find_tables()
        coordinate = []
        for table in tables:
            coordinate.append(table.bbox)
        return coordinate, p0.height
    
    def extract_one_table_from_page(self):
        df=[]
        tab = camelot.read_pdf(self.filename, pages=self.page,flavor='stream', edge_tol=500, row_tol=5)
        df.append(tab[0].df)
        return df
    
    def extract_multiple_tables_from_page(self):
        Tables = []
        coordinate, height = Extract.find_Tabs(self)
        for cor in coordinate:
           table_areas = str(cor[0])+", "+str(height-cor[1]) +", "+str(cor[2])+", "+str(height-cor[3])
           ac = camelot.read_pdf(self.filename, pages=str(self.page), flavor='stream', edge_tol=500, row_tol=5, table_areas=[table_areas])
           Tables.append(ac[0].df)
        return Tables
    
    def save_to_disk(self,Tables):
        dir =os.path.splitext(self.filename)[0]
        os.mkdir(dir)
        os.chdir(dir)
        i=1
        for df in Tables:
            df.to_excel(f"table{i}.xlsx")
            i = i+1
        