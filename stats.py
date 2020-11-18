"""
Writen by Eli James, 20177630
Last Edited on August 3rd
contains the averageRatings and mostPopular functions which determine the average ratings of the genres and the most popular genre in the dictioanry of subscribers and their ratings of each genre
"""
#creates the dictionary of subscribers and their genre ratings
import startercode
subscriber_ratings = startercode.startercode()

#this function takes the subscriber/genre dicitoanry as an argument and determines the average ratings of each genre
def averageRatings(subratings):
    #print(len(subratings))
    #dicitoanry which will store the average ratings for each genre. 
    averageRating = {'Jazz': 0,'Country':0,'Rap':0,'Blues':0,'Reggae':0,'Soul':0,'EDM':0,'Hip Hop':0,'World':0,'Rock':0,'Funk':0,'Dance':0,'Pop':0,'Metal':0,'Easy Listening':0,'Hits':0,'Opera':0,'Classical':0}
    
    #need to access each users ratings, add to running tally
    for user in subratings:
        userRatings = subratings[user]
        #print(userRatings)
        for genre in userRatings:
            averageRating[genre] += userRatings[genre]
    #print(averageRating)
    
    #divide each number in the average rationg sdictionary by the nuber of users, which is 38
    for item in averageRating:
        averageRating[item] /= 38
    #print(averageRating)
    
    #need to setup code that prints it all to a table. Prof Allison said this format was 'perfect', so I didn't bother using the tabulate module which would require TAs to pip3 install an external module
    print('Genre        Average Rating')
    for genreName, average in averageRating.items():
        print('{}   {}'.format(genreName, average))

#very simialr to the funciton above, but instead of returning all the genres' average ratings, finds the highest rated genre in the dictioanry and returns it.
def mostPopular(subratings):
    averageRating = {'Jazz': 0,'Country':0,'Rap':0,'Blues':0,'Reggae':0,'Soul':0,'EDM':0,'Hip Hop':0,'World':0,'Rock':0,'Funk':0,'Dance':0,'Pop':0,'Metal':0,'Easy Listening':0,'Hits':0,'Opera':0,'Classical':0}
    #need to access each users ratings, add to running tally
    for user in subratings:
        userRatings = subratings[user]
        #print(userRatings)
        for genre in userRatings:
            averageRating[genre] += userRatings[genre]
    #print(averageRating)
    #divide each number in the average rationg sdictionary by the nuber of users, which is
    for item in averageRating:
        averageRating[item] /= 38
    #print(averageRating)
    #finds max rating of all the genres.
    maxValue = max(averageRating.values())
    #determines which genre corresponds to the max rating
    popualarGenre = ''
    for maxGenre in averageRating:
        if averageRating[maxGenre] == maxValue:
            popualarGenre = maxGenre
    print(f"\n{popualarGenre} is the most popular genre, with an average rating of {maxValue}")


if __name__ == "__main__":
    #averageRatings(subscriber_ratings)
    mostPopular(subscriber_ratings)