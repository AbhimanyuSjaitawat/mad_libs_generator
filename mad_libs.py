# A list of replacement words to be passed in to the play game function. 
parts_of_speech1  = ["__1__","__2__","__3__","__4__","__5__"]

#A list of answer words 
answer_words_list1 = ["language","van","author","indentation"]
answer_words_list2 = ["language","pages","applications","pages","structure"]
answer_words_list3 = ["information","Apple","microcomputer","co-founder"]

#All strins with their answer are :
#string1 : "Python is a widely used high-level, general-purpose, interpreted, dynamic programming __1__. Guido __2__ Rossum was the __3__ of Python. Python uses whitespace __4__ to delimit blocks - rather than curly braces or keywords"
#string2 : "HyperText Markup Language (HTML) is the standard markup language for creating web pages and web applications. HTML elements are the building blocks of HTML pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document."
#string3 : "Steven Paul "Steve" Jobs was an American information technology entrepreneur and inventor. He was the co-founder, chairman, and chief executive officer (CEO) of Apple Inc. Jobs is widely recognized as a pioneer of the microcomputer revolution of the 1970s and 1980s, along with Apple co-founder Steve Wozniak."

# The following are some test strings to pass in to the play_game function.
test_string1 = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming __1__. Guido __2__ Rossum was the __3__ of Python. Python uses whitespace __4__ to delimit blocks - rather than curly braces or keywords"
test_string2 = "HyperText Markup Language (HTML) is the standard markup __1__ for creating web __2__ and web __3__. HTML elements are the building blocks of HTML __4__. HTML describes the __5__ of a web page semantically and originally included cues for the appearance of the document."
test_string3 = "Steven Paul (Steve) Jobs was an American __1__ technology entrepreneur and inventor. He was the co-founder, chairman, and chief executive officer (CEO) of __2__ Inc. Jobs is widely recognized as a pioneer of the __3__ revolution of the 1970s and 1980s, along with Apple __4__ Steve Wozniak."

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None
        
# Plays a full game of mad_libs. A player is prompted to replace words in ml_string, 
# which appear in parts_of_speech with their own words.  
def play_game(ml_string, parts_of_speech, answer_words_list):    
    replaced = []
    min_allowed_tries=0
    str = ml_string;
    ml_string = ml_string.split()
    index=0
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            print str
            user_input = raw_input(replacement + "Should substitute by : ")
            allowed_attempts=5
            while (user_input!=answer_words_list[index]):
                allowed_attempts=allowed_attempts-1
                if(allowed_attempts==min_allowed_tries): return None
                print "Wrong answer !!! try left : " ,allowed_attempts
                print str
                user_input = raw_input(replacement + "Should substitute by : ")
            str = str.replace(replacement,user_input)
            index=index+1;
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else:
            replaced.append(word)   
    replaced = " ".join(replaced)
    return replaced

#function to play game according to difficulty level 
def difficulty_selection(difficulty_passed):
    if (difficulty_passed== "easy"):
        print "You will get 5 guesses per problem"
        print "The current paragraph reads as such:"
        print play_game(test_string1, parts_of_speech1, answer_words_list1)       
    if (difficulty_passed == "medium"):    
        print "You will get 5 guesses per problem"
        print "The current paragraph reads as such:"
        print play_game(test_string2, parts_of_speech1, answer_words_list2)
    if (difficulty_passed == "hard"):    
        print "You will get 5 guesses per problem"
        print "The current paragraph reads as such:"
        print play_game(test_string3, parts_of_speech1, answer_words_list3)
    return None    

#For selecting difficulty 
print "Please select game difficulty !!!"
diff_user = raw_input("Choices are : easy,medium and hard : ")
difficulty_selection(diff_user)

