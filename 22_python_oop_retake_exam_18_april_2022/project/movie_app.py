from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def found_user(self, username):
        return next(filter(lambda x: x.username == username, self.users_collection), None)

    def register_user(self, username, age):
        user = self.found_user(username)
        if user:
            raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username: str, movie: Movie):
        user = self.found_user(username)
        if not user:
            raise Exception('This user does not exist!')
        elif movie.owner.username != username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        elif movie in self.movies_collection:
            raise Exception('Movie already added to the collection!')
        else:
            user.movies_owned.append(movie)
            self.movies_collection.append(movie)
            return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif movie.owner.username != username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username: str, movie: Movie):
        user = self.found_user(username)
        if movie not in self.movies_collection:
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif movie not in user.movies_owned:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.remove(movie)
            user.movies_owned.remove(movie)
            return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.found_user(username)
        if movie.owner.username == username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif movie in user.movies_liked:
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes += 1
            user.movies_liked.append(movie)
            return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.found_user(username)
        if movie not in user.movies_liked:
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -= 1
            user.movies_liked.remove(movie)
            return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
            return "\n".join(x.details() for x in sorted_movies)

    def __str__(self):
        display_string = ""
        if self.users_collection:
            display_string += f'All users: {", ".join(x.username for x in self.users_collection)}\n'
        else:
            display_string += f'All users: No users.\n'
        if self.movies_collection:
            display_string += f'All movies: {", ".join(x.title for x in self.movies_collection)}'
        else:
            display_string += f'All movies: No movies.'
        return display_string

