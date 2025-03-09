import os
import pickle
import sys

def check_pickle_file(file_path):
    """Check if a pickle file exists and can be loaded."""
    print(f"Checking {file_path}...")
    
    if not os.path.exists(file_path):
        print(f"❌ ERROR: File {file_path} does not exist!")
        return False
    
    try:
        with open(file_path, 'rb') as f:
            data = pickle.load(f)
        print(f"✅ SUCCESS: File {file_path} exists and can be loaded.")
        return True
    except Exception as e:
        print(f"❌ ERROR: File {file_path} exists but could not be loaded: {str(e)}")
        return False

def main():
    """Check if the required pickle files exist and can be loaded."""
    print("Movie Recommendation System - File Check Utility")
    print("=" * 50)
    
    # Check if the pickle files exist
    movies_file = "movies.pkl"
    similarity_file = "similarity.pkl"
    
    movies_ok = check_pickle_file(movies_file)
    similarity_ok = check_pickle_file(similarity_file)
    
    print("\nSummary:")
    print("=" * 50)
    if movies_ok and similarity_ok:
        print("✅ All required files exist and can be loaded.")
        print("You can run the app with: streamlit run app.py")
    else:
        print("❌ Some required files are missing or cannot be loaded.")
        print("Please run the Jupyter notebook to generate these files.")

if __name__ == "__main__":
    main() 