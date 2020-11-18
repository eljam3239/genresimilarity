import startercode

subscriber_ratings = startercode.startercode()

def genreSimilarity(subratings, p1, p2):
    sub1ratings = subratings[p1]
    sub2ratings = subratings[p2]
    sub1_sum=0
    sub2_sum=0
    shared_genre = []
    intersectionSum = 0
    #used for testing
    print(p1, sub1ratings, p2, sub2ratings)
    #find the sum of ratings for person 1:
    for x in sub1ratings:
        sub1_sum+=sub1ratings[x]
    for y in sub2ratings:
        sub2_sum+=sub2ratings[y]
    #test
    print(sub1_sum, sub2_sum)
    #finds which genres the two both listen to
    for genre in sub1ratings:
        if genre in sub2ratings:
            shared_genre.append(genre)
    print(shared_genre)
    #finds the smaller rating for each genre the users share, sums all the smaller ratings called intersection sum
    for genre in shared_genre:
        p1GenreRating = sub1ratings[genre]
        p2GenreRating = sub2ratings[genre]
        intersectionSum += min(p1GenreRating, p2GenreRating)
    print(intersectionSum)
    #determines the similarity of the two users, given the calculation provided on the onq page
    similarity = min(intersectionSum/sub1_sum, intersectionSum/sub2_sum)
    print(f" The two users have a similarity of {similarity}.")
    return(similarity)

def findSimilarity(subratings, p1, p2):

    sub1ratings = subratings[p1]
    sub2ratings = subratings[p2]
    sub1_sum=0
    sub2_sum=0
    shared_genre = []
    intersectionSum = 0
    #used for testing
    #print(p1, sub1ratings, p2, sub2ratings)
    #find the sum of ratings for person 1:
    for x in sub1ratings:
        sub1_sum+=sub1ratings[x]
    for y in sub2ratings:
        sub2_sum+=sub2ratings[y]
    #test
    #print(sub1_sum, sub2_sum)
    #finds which genres the two both listen to
    for genre in sub1ratings:
        if genre in sub2ratings:
            shared_genre.append(genre)
    #print(shared_genre)
    #finds the smaller rating for each genre the users share, sums all the smaller ratings called intersection sum
    for genre in shared_genre:
        p1GenreRating = sub1ratings[genre]
        p2GenreRating = sub2ratings[genre]
        intersectionSum += min(p1GenreRating, p2GenreRating)
    #print(intersectionSum)
    #determines the similarity of the two users, given the calculation provided on the onq page
    similarity = min(intersectionSum/sub1_sum, intersectionSum/sub2_sum)
    #print(f" The two users have a similarity of {similarity}.")
    return(similarity)

def match_subscribers(subratings, custname):
    similarityWith = {}
    users = ['Justin Trudeau','Bob Jones','Sam Frizzel','Captain Nemo','Joe Jameson','Paul Casindes','Justin Bieber','Natlie Portman','Bugs Bunny','Peter Rabbit','Mickey Mouse','Martin Melchor','Nada Neel','Kristin Karlin','Edmond Earls','Fredrick Foxwell','Thomas Twitty','Julieann Jenning',
			'Anton Autin','Alix Ashmore','Tiffany Turgeon','Noella Nash','Esther Edgerton','Sanda Sewart','Fannie Ferrera','Bernardine Block','Roger Rudd','Yang Wu','Raisa Rohr','Cirocco Jones','Mickie Milling','Ronald McDonald','Tim Horton','Colonel Sanders','Joel Jerry','Leanora Lion','Oscar Oliverio','Jernau Fortier']
    users.remove(custname)
    #
    #print(users)
    #print(usersExcludingCustname)
    for name in users:
        similarityWith[name] = findSimilarity(subratings, custname, name)
    #print(similarityWith)
    maxSimilarity = max(similarityWith.values())
    personWithMaxSimilarity = []
    for person in similarityWith:
        if similarityWith[person] == maxSimilarity:
            personWithMaxSimilarity.append(person)
    
    #print(maxSimilarity)
    print(f"The following person(s) are most similar to {custname} in their musical taste: {personWithMaxSimilarity}, with a similarity of {maxSimilarity}.")

def findClosestSub(subratings, custname):

    similarityWith = {}
    users = ['Justin Trudeau','Bob Jones','Sam Frizzel','Captain Nemo','Joe Jameson','Paul Casindes','Justin Bieber','Natlie Portman','Bugs Bunny','Peter Rabbit','Mickey Mouse','Martin Melchor','Nada Neel','Kristin Karlin','Edmond Earls','Fredrick Foxwell','Thomas Twitty','Julieann Jenning',
			'Anton Autin','Alix Ashmore','Tiffany Turgeon','Noella Nash','Esther Edgerton','Sanda Sewart','Fannie Ferrera','Bernardine Block','Roger Rudd','Yang Wu','Raisa Rohr','Cirocco Jones','Mickie Milling','Ronald McDonald','Tim Horton','Colonel Sanders','Joel Jerry','Leanora Lion','Oscar Oliverio','Jernau Fortier']
    users.remove(custname)
    #
    #print(users)
    #print(usersExcludingCustname)
    for name in users:
        similarityWith[name] = findSimilarity(subratings, custname, name)
    #print(similarityWith)
    maxSimilarity = max(similarityWith.values())
    personWithMaxSimilarity = ''
    for person in similarityWith:
        if similarityWith[person] == maxSimilarity:
            personWithMaxSimilarity = person
    
    #print(maxSimilarity)
    #print(f"The following person(s) are most similar to {custname} in their musical taste: {personWithMaxSimilarity}, with a similarity of {maxSimilarity}.")
    return personWithMaxSimilarity, maxSimilarity

def recommendGenre(subratings, subName):
    personWithMaxSimilarity, maxSimilarity = findClosestSub(subratings, subName)
    print(personWithMaxSimilarity, maxSimilarity)
    
    sub1ratings = subratings[subName]
    sub2ratings = subratings[personWithMaxSimilarity]
    sub1genres = []
    sub2genres = []

    print(sub1ratings, sub2ratings)

    for genre1 in sub1ratings.keys():
        sub1genres.append(genre1)
    print(sub1genres)
    for genre2 in sub2ratings.keys():
        sub2genres.append(genre2)
    print(sub2genres)
    
    uniqueGenres = []
    for word in sub2genres:
        if word not in sub1genres:
            uniqueGenres.append(word)
    print(uniqueGenres)
    
    #https://stackoverflow.com/questions/28444561/get-only-unique-elements-from-two-lists-python/45098345
    ##print(uniqueGenres)

    uniqueGenreRatings = {}
    for genre in uniqueGenres:
        uniqueGenreRatings[genre] = sub2ratings[genre]
    print(uniqueGenreRatings)
   
    maxGenre = max(uniqueGenreRatings)
    allsub2Ratings = uniqueGenreRatings.values()
    maxRating = max(allsub2Ratings)

    #print(maxGenre, maxRating)

    print(f"We recommend that {subName} listens to {maxGenre}, with a recommendation score of {maxRating}, as it has the highest rating out of genres they havn't rated.")



if __name__ == "__main__":
    #genreSimilarity(subscriber_ratings, 'Justin Trudeau', 'Bob Jones')
    #match_subscribers(subscriber_ratings, 'Bob Jones')
    recommendGenre(subscriber_ratings, 'Justin Trudeau')