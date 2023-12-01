import streamlit as st
import AleonaInfo as AI
import pandas as pd
st.set_page_config(page_title="Flamont")

def flamontPage(aDict):
    st.header("Flamont")
    st.image(AI.flamontFlag)
    st.write(AI.Flamont1 + AI.Flamont2 + AI.Flamont3)

    st.write("---")
    st.subheader("General Info")

    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Capital", "Population", "Size", "Currency", "Symbol"])

    with tab1:
       st.write(aDict["Capital"])
    with tab2:
       st.write(aDict["Population"])
    with tab3:
       st.write(aDict["Size"])
    with tab4:
       st.write(aDict["Currency"])
    with tab5:
       st.write(aDict["Symbol"])
    
        
    
flamontPage(AI.FlamontDict)
