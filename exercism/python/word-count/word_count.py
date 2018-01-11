from collections import Counter
import re

def word_count(phrase):
    my_str = phrase.lower()
    new_string = re.sub('[^a-zA-Z0-9 \n\']', ' ', my_str)
    cnt = Counter()
    print(new_string.split())
    for work in new_string.split():
        cnt[work]+=1
    print(cnt)
    
    return cnt

