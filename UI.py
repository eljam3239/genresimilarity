"""
Module written by Eli James, 20177630
Last edited on August 3rd
Runs the user interface for the program, calls the methods in the simAndDiff, stats and startercode modules, runs the unit testing
"""

import simAndDif
import stats
import startercode

#creates the dictioanry of subscribers and their genre ratings
subscribers = ['Justin Trudeau','Bob Jones','Sam Frizzel','Captain Nemo','Joe Jameson','Paul Casindes','Justin Bieber','Natlie Portman','Bugs Bunny','Peter Rabbit','Mickey Mouse','Martin Melchor','Nada Neel','Kristin Karlin','Edmond Earls','Fredrick Foxwell','Thomas Twitty','Julieann Jenning','Anton Autin','Alix Ashmore','Tiffany Turgeon','Noella Nash','Esther Edgerton','Sanda Sewart','Fannie Ferrera','Bernardine Block','Roger Rudd','Yang Wu','Raisa Rohr','Cirocco Jones','Mickie Milling','Ronald McDonald','Tim Horton','Colonel Sanders','Joel Jerry','Leanora Lion','Oscar Oliverio','Jernau Fortier']
subscriber_ratings = startercode.startercode()

#runs the UI and calls the other modules
def main():
    #error handling for if the user tries to use a subscriber that isn't in the subscribers list *which are the keys of the subscriber_ratings dictionary
    while True:
        try:
            user = input("Please input the name of a user: ")
        except ValueError:
            print("Woops! That wasn't a valid user, try again: ")
            continue
        if user not in subscribers:
            print("Not a valid subscriber, try again: ")
        else:
            break
    #recommends a genre for the subscriber inputed by the user
    simAndDif.recommendGenre(subscriber_ratings, user)
    print("\nHere are the average ratings for each genre: \n")
    #shows the user the average ratings and most popular genre in the subscriber_ratings dictionary
    stats.averageRatings(subscriber_ratings)
    stats.mostPopular(subscriber_ratings)
    #error handling to make sure the sub for which the user is trying to find a matched sub is actually a valid subscriber in the subscriber_ratings dictioanry
    while True:
        try:
            subscriber = input("\nPlease input the name of a subscriber for us to match someone with: ")
        except ValueError:
            print("Woops, that isn't a valid subscriber, try again: ")
            continue
        if subscriber not in subscribers:
            print("Not a valid subscriber, try again: ")
        else:
            break
    #shows the user the match subscriber
    simAndDif.match_subscribers(subscriber_ratings, subscriber)

main()

#for unit testing
if __name__ == "__main__":
    #the practice sub ratings dictioanry is: {'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}
    #Justin Trudeau will be the practice subscriber
    
    print("\n-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("UNIT TESTING\n")

    #find the genre simialrity between Justin Trudeau and Bob Jones
    print("\nShould be 0.2: ", simAndDif.genreSimilarity({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}, 'Justin Trudeau', 'Bob Jones'))
    #find the genre simialrity between Justin Trudeau and Sam Frizzle
    print("\nShould be 0.3125: ", simAndDif.genreSimilarity({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}, 'Justin Trudeau', 'Sam Frizzel'))
    #find the genre siomialrity betweej JT and Captain Nemo
    print("\nShould be 0.2: ", simAndDif.genreSimilarity({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}, 'Justin Trudeau', 'Captain Nemo'))

    #find the closest sub to justin trudeau (same method as match_subscribers)
    print("\nShould be Sam Frizzel: ", simAndDif.findClosestSubUnitTest({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}},'Justin Trudeau'))

    #find the genre JT should listen to
    print("\nShould be 'Dance': ", simAndDif.recommendGenreUnitTest({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}, 'Justin Trudeau'))
    
    #find the average ratings, if all values are 1, average should be 1
    print("\n Should be 0 when we switch all ratings to 0: ", stats.averageRatings({'Justin Trudeau': {'Country': 0, 'Hip Hop': 0, 'Opera': 0, 'Hits': 0, 'Metal': 0, 'Classical': 0, 'World': 0, 'Rock': 0, 'Soul': 0, 'Rap': 0}, 'Bob Jones': {'Rock': 0, 'Pop': 0, 'Classical': 0, 'Hip Hop': 0, 'Opera': 0, 'Soul': 0, 'EDM': 0, 'Easy Listening': 0}, 'Sam Frizzel': {'Rap': 0, 'Hits': 0, 'Soul': 0, 'Dance': 0, 'Funk': 0, 'Rock': 0, 'Jazz': 0, 'Classical': 0}, 'Captain Nemo': {'Blues': 0, 'Rock': 0, 'Soul': 0, 'Metal': 0, 'Funk': 0, 'EDM': 0, 'Dance': 0, 'Jazz': 0}}))
    print("Look above for average ratings table, ignore return type none ^^^")

    #find the most popular genre
    print("Should be rock: ", stats.mostPopular({'Justin Trudeau': {'Country': 4, 'Hip Hop': 6, 'Opera': 1, 'Hits': 3, 'Metal': 5, 'Classical': 8, 'World': 9, 'Rock': 3, 'Soul': 1, 'Rap': 5}, 'Bob Jones': {'Rock': 5, 'Pop': 4, 'Classical': 3, 'Hip Hop': 1, 'Opera': 3, 'Soul': 4, 'EDM': 8, 'Easy Listening': 10}, 'Sam Frizzel': {'Rap': 10, 'Hits': 5, 'Soul': 4, 'Dance': 9, 'Funk': 2, 'Rock': 9, 'Jazz': 6, 'Classical': 3}, 'Captain Nemo': {'Blues': 7, 'Rock': 6, 'Soul': 3, 'Metal': 8, 'Funk': 5, 'EDM': 5, 'Dance': 2, 'Jazz': 7}}))
    print("Look above for most popualr, ignore return type none ^^^")

    