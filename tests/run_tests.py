import pandas as pd
import math
import argparse
from dasrs.detectors.dasrs_rest import DasrsRest

PROBATIONARY_PERCENT = 0.15

def getProbationPeriod(probationPercent, fileLength):
    return min(
        math.floor(probationPercent * fileLength),
        probationPercent * 5000
    )

def main(args):
    print('running tests')

    input_file = args.input_file
    output_file = args.output_file
    timestamp_column = args.timestamp_column
    value_column = args.value_column
    output_columns = [timestamp_column, value_column, 'anomalyScore']

    input_data = pd.read_csv(input_file)

    min_value = input_data[value_column].min()
    max_value = input_data[value_column].max()
    probationary_period = getProbationPeriod(
        PROBATIONARY_PERCENT,
        input_data.shape[0])

    detector = DasrsRest(
        minValue=min_value,
        maxValue=max_value,
        restPeriod=probationary_period / 5.0)

    output_rows = []
    for i, row in input_data.iterrows():
        #pdb.set_trace()
        input_timestamp = row[timestamp_column]
        input_value = row[value_column]
        anomaly_score = detector.getAnomalyScore(input_value)
        output_row = (input_timestamp, input_value, anomaly_score)
        output_rows.append(output_row)

    output_data = pd.DataFrame(output_rows, columns=output_columns)
    output_data.to_csv(output_file, index=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_file",
                    help="Input file path",
                    default='tests/test_data/test_data_01.csv')

    parser.add_argument("--output_file",
                    help="Output file path",
                    default='tests/test_data/output_test_data_01.csv')

    parser.add_argument("--timestamp_column",
                    help="Timestamp column name",
                    default='timestamp')

    parser.add_argument("--value_column",
                    help="Value column name",
                    default='value')

    args = parser.parse_args()

    main(args)