import sys
import json


def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
#    hw()
#    lines(sent_file)
#    lines(tweet_file)
    afinnfile = open(sys.argv[1])

    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

#    print scores.items() # Print every (term, score) pair in the dictionary
    
    tweet_sentiment = []
    for tweets in tweet_file:
        tweet = json.loads(tweets)
        words = tweet["text"].split(" ")

        ## initialize the score to 0
        score = 0
        
        for word in words:
            word = word.lower()

            if scores.has_key(word):
                score += scores[word]

#   Append scores into list
        tweet_sentiment.append(score)
        print score


        
if __name__ == '__main__':
    main()
