# .6.	Class MovieApp
from project.user import User
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.movie_specification.movie import Movie


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        found_user = next(filter(lambda x: x.username == username, self.users_collection), None)
        if found_user:
            raise Exception("User already exists!")
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'
    # Creates an instance of the User class with the given username and age, and:
    # •	If the user (object) is not in the users_collection list,
    #   add him/her and return the message "{username} registered successfully."
    # •	If a user with the same username is already registered, raise an
    #   Exception with the message "User already exists!"

    def upload_movie(self, username: str, movie: Movie):
        pass
    # Only the owner of the given movie can upload it.
    # The method adds the movie to the user's movies_owned list as
    # well as the movies_collection list:
    # •	If the addition is successful, returns the message: "{username}
    # successfully added {movie_title} movie."
    # •	If the user with the username provided is not registered in the app,
    # raise an Exception with the message: "This user does not exist!"
    # •	If the user exists, but he/she is not the owner of the given movie,
    # raise an Exception with the message: "{username_given} is not the owner of the movie {movie_title}!"
    # •	If the movie object is already uploaded, raise an Exception with
    # the message: "Movie already added to the collection!"

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        pass
    # Only the owner of the movie given can edit it. You will
    # always be given usernames of registered users.
    # In this method, as kwargs you can receive one or more key-value pairs.
    # Each key will be a movie's attribute name ("title", "year", or "age_restriction"),
    # and the value will be the new value for that attribute. You will not
    # receive anything different from the keys mentioned above.
    # The method edits the movie attributes with the given values and returns
    # the message "{username} successfully edited {movie_title} movie."
    # •	If the movie is not uploaded, raise an Exception with the message
    #   "The movie {movie_title} is not uploaded!"
    # •	If the user does not own that movie, raise an Exception
    #   with the message "{username given} is not the owner of the movie {movie_title}!"

    def delete_movie(self, username: str, movie: Movie):
        pass
    # Only the owner of the movie given can delete it. You will
    # always be given usernames of registered users.
    # This method deletes the movie given in both movies_collection and
    # user's movies_owned lists. Then, it should return the message
    # "{username} successfully deleted {movie_title} movie."
    # •	If the movie is not uploaded, raise an Exception with the message
    #   "The movie {movie_title} is not uploaded!"
    # •	If the user does not own that movie, raise Exception with the
    #   message "{username given} is not the owner of the movie {movie_title}!"

    def like_movie(self, username: str, movie: Movie):
        pass
    # Owners cannot like their own movies. You will always
    # be given usernames of registered users and uploaded movies.
    # This method increases the value of the movie attribute
    # likes by 1 and adds the movie to the user's list movies_liked.
    # Then, it returns the message "{username} liked {movie_title} movie."
    # •	If the user is also the owner, raise an Exception with the
    #   message "{username} is the owner of the movie {movie_title}!"
    # •	If the user already liked that movie, raise an Exception
    #   with the message "{username} already liked the movie {movie_title}!"

    def dislike_movie(self, username: str, movie: Movie):
        pass
    # Only the user who has liked the movie can dislike it.
    # You will always be given usernames of registered users and uploaded movies.
    # This method decreases the value of the movie attribute likes
    # by 1 and removes that movie from the user's movies_liked list.
    # Then, it returns the message "{username} disliked {movie_title} movie."
    # •	If the user didn't like that movie in the first place,
    #   raise an Exception with the message "{username} has not liked the movie {movie_title}!"

    def display_movies(self):
        pass
    # This method sorts all movies uploaded by the year in
    # descending order. If there are two or more movies of the same year, sort them by title:
    # •	It should return the details() for each movie on separate lines in the format.
    # •	If there are no movies uploaded, it returns: "No movies found."

    def __str__(self):
        pass
    # This method should return a string on 2 lines for all users'
    # usernames and movies titles in the following format:
    # "All users: {all users' usernames separated by a comma and a space ", "}"
    # •	If no users: "All users: No users."
    # "All movies: {all movies' titles separated by a comma and a space ", "}"
    # •	If no movies: "All movies: No movies."
