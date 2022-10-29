import pandas as pd
import csv

if __name__ == '__main__':
    csv_input = pd.read_csv('../csv_files/test_figures_temp.csv')
    Diff = []
    for i in range(0, len(csv_input)):
        Avg1 = csv_input.iloc[i].values.flatten().tolist()[11]
        Avg2 = csv_input.iloc[i].values.flatten().tolist()[12]
        # If the left distribution Avg is higher then the label is 1.
        if Avg1 > Avg2:
            Diff.append([0])
        # If the right distribution Avg is higher then the label is 0.
        else:
            Diff.append([1])
    with open('Labels.csv', 'w') as f:

        # using csv.writer method from CSV package
        write = csv.writer(f)
        write.writerows(Diff)