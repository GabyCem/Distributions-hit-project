import pandas as pd
import csv

def getLabel(choice):
    choice_arr = choice.split('-')
    return choice_arr[1], choice_arr[2]

def createUsersDict(length):
    choiceDict = {}
    for i in range(0, length):
        choiceDict[i] = {}
    return choiceDict

def addMissingVal(mainDict, CSVlength):
    for user_id,choices_id in mainDict.items():
        for i in range(1,CSVlength + 1):
            if str(i) not in choices_id:
                mainDict[user_id][str(i)] = None

    return mainDict

if __name__ == '__main__':
    csv_input = pd.read_csv('../csv_files/users.csv')
    choiceDict = createUsersDict(len(csv_input))
    for j in range(1, 11):
        if j == 5 or j == 10:
            continue
        choice_str = "choicePicked" + str(j)
        cur_choices_picked = csv_input[choice_str]
        for i in range(0, len(csv_input)):
            id , choice = getLabel(cur_choices_picked[i])
            if choice == "R":
                choiceDict[i][id] = 1
            else:
                choiceDict[i][id] = 0
    userLabels = addMissingVal(choiceDict,54)
    df = pd.DataFrame(userLabels)
    df.sort_index()
    df.to_csv("userLabels.csv")