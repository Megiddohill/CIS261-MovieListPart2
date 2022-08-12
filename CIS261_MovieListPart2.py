# David Prato CIS261 LABWk6 Movie Guide P2


#File Write function____________________________________
fileName = "movies.txt"

def write_movies(movies): #This function will use movies as a parameter
    with open(fileName, "w") as file: #so here "WITH" cleans up after the file closes, OPEN opens, and AS makes an Alias
        for movie in movies:
            file.write(f'{movie}\n') #the guts of the function. This writes it into our file. 'W" before allows writing. "R" reading

# File Read Function___________________________________

def read_movies():
    movies = []
    with open(fileName) as file: #You don't need to type "r", it is the default "file" is representative of the "file object"
        for line in file:# this for loop will go thought every "line" in "fileName" aka movies.txt in this call
            line = line.replace("\n", "") #So in the file, titles are seperated by \, this replaces \ with nothing
            movies.append(line)#Then adds that line to the list
    return movies

# List Function -----------------------------------#

def list(movies):
    for i, movie in enumerate(movies,start = 1): # Remember that a enumerates count the iterations and gives each list item an assoicted number. "Start is where that number begins 
        print(f'{i}. {movie}\n')

# Add Function -------------------------------------#
def add(movies):

    movie = input("Movie title: ")
    movies.append(movie)
    write_movies(movies) #we use this function to write into our text file
    print(f'{movie} was added!\n')

# Delete Function ----------------------------------#
def delete(movies):
    index = int(input("Choose the movie number from your list you wish to delete: "))
    if index > 1 or index < len(movies): #Remember that the list will be indexed, it's not going to count words or the like)
        movie = movies.pop(index -1)#pop deletes, remember since indexes start with 0, you must -1 from your intended target
        write_movies(movies)
        print(f'{movie} was removed.\n')
    else:
        print("Invalid selection")

#Heading and List---------------------------------#

def display():
    print("Choose your Movie!\n")
    print("Menu Options\n")
    print("1: Movie List")
    print("2: Add a movie")
    print("3: Delete a movie")
    print("4: Exit")

# Main Program ----------------------------------------#

def main():
   
    command = 0
    movies = read_movies()
    
    display()

    while True: #"While True" is used to make a while loop operate until the given boolean condition becomes false
        try:
            command = int(input("Enter your choice number: \n"))
        except:
            print("Invalid input")
        if command == 1: 
            list(movies)
        elif command == 2:
            add(movies)
        elif command == 3:
            delete(movies)
        elif command == 4:
            break
        else:
            print("Invalid input, try again: \n")

    print("Thank you for using our service!")

if __name__ == "__main__": #This is used to call a "main()" function
    main()
