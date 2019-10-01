def main():
    print("This is a program that outputs statistics about a sentence")
    sentence = str(input("Please write a sentence: "))
    characters=len(sentence)
    print("The number of characters is: ", characters)
    words=len(sentence.split())
    print("The number of words is: ", words)
    c=0
    numwords=1
    for i in range (len(sentence)):
        if sentence[c]==" ":
            c=c+1

    A=len(sentence.replace(" ", ""))/words
    print("The average word length is: ",(A))
    
   
    

main()

