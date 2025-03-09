# 🎬 Enhanced Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on various features like genres, keywords, cast, crew, and overview.

## 🌟 Features

- **Content-based filtering** using movie metadata
- **Fuzzy matching** for movie titles to handle typos and variations
- **Diversity controls** to ensure varied recommendations
- **Similarity scores** to show how closely related recommendations are
- **User-friendly interface** built with Streamlit

## 🚀 System Features

1. **TF-IDF Vectorization**: Uses TF-IDF to give more weight to important terms and less to common terms
2. **Enhanced Recommendation Function**: Returns movie titles with similarity scores
3. **Simple UI**: Clean visualization of recommendations with similarity scores

## 🛠️ Installation

```bash
# Clone the repository
git clone <repository-url>
cd movie-recommendation-system

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 📊 How It Works

1. **Data Preprocessing**:
   - Merges movie data with credits data
   - Extracts features from genres, keywords, cast, crew, and overview
   - Processes text using stemming
   - Creates weighted feature vectors

2. **Recommendation Process**:
   - Converts input movie title to a feature vector
   - Calculates similarity with all other movies
   - Ranks movies by similarity score
   - Applies diversity filtering
   - Returns top 5 recommendations

## 🔮 Future Improvements

- **Collaborative Filtering**: Incorporate user ratings and preferences
- **Hybrid Approach**: Combine content-based and collaborative filtering
- **Advanced NLP**: Use word embeddings or BERT for better semantic understanding
- **Personalization**: Allow users to save preferences and get personalized recommendations
- **Movie Posters**: Display movie posters in the recommendations

## 📚 Dataset

This system uses the TMDB 5000 Movie Dataset, which includes:
- Movie metadata (genres, keywords, overview)
- Cast and crew information

## 📝 License

MIT License