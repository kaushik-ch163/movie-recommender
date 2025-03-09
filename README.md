# 🎬 Movie Recommendation System

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

## 🛠️ Installation & Setup

### Prerequisites
1. **Python**: Make sure Python 3.8 or higher is installed
2. **Git**: Install Git for version control
3. **Dataset**: Download the TMDB 5000 Dataset files:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

### Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/kaushik-ch163/movie-recommender.git
cd movie-recommender
```

2. **Create & Activate Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/MacOS
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup Dataset**
- Place the downloaded dataset files in the project root directory:
  - `tmdb_5000_movies.csv`
  - `tmdb_5000_credits.csv`
- Run the Jupyter notebook to generate required files:
```bash
jupyter notebook Project.ipynb
```
- Execute all cells to generate:
  - `movies.pkl`
  - `similarity.pkl`

5. **Run the Application**
```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501`

### Troubleshooting
- If you see "Movie not found" errors, ensure the dataset files are properly processed
- For "Module not found" errors, verify all dependencies are installed
- Check if pickle files are generated in the project directory

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