import pandas as pd
import os
import math
import argparse
from dasrs.detectors.dasrs_rest import DasrsRest
from dasrs.detectors.dasrs_likelihood import DasrsLikelihood

PROBATIONARY_PERCENT = 0.15

def getProbationPeriod(probationPercent, fileLength):
    return min(
        math.floor(probationPercent * fileLength),
        probationPercent * 5000
    )

def list_input_files(input_path):
    input_files = []
    for file in os.listdir(input_path):
        if file.endswith(".csv"):
            input_files.append(file)
    return input_files

def run_detector(input_path, output_path, file_name, timestamp_column,
                 value_column, detector_name):

    input_file = os.path.join(input_path, file_name)
    input_data = pd.read_csv(input_file)
    output_file = os.path.join(output_path, "{}-{}".format(
        detector_name, file_name))
    output_columns = [timestamp_column, value_column, 'anomalyScore']

    min_value = input_data[value_column].min()
    max_value = input_data[value_column].max()
    probationary_period = getProbationPeriod(
        PROBATIONARY_PERCENT,
        input_data.shape[0])

    if detector_name == 'DASRS_REST':
        detector = DasrsRest(
            minValue=min_value,
            maxValue=max_value,
            probationaryPeriod=probationary_period)
    elif detector_name == 'DASRS_LIKELIHOOD':
        detector = DasrsLikelihood(
            minValue=min_value,
            maxValue=max_value,
            probationaryPeriod=probationary_period)
    else:
        return

    output_rows = []
    for i, row in input_data.iterrows():
        input_timestamp = row[timestamp_column]
        input_value = row[value_column]
        anomaly_score = detector.getAnomalyScore(input_value, input_timestamp)
        output_row = (input_timestamp, input_value, anomaly_score)
        output_rows.append(output_row)

    output_data = pd.DataFrame(output_rows, columns=output_columns)
    output_data.to_csv(output_file, index=False)

def main(args):
    print('running detector')

    input_path = args.input_path
    output_path = args.output_path
    timestamp_column = args.timestamp_column
    value_column = args.value_column

    input_files = list_input_files(input_path)
    #print(input_files)
    for file_name in input_files:
        run_detector(input_path, output_path, file_name, timestamp_column,
            value_column, 'DASRS_REST')
        run_detector(input_path, output_path, file_name, timestamp_column,
            value_column, 'DASRS_LIKELIHOOD')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("--input_path",
                    help="Input data path",
                    default='scripts/input_test_data')

    parser.add_argument("--output_path",
                    help="Output data path",
                    default='scripts/output_test_data')

    parser.add_argument("--timestamp_column",
                    help="Timestamp column name",
                    default='timestamp')

    parser.add_argument("--value_column",
                    help="Value column name",
                    default='value')

    args = parser.parse_args()

    main(args)