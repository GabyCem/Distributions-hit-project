import pandas as pd

if __name__ == '__main__':
    csv_input = pd.read_csv('./test_figures.csv')
    ids = []
    for i in range(1, len(csv_input) + 1):
        ids.append("TEST-" + str(i))
        print(12)
    csv_input['ID'] = ids
    csv_input.to_csv('./output.csv', index=False)