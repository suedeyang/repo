from altair.vegalite.v4.api import sequence
import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image


st.header('Enter DNA sequence')
sequence_input=">DNA Query 2 \nGAACA"
sequence=st.text_area("Sequence input",sequence_input,height=150)
sequence=sequence.splitlines()
#sequence

sequence=sequence[1:]
sequence=''.join(sequence)

sequence
