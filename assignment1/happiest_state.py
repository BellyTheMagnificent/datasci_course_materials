import sys
import json
import re



def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def main():
    sentimentFile = open(sys.argv[1])
    tweetFile = open(sys.argv[2])
    states = {
        'ak': 'alaska',
        'al': 'alabama',
        'ar': 'arkansas',
        'as': 'american samoa',
        'az': 'arizona',
        'ca': 'california',
        'co': 'colorado',
        'ct': 'connecticut',
        'dc': 'district of columbia',
        'de': 'delaware',
        'fl': 'florida',
        'ga': 'georgia',
        'gu': 'guam',
        'hi': 'hawaii',
        'ia': 'iowa',
        'id': 'idaho',
        'il': 'illinois',
        'in': 'indiana',
        'ks': 'kansas',
        'ky': 'kentucky',
        'la': 'louisiana',
        'ma': 'massachusetts',
        'md': 'maryland',
        'me': 'maine',
        'mi': 'michigan',
        'mn': 'minnesota',
        'mo': 'missouri',
        'mp': 'northern mariana islands',
        'ms': 'mississippi',
        'mt': 'montana',
        'na': 'national',
        'nc': 'north carolina',
        'nd': 'north dakota',
        'ne': 'nebraska',
        'nh': 'new hampshire',
        'nj': 'new jersey',
        'nm': 'new mexico',
        'nv': 'nevada',
        'ny': 'new york',
        'oh': 'ohio',
        'ok': 'oklahoma',
        'or': 'oregon',
        'pa': 'pennsylvania',
        'pr': 'puerto rico',
        'ri': 'rhode island',
        'sc': 'south carolina',
        'sd': 'south dakota',
        'tn': 'tennessee',
        'tx': 'texas',
        'ut': 'utah',
        'va': 'virginia',
        'vi': 'virgin islands',
        'vt': 'vermont',
        'wa': 'washington',
        'wi': 'wisconsin',
        'wv': 'west virginia',
        'wy': 'wyoming'
        }
    
    have_place = 0
    have_state = 0
    # Get the scores
    scores = {}
    for line in sentimentFile:
        term, score = line.split('\t')
        scores[term] = int(score)


    # Get the tweet with state information
    stateTweets = []
    for line in tweetFile:
        tweet = json.loads(line)
        if tweet.get('text') == None : continue


        # Get state
        state = None
        if tweet.get('place') != None:
            if tweet['place'].get('country_code') != 'US' and tweet['place'].get('country') != 'United States':
                continue

            placeFullName = tweet['place'].get('full_name')
           
            if placeFullName != None : 
                have_place += 1
                placeFullName = placeFullName.lower()
                placeFullName = placeFullName.encode("utf-8")
                
                locations = re.split(", ", placeFullName)
                ## Lookup up to the list
                for place in locations:
                    if states.has_key(place):
                        state = place
                       # print state + " from key"
                        stateTweets.append((state, tweet['text']))
                        have_state += 1
                        break
                    elif place in states.values():
                        state = states.keys()[states.values().index(place)]
                       # print state + " from value"
                        stateTweets.append((state, tweet['text'])) 
                        have_state += 1   
                        break
                
        elif tweet['user'].get('loaction') != None:
            state = tweet['user'].get('loaction')
  
    stateScores = {}
   
    for stateTweet in stateTweets:
        state = stateTweet[0]
        text = stateTweet[1]
       
        score = 0.0
        words = text.split()
        for word in words:
            score += scores.get(word, 0)

        if state in stateScores:
            stateScores[state] += score
        else:
            stateScores[state] = score
            
    happiestState = (None, 0)
    for state, score in stateScores.iteritems():
        if score > happiestState[1]:
            happiestState = state, score

    print str(happiestState[0]).upper()



if __name__ == '__main__':
    main()
