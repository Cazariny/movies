#Media Class

This is a python class made for store movie related information

##Requirements
**You need to install Python ( 2.7 Recomended) for the use of this proyect**

##Usage
For the use of this class you need to call it from the file you where you need
it (Just like all other classes of Python)

```
import media
```
You can store the information about 4 things

  - The movie title
  - The movie storyline
  - The logo of the movie
  - The url of the movie trailer in  youtube

and the syntax for use it is :

```
name_of_movie = media.Movie("Movie Title",
                            "Movie Storyline",
                            "URL of the movie logo",
                            URL of the youtube trailer)
```

###Development
If you want or need to store an other thing in the class you can enter to the code of the file and do it for yourself

The syntax for do it its This

```
def __init__(self, name_of_the_new_argument): #
       #Assign the value of the argument
         self.argument = name_of_the_new_argument
```

if you add a new argument to the class the syntax needs to be this

```
name_of_movie = media.Movie("Movie Title",
                            "Movie Storyline",
                            "URL of the movie logo",
                            "URL of the youtube trailer",
                            "New information you add")
```


###Run
For run the program the only thing you have to do is double click the _entertaiment_center.py_ file and it will run the Python program creating the web page.
If you modify the class file you have to run the _entertaiment_center_ again
