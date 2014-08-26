import sys
import json
from collections import defaultdict

punctuation = ".,:;!?"

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    undefine_term = defaultdict(list)
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        keyword, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[keyword] = int(score)  # Convert the score to an integer.
    
    for line in tweet_file:
        tweet_json = json.loads(line)
        
        if (tweet_json.has_key("text")):
            tweet = tweet_json["text"]
            tweet = tweet.lower()
            tweet = "".join(c for c in tweet if c not in ('\'','"','/','-','#','(',')',',','_','!','.',':','@','$','%','^','&','*','?'))
            terms = tweet.split(" ")
            
            ## initialize tweet score
            score = 0
            
            ## Analyze each term in tweets
            for term in terms:
                term = term.encode('utf-8')
                if scores.has_key(term):
                    score += scores[term]

            for term in terms:
                term = term.encode('utf-8')
                if not scores.has_key(term):
                    #if not (undefine_term.has_key(term)):
                    #    undefine_term[str(term)] = []
                    undefine_term[term].append(score)
                    
    for term in undefine_term:
        term_count = len(term)
        term_score = sum(undefine_term[term])
        term_avg = 0
        
        if term_count <> 0 and term_score <> 0:
            term_avg = float(term_score)/float(term_count)
        print term, term_avg


if __name__ == '__main__':
    main()
