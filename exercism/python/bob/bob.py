def hey(phrase):
    
    if phrase.isspace() or phrase == "":
        return 'Fine. Be that way!'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    elif phrase.strip()[-1]=='?': #เป็นการตัดข้อความออกให้เหลือแค่ตัวสุดท้าย ? หรือป่าว
        
        return 'Sure.'
    else:
        return 'Whatever.' 


