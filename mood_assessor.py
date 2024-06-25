import datetime
import os



def assess_mood():

    types_of_moods = {'happy' : 2, 'relaxed' : 1, 'apathetic' : 0, 'sad' : -1, 'angry' : -2}

    diary_file = 'data/mood_diary.txt'

    os.makedirs('data', exist_ok=True)
    

    if os.path.exists(diary_file):
        with open (diary_file, 'r', encoding="utf-8") as f:
            entries = f.readlines()
    else:
        entries = {}

    
    date_today = str(datetime.date.today())
    for entry in entries:
        date , _ =entry.strip().split(" ")
        if date == date_today:
            print("Sorry, you have already entered your mood today.")
            return 

    while True:
        mood = input("What's your mood today (happy, relaxed, apathetic, sad, and angry) ").lower().strip()
        if mood in types_of_moods:
            break
        else:
            print("Invalid answer! Please enter a new answer from the list (types of moods)")

    
    #store the input
    with open(diary_file, 'a', encoding='utf-8') as f:
        f.write(f"{date_today} {types_of_moods[mood]}\n")

    if len(entries)>=6:
        recent_entries = entries[-6:] + [f"{date_today} {types_of_moods[mood]}\n"]
        mood_scores = [int(entry.strip().split(" ")[1])for entry in recent_entries] 

        happy_days = sum(1 for score in mood_scores if score == 2)
        sad_days = sum(1 for score in mood_scores if score == -1)
        apathetic_days = sum(1 for score in mood_scores if score == 0)

        if happy_days >= 5:
            diagnosis = "manic"
        elif sad_days >= 4:
            diagnosis = "depressive"
        elif apathetic_days >= 6:
            diagnosis = "schizoid"
        else:
            round_score = round(sum(mood_scores) / 7)

            diagnosis = {2:"happy", 1:"relaxed", 0:"apathetic", -1:"sad", -2:"angry"}[round_score]


        print(f"Your diagnosis: {diagnosis}!")



    

    



    



