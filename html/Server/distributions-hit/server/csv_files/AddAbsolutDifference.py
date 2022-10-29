import pandas as pd

if __name__ == '__main__':
    csv_input = pd.read_csv('./test_figures_temp.csv')
    Diff = []
    for i in range(0, len(csv_input)):
        Avg1 = csv_input.iloc[i].values.flatten().tolist()[11]
        Avg2 = csv_input.iloc[i].values.flatten().tolist()[12]
        Diff.append(round(abs(Avg2 - Avg1), 3))
    csv_input['AVG-DIFF'] = Diff
    csv_input.to_csv('./output.csv', index=False)