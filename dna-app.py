from altair.vegalite.v4.api import sequence
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


st.image("dna-logo.jpg",use_column_width=True)

st.header('Enter DNA sequence')
sequence_input=">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"
sequence=st.text_area("Sequence input",sequence_input,height=150)
sequence
sequence=sequence.splitlines()
sequence

sequence=sequence[1:]
sequence=''.join(sequence)
sequence

st.write("""
# DNA  Nucleotide Count Web App
This app counts the nucleotide composition of query DNA!
***
""")

st.header('Output (DNA Counts)')
st.subheader('1.Print Dictionary')

def DNA_nucleotide(seq):
    d=dict([
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('C',seq.count('C')),
        ('G',seq.count('G'))
    ])
    return d
X=DNA_nucleotide(sequence)
X

### 2. Print text
st.subheader('2. Print text')
st.write('There are',str(X['A']),'adenine(A)')
st.write('There are',str(X['T']),'thymine (T)')
st.write('There are',str(X['G']),'guanine(G)')
st.write('There are',str(X['C']),'cytosine(C)')



st.subheader('3.Display Dataframe')
df=pd.DataFrame.from_dict(X,orient='index')
df
df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('4.Display Bar Chart using Altair')


