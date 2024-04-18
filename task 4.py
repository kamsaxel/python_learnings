sentence = input("Enter a sentence: ")
if "python" in sentence.lower():
    print(sentence[::-1])
elif "java" in sentence.lower():
    print(sentence.upper())
else:
    print(sentence.lower()) 
