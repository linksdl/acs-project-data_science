# -*- coding: utf-8 -*-
"""
Created on 26 Sep 2018

How to use chardet to detect a text file's encoding

@author: Roy Ruddle
"""
import chardet

#
# Main program
#
input_filename = 'teaching value distributions.csv' # 'teaching data type.csv' #'YOUR FILENAME' # A file name

read_in_chunks = True # True or False
confidence_level = 0.9 # 0.0 to 1.0
result = None

try:    
    with open(input_filename, "rb") as fin:

        if read_in_chunks:

            while True:

                try:
                    chunk_size = 1024
                    rawdata = fin.read(chunk_size)
                    
                    if len(rawdata) > 0:
                        result = chardet.detect(rawdata)
                        
                        if result['confidence'] >= confidence_level:
                            break
                        else:
                            result = None

                    else:
                        break

                except Exception as e:
                    raise

        else:

            try:
                rawdata = fin.read()
                
                if len(rawdata) > 0:
                    result = chardet.detect(rawdata)

            except Exception as e:
                raise

except Exception as e:
    raise
else:
    print(result)

