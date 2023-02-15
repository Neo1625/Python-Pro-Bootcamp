#student_dict = {
#    "student": ["Angela", "James", "Lily"],
#    "score": [56, 76, 98]
#}

#Looping through dictionaries:
#for (key, value) in student_dict.items():
#    #Access key and value
#    pass


#student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
#for (index, row) in student_data_frame.iterrows():
#    #Access index and row
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
import pandas


nato = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_df = pandas.DataFrame(nato)
#print(nato_df)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}
print(nato_dict)


valid = True
while valid:
    try:
        word = input("Enter a word: ")
        phonetic_list = [nato_dict[l.upper()] for l in word]
        print(phonetic_list)
        valid = False
    except KeyError:
        print("Sorry only letters in the alphabets please")

