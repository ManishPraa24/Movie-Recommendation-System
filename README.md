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
