import json
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle


def load_data(users_path, test_path):
    """
    Loads the data from test figures file and from users file.
    Merges them together and returns a dataframe.
    """
    with open(users_path, 'rb') as f:
        users = json.load(f)

    user_list = []
    test_id_list = []
    choice_list = []
    for user in users:
        oid = user['_id']['$oid']
        for i in range(10):
            choice_data = user[f'choicePicked{i+1}']
            if 'test' in choice_data:

                test_id = choice_data.split('-')[1]
                choice = choice_data.split('-')[2]

                user_list.append(oid)
                test_id_list.append(test_id)
                choice_list.append(choice)

    users_df = pd.DataFrame({'oid': user_list, 'test_id': test_id_list, 'choice': choice_list})

    tests_df = pd.read_csv(test_path, header=None)
    tests_df.columns=['L1', 'L2', 'L3', 'L4', 'L5', 'R1', 'R2', 'R3', 'R4', 'R5', 'test_id', 'Lavg', 'Ravg']
    # Change the value to pure numerical without the word test.
    tests_df['test_id'] = tests_df['test_id'].apply(lambda x: x.replace('test', ''))

    # Rearranging the merged dataframe before the training step.
    res_df = users_df.merge(tests_df, how='left', left_on='test_id', right_on='test_id')

    res_df[['L1', 'L2', 'L3', 'L4', 'L5']] = res_df[['L1', 'L2', 'L3', 'L4', 'L5']]/100
    res_df[['R1', 'R2', 'R3', 'R4', 'R5']] = res_df[['R1', 'R2', 'R3', 'R4', 'R5']]/100

    return res_df


def train(users_path, test_path):
    data_df = load_data(users_path, test_path)

    X = data_df[['L1', 'L2', 'L3', 'L4', 'L5', 'R1', 'R2', 'R3', 'R4', 'R5']]
    y = data_df[['choice']]

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2)

    from sklearn.tree import DecisionTreeClassifier

    clf = DecisionTreeClassifier(max_depth=6)

    clf.fit(X_train, y_train)
    acc_score = clf.score(X_test, y_test)
    print(f'Model accuracy: {acc_score}')

    pickle.dump(clf, open('model.pkl', 'wb'))


if __name__ == '__main__':
    users_path = 'projDocs/users.json'
    test_path = 'projDocs/test_figures.csv'
    train(users_path, test_path)
