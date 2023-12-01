import streamlit as st
import AleonaInfo as AI


#Welcome Page
st.set_page_config(page_title="Welcome To Aleona")
def welcome():
    st.header("Welcome to Aleona!")
    #mapSlider = st.slider("Map Type", 0, 1, 2
    mapType = st.selectbox(
        "Select map type",
        options = ["Political Map", "Province Map", "Biome Map", "Religion Map"])
    if mapType == "Political Map":
        mapType = AI.politicalMap
        st.image(mapType)
    elif mapType == "Province Map":
        mapType = AI.provinceMap
        st.image(mapType)
    elif mapType == "Biome Map":
        mapType = AI.biomeMap
        st.image(mapType)
    elif mapType == "Religion Map":
        mapType = AI.religionMap
        st.image(mapType)
    
    st.write(AI.welcome+AI.welcome2)
        
    st.write("---")

welcome()

    
def flamontQuiz():
    st.header("Flamont Quiz")
    
    score = 0
    Flamont = "Red, Black, Gold"
    Marshlen = "Green, Purple, Gold"
    Inferna = "Blue, Black, Gold, White"
        
    with st.form("Flamont_Quiz", clear_on_submit=True):
        question1 = st.radio(
            "How many Provinces does Flamont have?",
            ["7", "5", "4"],
            index = None
            )
        question2 = st.radio(
            "This country's top soldiers are call the?",
            ["The Elders", "The Pillars", "Infernal Knights"],
            index = None
            )

        question3 = st.radio(
            "What is the currency of Flamont",
            ["Marsh", "Drac", "Royal"],
            index = None
            )
        question4 = st.radio(
            "The dominate religion of Flamont is?",
            ["Andrean Faith", "Cadenth Faith", "Dycan Fellowship"],
            index = None
            )
        question5 = st.radio(
            "The colors of Flamont's flag are?",
            [Flamont, Inferna, Marshlen],
            index = None
            )
        submitted = st.form_submit_button("Submit")

    if submitted:
        if question1 == "5":
            score += 1
        if question2 == "The Pillars":
            score += 1
        if question3 == "Royal":
            score += 1
        if question4 == "Dycan Fellowship":
            score += 1
        if question5 == Flamont:
            score += 1
        return st.write("You scored {} out of 5!".format(score))

def infernaQuiz():
    st.header("Inferna Quiz")

    score = 0
    maxScore = 5
    Inferna = "Blue, Black, Gold, White"

    with st.form("Inferna_Quiz", clear_on_submit=True):
        question1 = st.radio(
            "What is the main agricultural export of Inferna?",
            ["Wheat", "Corn", "Potatoes", "Oranges"],
            index = None
            )
        question2 = st.radio(
            "What is the population of Inferna?",
            ["1.2 million sqaure miles", "2.1 million square miles", "3 million square miles"],
            index = None
            )
        question3 = st.radio(
            "What is the capital of Inferna?",
            ["Cadenth", "Riverston", "Helen"],
            index = None
            )
        question4 = st.radio(
            "Which of these is not a province of Inferna?",
            ["Pythona", "Ladon", "Khun", "Bragapin"],
            index = None
            )
        question5 = st.radio(
            "True or False: Inferna has the largest plains biome in Aleona.",
            ["True", "False"],
            index = None
            )
        submitted = st.form_submit_button("Submit")
            
        if submitted:
            if question1 == "Wheat":
                score += 1
            if question2 == "1.2 million sqaure miles":
                score += 1
            if question3 == "Helen":
                score += 1
            if question4 == "Bragapin":
                score += 1
            if question5 == "True":
                score += 1
            return st.write("You scored {} out of 5!".format(score))

def marshlenQuiz():
    st.header("Marshlen Quiz")
    score = 0

    with st.form("Marshlen_Quiz", clear_on_submit=True):
        question1 = st.radio(
            "What is the symbol of Marshlen?",
            ["World Tree", "Tree of Life", "Swamp Tree"],
            index = None
            )
        question2 = st.radio(
            "How many stars are on the Marshlen Flag?",
            ["6", "7", "8", "5"],
            index = None
            )
        question3 = st.radio(
            "Where is the capital of Marshlen located?",
            ["Bragapin", "Perston", "Carlister", "Botherston"],
            index = None
            )
        question4 = st.radio(
            "True or False: Marshlen is the youngest country in Aleona.",
            ["True", "False"],
            index = None
            )
        question5 = st.radio(
            "How many religions are practiced in Marshlen?",
            ["7", "2", "3", "5"],
            index = None
            )
        submitted = st.form_submit_button("Submit")
        if submitted:
            if question1 == "Tree of Life":
                score += 1
            if question2 == "6":
                score += 1
            if question3 == "Carlister":
                score += 1
            if question4 == "False":
                score += 1
            if question5 == "5":
                score += 1
            return st.write("You scored {} out of 5!".format(score))
                
        
def quiz():
    st.header("Fun Quiz!")
    st.write("Take this fun little quiz to see what you've learned! Use the buttons below to choose which country you'd like to quiz over.")
    tab1, tab2, tab3 = st.tabs(["Flamont", "Inferna", "Marshlen"])

    with tab1:
        flamontQuiz()
    with tab2:
        infernaQuiz()
    with tab3:
        marshlenQuiz()
quiz()
    
            
            
            
        
                
            
        
