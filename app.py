import streamlit as st
import pickle
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from Modules.similarity_score import similarity_scores

# Creating a Robust session
# I need to create this in order to avoid the following error:

# SSLError: HTTPSConnectionPool(host='api.themoviedb.org', port=443): Max retries exceeded with url: 
# (Caused by SSLError(SSLEOFError(8, '[SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol 
# (_ssl.c:1006)')))

session = requests.Session()

retry_strategy = Retry(
    total=5,              # retry up to 5 times
    backoff_factor=0.5,   # wait 0.5, 1, 2, 4, ... seconds between retries
    status_forcelist=[429, 500, 502, 503, 504],  # retry for these HTTP errors
    allowed_methods=["GET"]  # only retry GET requests
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

API_KEY = "92a1402246e8d98607ccf329c3f5283d"
BASE_URL = "https://api.themoviedb.org/3/movie/"
IMG_BASE_URL = "https://image.tmdb.org/t/p/w500"
SIMILARITY_SCORE_MATRIX_PATH = "./Output/similarity_scores.pkl"
MOVIES_PROCESSED_PATH = "./Output/movies_processed.pkl"

# --- Function to safely fetch poster URL ---
def fetch_poster(movie_id):
    url = f"{BASE_URL}{movie_id}?api_key={API_KEY}&language=en-US"
    try:
        response = session.get(url, timeout=10)  # timeout to avoid hanging
        response.raise_for_status()  # raises HTTPError for bad codes

        data = response.json()
        poster_path = data.get("poster_path")

        if not poster_path:
            print(f"Poster for movie_id={movie_id} DO NOT EXIST")
            return None

        return IMG_BASE_URL + poster_path

    except requests.exceptions.SSLError as e:
        print(f"SSL Error for movie_id={movie_id}: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed for movie_id={movie_id}: {e}")
        return None


# --- Function to get posters for a list of movie indexes ---
def get_movie_posters(movies_indexes, dataframe):
    movie_posters = []
    for i in movies_indexes:
        movie_id = dataframe['movie_id'].iloc[i]
        poster = fetch_poster(movie_id)
        movie_posters.append(poster)
    return movie_posters

## Function to return the movie names based on the indexes received
def get_Movie_Names(movie_indexes, dataframe):

    movie_names = []

    for i in movie_indexes:

        movie_names.append(dataframe['title'][i])

    return movie_names


## Function that will create the recommendation of the movies
## It will return the movie indexes

def recommend_movie(movie_name, dataframe, similarity_scores):
    movie_index = dataframe[dataframe['title'] == movie_name].index[0]

    distances = similarity_scores[movie_index]

    # print(distances)

    ### Now, we will sort the scores in descending order such that we retain the index values of the movies

    ## We will use enumerate function

    movie_number_list = list(enumerate(distances))

    sorted_movies = sorted(movie_number_list, key=lambda x: x[1], reverse=True)[1:7]  # Returning 1st 10 similar movies

    return [x[0] for x in sorted_movies]

    # movies_name = []
    #
    # movie_posters = []
    #
    # for i in sorted_movies:
    #     # print(i[0], dataframe['title'][i[0]])
    #     movies_name.append(dataframe['title'][i[0]])
    #
    #     # Fetching the poster of the movie
    #
    #     movie_posters.append(fetch_poster(dataframe['movie_id'][i[0]]))
    #
    # return movies_name, movie_posters




similarity_scores = pickle.load(open(SIMILARITY_SCORE_MATRIX_PATH, 'rb'))
movies_list = pickle.load(open(MOVIES_PROCESSED_PATH, "rb"))
# similarity_scores = similarity_scores(movies_list)

movies_name = movies_list['title'].values

# movies_name.remove('The Dark Knight Rises')



st.title('Content-based')
st.title('Movie Recommendation System')

st.write("This will recommend you 6 similar movies to watch . . .")

# Creating a select box in the streamlit

option = st.selectbox(
    "Enter a movie: ",
    movies_name,
)

if st.button('Recommend'):

    # movie_indices = recommend_movie(option, movies_list, similarity_scores)
    # # print(movie_indices)
    # movies_names = get_Movie_Names(movie_indices, movies_list)
    #
    # for movie in enumerate(movies_names):
    #     st.write(f'{movie[0] + 1}.) ', movie[1])
    #
    # movie_posters = get_movie_posters(movie_indices, movies_list)
    #
    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.text(f"1.) {movies_names[0]}")
    #     st.image(movie_posters[0])
    # with col2:
    #     st.text(f"2.) {movies_names[1]}")
    #     st.image(movie_posters[1])
    #
    # with col3:
    #     st.text(f"3.) {movies_names[2]}")
    #     st.image(movie_posters[2])
    #
    # col4, col5, col6 = st.columns(3)
    #
    # with col4:
    #     st.text(f"4.) {movies_names[3]}")
    #     st.image(movie_posters[3])
    # with col5:
    #     st.text(f"5.) {movies_names[4]}")
    #     st.image(movie_posters[4])
    # with col6:
    #     st.text(f"6.) {movies_names[5]}")
    #     st.image(movie_posters[5])


    try:
        movie_indices = recommend_movie(option, movies_list, similarity_scores)
        # print(movie_indices)
        movies_names = get_Movie_Names(movie_indices, movies_list)

        for movie in enumerate(movies_names):
            st.write(f'{movie[0]+1}.) ', movie[1])

        try:

            st.write("Loading posters . . .")

            movie_posters = get_movie_posters(movie_indices, movies_list)

            col1, col2, col3 = st.columns(3)
            with col1:
                st.text(f"1.) {movies_names[0]}")
                st.image(movie_posters[0])
            with col2:
                st.text(f"2.) {movies_names[1]}")
                st.image(movie_posters[1])

            with col3:
                st.text(f"3.) {movies_names[2]}")
                st.image(movie_posters[2])

            col4, col5, col6 = st.columns(3)

            with col4:
                st.text(f"4.) {movies_names[3]}")
                st.image(movie_posters[3])
            with col5:
                st.text(f"5.) {movies_names[4]}")
                st.image(movie_posters[4])
            with col6:
                st.text(f"6.) {movies_names[5]}")
                st.image(movie_posters[5])

        except:
            st.write("Oops some error occurred while loading the movie posters . . . ")


    except:
        st.write("Oops, recommender got confused... I guess there's no other movie like ", option, "!!")