def hey(phrase):
    
    if phrase.isspace() or phrase == "":
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.strip()[-1]=='?': 
        
        return 'Sure.'
    else:
        return 'Whatever.' 


