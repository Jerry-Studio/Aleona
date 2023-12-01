import streamlit as st
import AleonaInfo as AI
st.set_page_config(page_title="Inferna")

def infernaPage(aDict):
    st.header("Inferna")
    st.image(AI.infernaFlag)
    st.write(AI.Inferna1 + AI.Inferna2 + AI.Inferna3)

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
    
        
    
infernaPage(AI.InfernaDict)
