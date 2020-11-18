"""
Module written by Eli James, 20177630
Last edited on august 3rd
Contains the genre similarity, match subscribers and recommend genre functions, and versions of the 1st two which act as helper functions to the recommendation function, just without all the outputing to console
"""
#creates the dictiopanry of subscriubers and their genre ratings
import startercode
subscriber_ratings = startercode.startercode()

#this function takes the subscriber rating dictionary and two subs in the dicitonary as inputs, and finds the similarity of the two subs using the fuzzy set theory shown on OnQ
def genreSimilarity(subratings, p1, p2):
    #variables needed to calculate things within fuzzy set theory
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
    #find the sum of ratings for p2
    for y in sub2ratings:
        sub2_sum+=sub2ratings[y]
    #test
    #print(sub1_sum, sub2_sum)
    #finds which genres the two both listen to
    for genre in sub1ratings:
        if genre in sub2ratings:
            shared_genre.append(genre)
    print(shared_genre)
    #finds the smaller rating for each genre the users share, sums all the smaller ratings called intersection sum. I found this useful: https://www.w3schools.com/python/ref_func_min.asp
    for genre in shared_genre:
        p1GenreRating = sub1ratings[genre]
        p2GenreRating = sub2ratings[genre]
        intersectionSum += min(p1GenreRating, p2GenreRating)
    print(intersectionSum)
    #determines the similarity of the two users, given the calculation provided on the onq page
    similarity = min(intersectionSum/sub1_sum, intersectionSum/sub2_sum)
    print(f" The two users have a similarity of {similarity}.")
    return(similarity)

#this function does exactly the same thing as the one above, I used it before I commented out the print statements in the above function as a more consise way of testing my program
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

#this function accepts the dictioanry of subs and their ratings and a sub in the dictioanry as arguments then prints out which other sub(s) is/are closest to the sub given
def match_subscribers(subratings, custname):
    similarityWith = {}#creates a dictionary that has the other subs as keys and will have their simialrities as values
    users = ['Justin Trudeau','Bob Jones','Sam Frizzel','Captain Nemo','Joe Jameson','Paul Casindes','Justin Bieber','Natlie Portman','Bugs Bunny','Peter Rabbit','Mickey Mouse','Martin Melchor','Nada Neel','Kristin Karlin','Edmond Earls','Fredrick Foxwell','Thomas Twitty','Julieann Jenning',
			'Anton Autin','Alix Ashmore','Tiffany Turgeon','Noella Nash','Esther Edgerton','Sanda Sewart','Fannie Ferrera','Bernardine Block','Roger Rudd','Yang Wu','Raisa Rohr','Cirocco Jones','Mickie Milling','Ronald McDonald','Tim Horton','Colonel Sanders','Joel Jerry','Leanora Lion','Oscar Oliverio','Jernau Fortier']
    users.remove(custname)#remove the sub being compared to, otherwise it would just return themselves every time
    #
    #print(users)
    #print(usersExcludingCustname)
    #for each sub, adds the vlaue of the similarity with each user to the similarityWith dictionary
    for name in users:
        similarityWith[name] = findSimilarity(subratings, custname, name)
    #print(similarityWith)
    maxSimilarity = max(similarityWith.values())#finds the max simialrity score (not person)
    personWithMaxSimilarity = [] #will store the name(s) of the subs with the max similarity score
    for person in similarityWith: #iterates through the simialrityWith dicitoanry, and stores the names of the subs with the max similarity to custname
        if similarityWith[person] == maxSimilarity:
            personWithMaxSimilarity.append(person)
    
    #print(maxSimilarity)
    print(f"\nThe following person(s) are most similar to {custname} in their musical taste: {personWithMaxSimilarity}, with a similarity of {maxSimilarity}.")

#once again, this funciton is exactly the same as match_subscribers, except I hadn't commented out the test print statements in math_subscribers so I could use findClosestSub to more cleearly and easily test my code
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

#same as immediately above, except the subs are only the ones used in the subset from the sublist used for unit testing
def findClosestSubUnitTest(subratings, custname):

    similarityWith = {}
    users = ['Justin Trudeau','Bob Jones','Sam Frizzel','Captain Nemo']
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

#this function takes the dictioanry of subs and their ratings and a subscriber as arguments, and determines which genre that sub should listen to provided the algorithm on OnQ
def recommendGenre(subratings, subName):
    personWithMaxSimilarity, maxSimilarity = findClosestSub(subratings, subName)#finds the people and similarity score of the sub closest to subName
    #print(personWithMaxSimilarity, maxSimilarity)
    
    sub1ratings = subratings[subName]
    sub2ratings = subratings[personWithMaxSimilarity]
    sub1genres = []
    sub2genres = []

    #print(sub1ratings, sub2ratings)
    #creates a list of the genres sub1 listens to
    for genre1 in sub1ratings.keys():
        sub1genres.append(genre1)
    #print(sub1genres)
    #creates a list of the genres sub2 listens to
    for genre2 in sub2ratings.keys():
        sub2genres.append(genre2)
    #print(sub2genres)
    
    #figures out which genres sub2 listens to that custName doesn't
    uniqueGenres = []
    for word in sub2genres:
        if word not in sub1genres:
            uniqueGenres.append(word)
    #print(uniqueGenres)
    
    #creates a dictioanry with the genres custName doesn't listen to as keys and sub2's ratings of those genres
    uniqueGenreRatings = {}
    for genre in uniqueGenres:
        uniqueGenreRatings[genre] = sub2ratings[genre]
    #print(uniqueGenreRatings)
    #of the unique genres, determines the one sub2 rated highest, which will be the genre that custName should try out!
    maxGenres = []
    allsub2Ratings = uniqueGenreRatings.values()
    maxRating = max(allsub2Ratings)
    #finds which genres corrrespond to the max rating, tried using max() but it ran but gave the wrong genre
    for word in uniqueGenreRatings:
        if uniqueGenreRatings[word] == maxRating:
            maxGenres.append(word)

    #print(maxGenre, maxRating)

    print(f"\nWe recommend that {subName} listens to {maxGenres}, with a recommendation score of {maxRating}, as it has the highest rating out of genres they havn't rated.")

#same as immediately above, except calls a modified match subscriber method that only contains the subs in the subset used for unit testing
def recommendGenreUnitTest(subratings, subName):
    personWithMaxSimilarity, maxSimilarity = findClosestSubUnitTest(subratings, subName)#finds the people and similarity score of the sub closest to subName
    #print(personWithMaxSimilarity, maxSimilarity)
    
    sub1ratings = subratings[subName]
    sub2ratings = subratings[personWithMaxSimilarity]
    sub1genres = []
    sub2genres = []

    #print(sub1ratings, sub2ratings)
    #creates a list of the genres sub1 listens to
    for genre1 in sub1ratings.keys():
        sub1genres.append(genre1)
    #print(sub1genres)
    #creates a list of the genres sub2 listens to
    for genre2 in sub2ratings.keys():
        sub2genres.append(genre2)
    #print(sub2genres)
    
    #figures out which genres sub2 listens to that custName doesn't
    uniqueGenres = []
    for word in sub2genres:
        if word not in sub1genres:
            uniqueGenres.append(word)
    #print(uniqueGenres)
    
    #creates a dictioanry with the genres custName doesn't listen to as keys and sub2's ratings of those genres
    uniqueGenreRatings = {}
    for genre in uniqueGenres:
        uniqueGenreRatings[genre] = sub2ratings[genre]
    #print(uniqueGenreRatings)
    #of the unique genres, determines the one sub2 rated highest, which will be the genre that custName should try out!
    maxGenres = []
    allsub2Ratings = uniqueGenreRatings.values()
    maxRating = max(allsub2Ratings)
    #finds which genres correspond to the max rating, tried using max() but it ran but gave the wrong genre
    for word in uniqueGenreRatings:
        if uniqueGenreRatings[word] == maxRating:
            maxGenres.append(word)

    #print(maxGenres, maxRating)

    return(maxGenres)

if __name__ == "__main__":
    #genreSimilarity(subscriber_ratings, 'Justin Trudeau', 'Bob Jones')
    #match_subscribers(subscriber_ratings, 'Bob Jones')
    #recommendGenre(subscriber_ratings, 'Justin Trudeau')
    recommendGenreUnitTest({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}, 'Justin Trudeau')