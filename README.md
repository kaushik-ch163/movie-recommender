# 🎬 Movie Recommendation System

A content-based movie recommendation system that suggests similar movies based on various features like genres, keywords, and overview.

## 🌟 Features

- **Content-based filtering** using movie metadata
- **Similarity scores** to show how closely related recommendations areare
- **User-friendly interface** built with Streamlit

## 🚀 System Features

1. **TF-IDF Vectorization**: Uses TF-IDF to give more weight to important terms and less to common termstion**: Uses TF-IDF to give more weight to important terms and less to common terms
2. **Enhanced Recommendation Function**: Returns movie titles with similarity scores2. **Enhanced Recommendation Function**: Returns movie titles with similarity scores
3. **Simple UI**: Clean visualization of recommendations with similarity scores

## 🛠️ Installation & Setup

### Prerequisites
1. **Python**: Make sure Python 3.8 or higher is installed1. **Python**: Make sure Python 3.8 or higher is installed
2. **Git**: Install Git for version controlll Git for version control
3. **Dataset**: Download the TMDB 5000 Dataset files:
   - `tmdb_5000_movies.csv`
   - `tmdb_5000_credits.csv`

### Step-by-Step Installationn

1. **Clone the Repository**
```bash```bash
git clone https://github.com/kaushik-ch163/movie-recommender.gitm/kaushik-ch163/movie-recommender.git
cd movie-recommendere-recommender
```

2. **Create & Activate Virtual Environment****Create & Activate Virtual Environment**
```bash```bash
# Windows
python -m venv venv-m venv venv
venv\Scripts\activatepts\activate

# Linux/MacOS
python3 -m venv venvpython3 -m venv venv
source venv/bin/activatein/activate
```

3. **Install Dependencies****Install Dependencies**
```bash```bash
pip install -r requirements.txt.txt
```

4. **Setup Dataset****Setup Dataset**
- Place the downloaded dataset files in the project root directory:- Place the downloaded dataset files in the project root directory:
  - `tmdb_5000_movies.csv`s.csv`
  - `tmdb_5000_credits.csv`
- Run the Jupyter notebook to generate required files: to generate required files:
```bash
jupyter notebook Project.ipynb
```
- Execute all cells to generate:e:
  - `movies.pkl` `movies.pkl`
  - `similarity.pkl`

5. **Run the Application**tion**
```bash```bash
streamlit run app.py
```
The application will open in your default web browser at `http://localhost:8501` open in your default web browser at `http://localhost:8501`

### Troubleshooting
- If you see "Movie not found" errors, ensure the dataset files are properly processed- If you see "Movie not found" errors, ensure the dataset files are properly processed
- For "Module not found" errors, verify all dependencies are installedound" errors, verify all dependencies are installed
- Check if pickle files are generated in the project directory

## 📊 How It Works

1. **Data Preprocessing**:ssing**:
   - Merges movie data with credits data   - Merges movie data with credits data
   - Extracts features from genres, keywords, and overviewm genres, keywords, and overview
   - Processes text using stemming
   - Creates weighted feature vectors

2. **Recommendation Process**:
   - Converts input movie title to a feature vector   - Converts input movie title to a feature vector
   - Calculates similarity with all other moviesh all other movies
   - Ranks movies by similarity score
   - Returns top 5 recommendations

## 🔮 Future Improvements

- **Cast and Crew Analysis**: Incorporate actor and director information for better recommendations- **Cast and Crew Analysis**: Incorporate actor and director information for better recommendations
- **Movie Posters**: Display movie posters in the recommendationslay movie posters in the recommendations
- **Personalization**: Allow users to save preferences and get personalized recommendations- **Personalization**: Allow users to save preferences and get personalized recommendations

## 📚 Dataset

This system uses the TMDB 5000 Movie Dataset, which includes:
- Movie metadata (genres, keywords, overview)
- Cast and crew information- Cast and crew information

## 📝 License## 📝 License

MIT License