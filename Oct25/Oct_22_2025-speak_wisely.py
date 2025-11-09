"""
Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."
"""
def wise_speak(sentence):
    wise_words = ["have", "must", "are", "will", "can"]
    for word in wise_words:
        if word in sentence:
            word_index = sentence.find(word)
            end_sentence = sentence[:word_index + len(word)].lower()
            first_sentence = sentence[word_index + len(word):-1].strip()
            
            # first_sentence_splitted = first_sentence.split(" ")
            # Capitalize_word = first_sentence_splitted[0].capitalize()

            first_sentence = first_sentence[0].upper() + first_sentence[1:]



    return f"{first_sentence}, {end_sentence}{sentence[-1]}"

print(wise_speak("You must speak wisely."))


"""
1. wise_speak("You must speak wisely.") should return "Speak wisely, you must."
2. wise_speak("You can do it!") should return "Do it, you can!"
3. wise_speak("Do you think you will complete this?") should return "Complete this, do you think you will?"
4. wise_speak("All your base are belong to us.") should return "Belong to us, all your base are."
5. wise_speak("You have much to learn.") should return "Much to learn, you have."
"""


def wise_speak(sentence):
    wise_words = ["have", "must", "are", "will", "can"]
    words_list = sentence[0:-1].split(" ")
    punctuation = sentence[-1]
    word_idx = -1
    for idx, word in enumerate(words_list):
        if word.lower() in wise_words:
            word_idx = idx

    if word_idx != -1:
            
            
   
        first_word = words_list[word_idx + 1].capitalize()

        
        first_sentence = first_word + ' ' +" ".join(words_list[word_idx + 2:])

        end_sentence = " ".join(words_list[:word_idx + 1]).lower()
                
        return f"{first_sentence}, {end_sentence}{punctuation}"
    return sentence
#print(wise_speak("You must speak wisely."))

print(wise_speak("You canee do it now!"))
