import pandas as pd

def AvgCalc(rowArr):
    final = 0
    for i in range(len(rowArr)):
        final += (i+1) * rowArr[i]
    return final / 100


if __name__ == '__main__':
    csv_input = pd.read_csv('./test_figures_temp.csv')
    avgStart = []
    avgEnd = []
    for i in range(0, len(csv_input)):
        print(csv_input.iloc[i].values.flatten().tolist())
        rowAvgStart = AvgCalc(csv_input.iloc[i].values.flatten().tolist()[0:5])
        rowAvgEnd = AvgCalc(csv_input.iloc[i].values.flatten().tolist()[5:10])
        avgStart.append(rowAvgStart)
        avgEnd.append(rowAvgEnd)
    csv_input['AVG-START'] = avgStart
    csv_input['AVG-END'] = avgEnd
    csv_input.to_csv('./output.csv', index=False)