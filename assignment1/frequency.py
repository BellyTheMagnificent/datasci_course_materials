import sys
import json
import re


def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
#    lines(tweet_file)
    
    terms = {}
    total_terms = 0
    
    for tweet in tweet_file:
        json_tweet = json.loads(tweet)
        words = json_tweet["text"]
        words = words.lower()
        words = re.findall(r'\w+', words,flags = re.UNICODE | re.LOCALE) 

        for word in words:
            word = word.lower()
            word = word.encode('utf-8')
            
            if not word in terms:
                terms[word] = 1
            else:
                terms[word] +=1
            total_terms += 1

    for term in terms:
        print term, float(terms[term]) /float(total_terms)

if __name__ == '__main__':
    main()
