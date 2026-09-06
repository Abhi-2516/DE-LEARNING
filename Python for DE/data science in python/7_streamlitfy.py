import pandas as pd

from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.model_selection import train_test_split
import streamlit as st


@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")

    X_train , X_test ,Y_train , Y_test = train_test_split(df['comment'] , df['label'] , test_size = 0.2, random_state= 42)

    model = Pipeline([
        
        ('tfidf' , TfidfVectorizer()),
        ('clf' , LogisticRegression())
    ])

    model.fit(X_train ,Y_train)

    return model

model = load_model()

st.title("YT comment analyzer : ")
st.write("Classify your comment as Toxic or supportive ")

user_input = st.text_area("enter an yt comment")

if user_input:
    prediction   = model.predict([user_input])[0]
    if prediction == "toxic":
        st.error("this is toxic  comment")
    else:
        st.success("Good comment")
    
