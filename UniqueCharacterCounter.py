#Input a long sentence from user and remove the space if possible, find and print the set of unique letters and count.
sentence = input("Enter a long sentence: ")
sentence = sentence.replace(" ", "")
unique_characters = set(sentence)                           #transforn into set type bcz set have only unque letters it eliminate duplicate fron it
print("Unique characters used:", unique_characters)
print("Total number of unique characters:", len(unique_characters))