# importing necessary libraries
import streamlit as st
import pickle
import pandas as pd
import requests

# importing necessary pickle files
movie_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))
new_movies1 = pickle.load(open('new_movies1.pkl', 'rb'))
movie_links = pickle.load(open('movie_links.pkl', 'rb'))
user_rating = pickle.load(open('user_given_ratings.pkl', 'rb'))
user_rating1 = pd.Series(user_rating).to_frame()
correlation_matrix = pickle.load(open('correlation_matrix.pkl', 'rb'))
user_rating_pivot = pickle.load(open('user_rating_pivot1.pkl', 'rb'))
st.set_page_config(layout="wide")


# Method To add background image on home page
def set_bg_hack_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url("https://www.itl.cat/pngfile/big/46-465731_streaming-movies.jpg");
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


activities = ["Home", "Trending", "Search", "Genre-wise"]  # Options on the sidebar
with st.sidebar:  # creating a sidebar
    with st.form(key='my_form'):
        try:
            user_id = st.sidebar.text_input('User ID')  # For getting the userId from user
            user_id = int(user_id)
        except ValueError:
            print(" ")
    choice = st.sidebar.selectbox("Select Activity", activities)  # For selecting the options on the sidebar

d = {}  # declaring dictionaries and list to be used in further functions
L = []
d2 = {}


def fetch_poster(movie_id):  # Method for fetching Posters from TMDb API
    global s1
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US'.format(
            movie_id))
    data = response1.json()
    if data['poster_path'] is not None:
        s1 = "https://image.tmdb.org/t/p/w500" + data['poster_path']
    return s1


def fetch_overview(movie_id):  # Method for fetching overview of the Movie
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US'.format(
            movie_id))
    data1 = response1.json()
    return data1['overview']  # Method will return movie Overview


def fetch_vote_average(movie_id):  # Method for fetching average vote of a movie
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US'.format(
            movie_id))
    data3 = response1.json()
    return data3['vote_average']


def fetch_runtime(movie_id):  # For fetching the runtime of a movie
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US'.format(
            movie_id))
    data4 = response1.json()
    return data4['runtime']


def fetch_popular_title():  # Getting the title of the popular Movies
    response1 = requests.get(
        'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
    data = response1.json()
    d[0] = data['results'][0]['title']
    d[1] = data['results'][1]['title']
    d[2] = data['results'][2]['title']
    d[3] = data['results'][3]['title']
    d[4] = data['results'][4]['title']
    d[5] = data['results'][5]['title']

    return ""


if choice == "Home":  # Default Home Page

    st.markdown("""
    <style>
    .big-font {
        font-size:200px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 style="font-size:70px; text-align:left;">PickNflix</h1>',
                unsafe_allow_html=True)  # To set the Header on the page
    set_bg_hack_url()  # Calling the set_bg_hack_url Method to add background image

elif choice == "Trending":  # If user selected Trending option
    try:
        st.write(fetch_popular_title())  # Calling the method to fetch the posters of popular movies
        st.header("Trending")

        col1, col2, col3 = st.columns(3)  # For arranging the movie titles and posters in columns
        with col1:
            st.markdown(d.get(0))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][0]['poster_path'])
            st.markdown(" ")
        with col2:
            st.markdown(d.get(1))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][1]['poster_path'])
            st.markdown(" ")
        with col3:
            st.markdown(d.get(2))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][2]['poster_path'])
            st.markdown(" ")
        with col1:
            st.markdown(d.get(3))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][3]['poster_path'])

        with col2:
            st.markdown(d.get(4))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][4]['poster_path'])

        with col3:
            st.markdown(d.get(5))
            response1 = requests.get(
                'https://api.themoviedb.org/3/movie/popular?api_key=2d0f610bf9a084dfe8419d91cd008fe8&language=en-US&page=1')
            data = response1.json()
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][5]['poster_path'])
    except IndexError:
        print(" ")
    except TypeError:
        print(" ")

elif choice == "Search":  # To search Movies
    try:
        def Search_similar(movie):  # Method to get similar movies
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:7]
            recommended_movies = []  # List to add movie title
            recommended_posters = []  # List to add movie posters
            movie_overview = []  # List to add movie overview
            vote_average = []  # List to add movie ratings
            runtime = []  # List to add movie runtime

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id
                # Appending Movie details to respective lists
                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_posters.append(fetch_poster(movie_id))
                movie_overview.append(fetch_overview(movie_id))
                vote_average.append(fetch_vote_average(movie_id))
                runtime.append(fetch_runtime(movie_id))

            return recommended_movies, recommended_posters, movie_overview, vote_average, runtime


        your_movie = st.selectbox(' ', movies['title'].values)  # Select box for selecting Movies

        if st.button('Search'):  # Search Button
            names, posters, overview, vote_average, runtime = Search_similar(
                your_movie)  # Storing return value of function in variables
            col6, col7 = st.columns(2)
            col8, col9 = st.columns(2)
            with col6:
                st.subheader(names[0])
                st.image(posters[0])
            with col7:
                st.subheader("Overview:")
                st.markdown(overview[0])

                st.subheader("Ratings:")
                st.subheader(vote_average[0])

                st.markdown("duration(in mins):")
                st.markdown(runtime[0])

            st.subheader("Similar Movies you may like:")
            col1, col2, col3, col4, col5 = st.columns(5)  # Displaying Similar movies in columns
            with col1:
                st.caption(names[1])
                st.image(posters[1])
                st.caption(overview[1])
            with col2:
                st.caption(names[2])
                st.image(posters[2])
                st.caption(overview[2])

            with col3:
                st.caption(names[3])
                st.image(posters[3])
                st.caption(overview[3])

            with col4:
                st.caption(names[4])
                st.image(posters[4])
                st.caption(overview[4])

            with col5:
                st.caption(names[5])
                st.image(posters[5])
                st.caption(overview[5])
    except IndexError:
        print()

elif choice == "Genre-wise":  # To get the genre-wise movie suggestions
    col1, col2, col3, col4, col5 = st.columns(5)


    def get_genre(genre_id):  # Method to get genre-wise movie details
        response1 = requests.get(
            'https://api.themoviedb.org/3/discover/movie?api_key=2d0f610bf9a084dfe8419d91cd008fe8&with_genres={}'.format(
                genre_id))
        data = response1.json()
        with col6:
            d2[0] = data['results'][0]['title']
            st.markdown(d2.get(0))
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][0]['poster_path'])
        with col7:
            d2[1] = data['results'][1]['title']
            st.markdown(d2.get(1))
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][1]['poster_path'])
        with col8:
            d2[2] = data['results'][2]['title']
            st.markdown(d2.get(2))
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][2]['poster_path'])
        with col6:
            d2[3] = data['results'][3]['title']
            st.markdown(d2.get(3))
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][3]['poster_path'])
        with col7:
            d2[4] = data['results'][4]['title']
            st.markdown(d2.get(4))
            st.image("https://image.tmdb.org/t/p/w500" + data['results'][4]['poster_path'])

        return d2


    col6, col7, col8 = st.columns(3)
    with col1:
        if st.button('Animation'):
            get_genre(16)  # Calling the method for genre-id of different genres
    with col2:
        if st.button('Action'):
            get_genre(28)
    with col3:
        if st.button('Adventure'):
            get_genre(12)
    with col4:
        if st.button('Comedy'):
            get_genre(35)
    with col5:
        if st.button('Crime'):
            get_genre(18)
    with col1:
        if st.button('Drama'):
            get_genre(10751)
    with col2:
        if st.button('Family'):
            get_genre(14)
    with col3:
        if st.button('Fantasy'):
            get_genre(12)
    with col4:
        if st.button('Horror'):
            get_genre(27)
    with col5:
        if st.button('History'):
            get_genre(36)
if choice == "Home":
    print(" ")
else:
    try:

        def recommend(userId):  # Recommend Function which will return the list of recommended movies
            user_rating1 = user_rating_pivot.loc[userId].dropna()
            similar_items = pd.Series()
            for i in range(0, len(user_rating1.index)):
                # Finding similar movies to the already rated movies.
                sims = correlation_matrix[user_rating1.index[i]].dropna()
                # Based on how the user rated the movie scale the similarity values.
                sims = sims.map(lambda x: x * user_rating1[i])
                similar_items = similar_items.append(sims)
            similar_items.sort_values(inplace=True, ascending=False)  # sorting the similarity values
            similar_items.head(10)
            watched_list = []
            for i in similar_items.index:
                if i in user_rating1.index:
                    watched_list.append(i)
            filtered_similar_items = similar_items.drop(watched_list) # dropping the items from the watched list
            d = filtered_similar_items.to_dict()
            for keys in d:
                L.append(keys)  #Appending the keys of dictionary in list
            return L    # returning the list of recommended movies


        if int(user_id) <= 668 and int(user_id) != 0:   # Checking if the user is in dataset or not
            title = recommend(int(user_id)) #Calling the method for userId entered by user
        else:
            st.caption("You are not an Authorised user you can select your favourite genre or search your favourite "
                       "movie:")

        if int(user_id) <= 668 and int(user_id) != 0:
            st.subheader("Recommended For You:")

        col1, col2, col3 = st.columns(3) # Arranging the recommended movies
        with col1:
            st.caption(L[0])
            str = L[0]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col2:
            st.caption(L[1])
            str = L[1]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col3:
            st.caption(L[2])
            str = L[2]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))
        with col1:
            st.caption(L[3])
            str = L[3]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col2:
            st.caption(L[4])
            str = L[4]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col3:
            st.caption(L[5])
            str = L[5]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col1:
            st.caption(L[6])
            str = L[6]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col2:
            st.caption(L[7])
            str = L[7]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col3:
            st.caption(L[8])
            str = L[8]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

        with col1:
            st.caption(L[9])
            str = L[9]
            movie_id1 = movie_links.loc[movie_links['title'] == str]
            temp = float(movie_id1.get(key="tmdbId"))
            st.image(fetch_poster(temp))

    except ValueError:
        print(" ")
    except IndexError:
        print(" ")
