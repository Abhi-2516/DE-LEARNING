import pandas as pd
import streamlit as st

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Book Recommendation Engine",
    page_icon="📚",
    layout="wide"
)


# ==========================================================
# LOAD DATASET
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("books.csv")


df = load_data()


# ==========================================================
# TF-IDF MODEL
# ==========================================================

@st.cache_resource
def create_model(data):

    # Convert descriptions into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        data["description"]
    )

    # Calculate cosine similarity
    cosine_matrix = cosine_similarity(
        tfidf_matrix,
        tfidf_matrix
    )

    return vectorizer, cosine_matrix


vectorizer, cosine_matrix = create_model(df)


# ==========================================================
# CREATE TITLE -> INDEX MAPPING
# ==========================================================

indices = pd.Series(
    df.index,
    index=df["title"]
)


# ==========================================================
# RECOMMENDATION FUNCTION
# ==========================================================

def get_recommendation(
    title,
    number_of_recommendations=5
):

    # Check whether the selected book exists
    if title not in indices:
        return pd.DataFrame()

    # Get index of selected book
    idx = indices[title]

    # Get similarity scores
    sim_scores = list(
        enumerate(cosine_matrix[idx])
    )

    # Sort by similarity score
    sim_scores = sorted(
        sim_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Remove the selected book itself
    sim_scores = sim_scores[
        1:number_of_recommendations + 1
    ]

    # Get book indexes
    book_indices = [
        item[0]
        for item in sim_scores
    ]

    # Get similarity scores separately
    similarity_scores = [
        item[1]
        for item in sim_scores
    ]

    # Get recommended books
    recommendations = df.iloc[
        book_indices
    ][
        [
            "title",
            "genre",
            "author",
            "description"
        ]
    ].copy()

    # Add similarity percentage
    recommendations["similarity"] = [
        round(score * 100, 2)
        for score in similarity_scores
    ]

    return recommendations


# ==========================================================
# HEADER
# ==========================================================

st.title("📚 Book Recommendation Engine")

st.markdown(
    """
    ### Find your next book

    Select a book you like and the recommendation engine
    will find books with similar descriptions using
    **TF-IDF and Cosine Similarity**.
    """
)

st.divider()


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.header("⚙️ Recommendation Settings")

selected_book = st.sidebar.selectbox(
    "Select a book",
    df["title"].tolist()
)

number_of_recommendations = st.sidebar.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)

recommend_button = st.sidebar.button(
    "🔍 Get Recommendations",
    use_container_width=True
)


# ==========================================================
# DATASET INFORMATION
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "📚 Total Books",
        len(df)
    )

with col2:
    st.metric(
        "🎭 Genres",
        df["genre"].nunique()
    )

with col3:
    st.metric(
        "✍️ Authors",
        df["author"].nunique()
    )


st.divider()


# ==========================================================
# SELECTED BOOK
# ==========================================================

st.subheader("📖 Selected Book")

selected_book_data = df[
    df["title"] == selected_book
].iloc[0]

col1, col2 = st.columns([1, 2])

with col1:

    st.markdown(
        f"### {selected_book_data['title']}"
    )

    st.write(
        f"**Genre:** {selected_book_data['genre']}"
    )

    st.write(
        f"**Author:** {selected_book_data['author']}"
    )

with col2:

    st.write(
        selected_book_data["description"]
    )


st.divider()


# ==========================================================
# RECOMMENDATIONS
# ==========================================================

st.subheader("✨ Recommended Books")

# Show recommendations when button is clicked
if recommend_button:

    recommendations = get_recommendation(
        selected_book,
        number_of_recommendations
    )

    if recommendations.empty:

        st.error(
            "Sorry, this book could not be found."
        )

    else:

        for _, book in recommendations.iterrows():

            with st.container(border=True):

                col1, col2 = st.columns(
                    [3, 1]
                )

                with col1:

                    st.markdown(
                        f"### 📕 {book['title']}"
                    )

                    st.write(
                        f"**Genre:** {book['genre']}"
                    )

                    st.write(
                        f"**Author:** {book['author']}"
                    )

                    st.write(
                        book["description"]
                    )

                with col2:

                    st.metric(
                        "Similarity",
                        f"{book['similarity']}%"
                    )

else:

    st.info(
        "👈 Select a book from the sidebar and "
        "click **Get Recommendations**."
    )


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "Built with Python, Streamlit, Pandas and Scikit-learn"
)