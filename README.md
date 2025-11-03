# Movie Recommendation System

<p>
I have created a content-based based movie recommendation system, which is inspired from many open-source projects. 
</p>

<h2>
Problem Statement
</h2>
<p>
    Recommend movies based on similar content. Similar content means similarity in cast, crew, movie title, genres, and other aspects.
</p>

<h2>
Dataset
</h2>

<p>
TMDB 5000 Movie Dataset
</p>
<p>
Source: <a href="https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata">TMDB Kaggle</a>
</p>

<h2>
Flow of implementation
</h2>
<ol>
<li>
    Studied about the dataset from the source.
</li>
<li>
    Analyzed attributes and their influence factor.
</li>
<li>
    Created a new feature from the attributes with influencing factor.
</li>
<li>
    Extracted numerical embeddings of the textual feature created.
</li>
<li>
    Calculated a similarity matrix using cosine similarity.
</li>
<li>
    For a given movie, extract the 6 nearest (similar) movies using the similarity score obtained.
</li>
<li>
    Return (represent) the similar movies found.
</li>
</ol>

<br>
<p>
    Still step 6 of the above implementation plan, my raw work can be found in Movie_Recommendation.ipynb file.
</p>

<h2>
    1. About the Dataset
</h2>
<p>
    The dataset is having two portions: tmdb_5000_movies.csv and tmdb_5000_credits.csv
</p>
<p>
    Following are the attributes present in the csv files:
</p>
<table>
    <tr>
        <th>
            tmdb_5000_movies
        </th>
        <th>
            tmdb_5000_credits
        </th>
    </tr>
    <tr>
        <td>
            budget: numeric value
        </td>
        <td>
            movie_id: numeric value
        </td>
    </tr>
    <tr>
        <td>
            genre: stringed_json
        </td>
        <td>
            title: string
        </td>
    </tr>
    <tr>
        <td>
            homepage: stringed_url
        </td>
        <td>
            cast: stringed_json
        </td>
    </tr>
    <tr>
        <td>
            id: numeric value
        </td>
        <td>
            crew: stringed_json
        </td>
    </tr>
    <tr>
        <td>
            original_title: string
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            popularity: numeric value
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            production_companies: stringed_json
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            production_countries: stringed_json
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            release_date: date
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            revenue: numeric value
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            runtime: numeric value (in minutes)
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            spoken_language: stringed_json
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            status: string
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            tagline: string
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            title: string
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            vote_average: numeric value
        </td>
        <td>
        </td>
    </tr>
    <tr>
        <td>
            vote_count: numeric value
        </td>
        <td>
        </td>
    </tr>
</table>

<p>
    As the information in the tmdb_5000_credits.csv like 'cast' and 'crew' is required for further analysis, I merged both the dataframes into one. 
</p>
<p>
    <b>CODE:</b>
</p>
<code>
    MOVIE_CSV = r"Dataset/tmdb_5000_movies.csv"
    CREDITS_CSV = r"Dataset/tmdb_5000_credits.csv"
</code>
<code>
    movies = pd.read_csv(MOVIE_CSV)
    credits = pd.read_csv(CREDITS_CSV)
</code>
<p>
    I am merging both the dataframes based on 'title' as title is unique for all possible movies in this case.
</p>
<code>
    merged_movies = movies.merge(credits, on='title')
</code>

<h2>
    2. Analysis of attributes
</h2>
<p>
    Attributes considered for recommendation system build-up are in <b>bold</b> font.
</p>
<p>
    i) budget: As it depicts the price of making a movie, usually a high budget film may attract good ratings. Being a numeric value, I will not use in my recommendation system.
</p>
<p>
    ii) <b>genres</b>: Depicts type of the movie. Used for recommendation as it helps to find the similar movie.
</p>
<p>
    iii) homepage: Not required as it not helps in finding similar movie. A URL is always unique.
</p>
<p>
    iv) movie_id: I have not used this but it is required for fetching the movie related information. This movie_id is provided by the TMDB.
</p>
<p>
    v) <b>keywords</b>: Useful for finding the similarity between the movies, as these words are often remembered by the users.
</p>
<p>
    vi) original_language: May affect if also look for region of the user. In this case, we are only considering the content of the movie, hence not taken into the account.
</p>
<p>
    vii) original_title: There may be multiple language, and here I am handling the cases for only one language, i.e. English. Hence, skipping this at the moment.
</p>
<p>
    viii) <b>overview</b>: This contains the summary of the movie. This information is necessary to consider as it kind of characterizes the movie.
</p>
<p>
    ix) 
</p>

<p>
    Below is the visualization of count of languages present in the dataset:
</p>
<img src="Language_Count.jpg">
