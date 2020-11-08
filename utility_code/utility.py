import numpy as np
import sklearn 
import pandas as pd
import matplotlib.pyplot as plt
from itertools import chain

class utils(object):
    
    #splits dataframe into 2 peices and ensures each segment of data belong to only one split
    def split_dataframe(dataframe,percent_split,segment_length=1):
        num_segments = int(dataframe.shape[0] / segment_length)
        num_segment_split1 = int(num_segments * percent_split / 100)
        split1_size = num_segment_split1 * segment_length
        return(dataframe.iloc[:split1_size,:] ,  dataframe.iloc[split1_size:,:])
    
    #get column indices from column names
    def get_column_indices(dataframe,col_names):
        indices = []
        for c in col_names:
            indices.append(dataframe.columns.get_loc(c))
        return indices
    
    #return a row-wise concatenation of the dataframe
    #arg can be a slice object or array of desired indices
    def flatten_dataframe(dataframe,row_arg,col_arg):
        return list(chain(*dataframe.iloc[row_arg,col_arg].values.tolist()))
    
    #appends the row to the dataframe and titles it "s (day d)"
    def dataframe_append_row(dataframe,row,s,d):
        row_name = s + " (day " + str(d) + ")"
        dataframe.loc[row_name,:] = row     
        
    #replaces row-names of a dataframe1 with row-names from dataframe2
    #keeps only columns from dataframe2
    def dataframe_copy_rows_and_filter_columns(dataframe1,dataframe2):
        dataframe1.index = dataframe2.index
        return dataframe1[dataframe2.columns]
