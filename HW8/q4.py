import requests


def ID_info():
    movie_id = input("Enter your movie's IMDB ID:\n>>>> ") 
    url = f"http://www.omdbapi.com/?i={movie_id}&apikey=3300ae5"
    response = requests.get(url)
    result = response.json()
    return result

def transform(data):
    
    #provides the info about title, ratings, genre, director, language, country, plot,list of actors
    x = [f"Title: {data["Title"]} {data["Year"]}",
        f"MT: {data["Ratings"][2]['Value']} - RT: {data["Ratings"][1]['Value']} "
        f" Genre: {data["Genre"]}", f'Director: {data["Director"]}',
        f'Language: {data["Language"]}', f"Country: {data["Country"]}",
        f'Actors: {data['Actors']}', f"Plot summary: {data["Plot"]}" ]
    
    
print(transform(ID_info()))
