# Movie-Recommender-Engage
## PickNflix (Movie Recommender System using content-based and collaborative filtering)


Different Methods/filtering Algorithm for Recommendation Systems:

### Content-based filtering:
  Content-based filtering uses item features to recommend other items similar to what the user likes, based on their previous actions or explicit feedback.
### Collaborative filtering :
  Collaborative filtering is a family of algorithms where there are multiple ways to find similar users or items and multiple ways to calculate rating based on ratings of similar users.
  #### Item based Collaborative filtering:
  Item-item collaborative filtering is a type of recommendation system that is based on the similarity between items calculated using the rating users have given to items. 
  #### User based Collaborative filtering:
  User-Based Collaborative Filtering is a technique used to predict the items that a user might like on the basis of ratings given to that item by the other users who have similar taste with that of the target user
### Hybrid filtering :
This is a combination of Content-based and Collaborative filtering.

My objective was to implement a model that would recommend the relevant content(movies) to the user (content similarity) according to the movie they have searched, so I have Implemented a content based Recommendation system.
But then I observed that The model can only make recommendations based on existing interests of the user.So,to overcome this problem I have used collaborative Filtering Method.In collaborative filtering there is no need to understand item(Movie) content and we can use user ratings to predict the probable ratings for other Movies.
### Datasets Used:
Link to the dataset:
tmdb_5000_movies
tmdb_5000_credits
https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/discussion?select=tmdb_5000_movies.csv
movies
ratings
https://www.kaggle.com/datasets/ayushimishra2809/movielens-dataset?select=movies.csv
links_small
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset

### Project Flow :
Dataset Analysis
Data Pre-processing
Model Building (for content based recommendations using text vectorization and cosine similarity)
Model Building (for collaborative filtering method)
Model Testing
Front-end designing using streamlit

# Requirements:
##### numpy
##### pandas 
##### ast
##### sklearn
##### nltk
##### scipy
##### pickle
##### streamlit
##### requests
### step 1:
Open final_content_based.ipynb jupyter notebook file and run the code(datasets should be uploaded on the same folder or add the file path)
### step 2:
After completing the execution of the program, there will be 7 files downloaded to the main folder : movie_dict.pkl, similarity.pkl,correlation_matrix.pkl,movie_links.pkl,new_movies1.pkl,user_given_ratings.pkl and user_rating_pivot1.pkl
These files will be used during the execution of App.py file.
### step 3:
After entering the source code folder, run the following command on command prompt, to locally host the webpage
streamlit run app.py

### Home Page(User can add his userId here)
![Screenshot (186)](https://user-images.githubusercontent.com/106458512/170855469-4c30dd15-3bac-4dc0-bff7-21c84a31fd08.png)
### User can select Trending option and can get the list of trending movies
![Screenshot (187)](https://user-images.githubusercontent.com/106458512/170856620-3173a16c-0ba5-4b09-9c83-324b85de8064.png)
### User can search and select a movie in select bar and will get recommendations 
![Screenshot (188)](https://user-images.githubusercontent.com/106458512/170856632-ef00ff00-9f9c-44f8-8338-da9a2f1a197d.png)
### Searched movie details will be displayed
![Screenshot (189)](https://user-images.githubusercontent.com/106458512/170856646-4bdc6c3e-2d88-434d-bde2-0d3d6a74106a.png)
###  Similar movies related to the searched movie and their overviews
![Screenshot (190)](https://user-images.githubusercontent.com/106458512/170856652-3b3faaf2-34e8-4470-8978-0590bb8d3ba1.png)
### User can select his favourite genres and can get the list of movies from that genre.
![Screenshot (191)](https://user-images.githubusercontent.com/106458512/170856661-0194affa-3848-427e-9edb-21f37e4b95ec.png)




