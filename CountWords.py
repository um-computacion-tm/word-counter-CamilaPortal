
def count_words(word:str):
    
    listw=word.split()
    result={}
    
    for word in range(len(listw)):
        listw[word]=listw[word].lower()
        
    for word in listw:
        if word in result:
            result[word]+=1
        else:
            result[word]=1
            
    return result

