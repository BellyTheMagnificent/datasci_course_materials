import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
#    print scores.items() # Print every (term, score) pair in the dictionary
    
    tags = {}
    for line in tweet_file:
        tweet = json.loads(line)
        if tweet.has_key("entities"):
            entities = tweet["entities"]
            #print entities
            if entities.has_key("hashtags"):
                for hashtag in entities["hashtags"]:
                    tag = hashtag["text"]
                    tag = tag.encode('utf-8')
                    if tag not in tags:
                        tags[tag] = 1
                    else:
                        tags[tag] += 1
    sort_tags =  sorted(tags, key=tags.get, reverse=True)
    for i in range(1,11):
        print sort_tags[i], tags[sort_tags[i]]
        
if __name__ == '__main__':
    main()
