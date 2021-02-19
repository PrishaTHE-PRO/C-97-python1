abc=input('enter your introduction') 
charactersCount=0
wordCount=1
for i in abc :
    charactersCount=charactersCount+1
    if (i==' '):
        wordCount=wordCount+1
print('number of characters in a string : =>')
print(charactersCount)
print('number of words in a string : =>')
print(wordCount)
