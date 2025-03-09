import streamlit as st
import pandas as pd
import pickle
import requests
from fuzzywuzzy import process

st.title("🎬 Movie Recommender System")

# Load saved model data
try:
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
except FileNotFoundError:
    st.error("Required data files (movies.pkl or similarity.pkl) not found. Please run the Jupyter notebook first to generate these files.")
    st.stop()
except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.stop()

# Convert to DataFrame
movies_df = pd.DataFrame(movies)
movies_df['title'] = movies_df['title'].str.lower()

# Function to find closest movie title match
def find_closest_title(title):
    # Get list of all movie titles
    all_titles = movies_df['title'].tolist()
    
    # Find closest match
    closest_match = process.extractOne(title.lower(), all_titles)
    
    if closest_match and closest_match[1] >= 80:  # If similarity score is at least 80%
        return closest_match[0]
    return None

# Function to recommend movies
def recommend(movie):
    movie = movie.lower().strip()
    
    if movie not in movies_df['title'].values:
        return {"error": "Movie not found in database"}

    index = movies_df[movies_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommendations = []
    for i in distances[1:6]:
        movie_title = movies_df.iloc[i[0]]['title']
        movie_id = movies_df.iloc[i[0]]['id']
        similarity_score = i[1]
        
        recommendations.append({
            'title': movie_title.title(),
            'id': movie_id,
            'similarity': similarity_score
        })
    
    return {"recommendations": recommendations}

with st.sidebar:
    st.header("About This Recommender")
    st.write("""
    This movie recommender uses content-based filtering to suggest movies similar to your input.
    
    It analyzes:
    - Movie genres
    - Plot keywords
    - Movie overview
    
    The similarity is calculated using cosine similarity between movie feature vectors.
    """)

# Use session state to manage app flow
if 'show_recommendations' not in st.session_state:
    st.session_state.show_recommendations = False
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = []

st.write("Enter a movie name to get similar recommendations!")
# Add key parameter and on_change=None to disable automatic updates
title = st.text_input("🎥 Enter a movie name:", key="movie_input", on_change=None).strip()

# Create a form to prevent Enter key from triggering
with st.form(key='movie_form'):
    # Add a hidden text input to prevent form submission on Enter
    st.text_input("", value="", key="hidden", label_visibility="collapsed")
    submit = st.form_submit_button("🔍 Recommend")
    if submit:
        if not title:
            st.warning("Please enter a movie title")
        else:
            result = recommend(title)
            
            if "error" in result:
                st.session_state.show_recommendations = False  # Clear previous recommendations
                st.error(result["error"])
            else:
                st.session_state.show_recommendations = True
                st.session_state.recommendations = result["recommendations"]

# Display recommendations if available
if st.session_state.show_recommendations and st.session_state.recommendations:
    display_title = title.title()
    st.subheader(f"🎬 Movies similar to '{display_title}':")
    
    for i, movie in enumerate(st.session_state.recommendations):
        col1, col2 = st.columns([1, 3])
        
        with col1:
            st.write(f"**#{i+1}**")
        
        with col2:
            st.write(f"**{movie['title']}**")
            st.write(f"Similarity Score: {movie['similarity']:.2f}")
        
        st.divider()
