import csv
import os
from pprint import pprint as pp
import statistics


"""

This is column headers from input folder files.

Slide.ID
Cell.ID
Cell.X.Position
Cell.Y.Position
Annotation.ID
Tissue.Category
Distance.from.Tissue.Category.Edge..microns.
Phenotype.CD4
Phenotype.CD8
Phenotype.CD138
Phenotype.FOXP3
Phenotype.GZMB
CD4..within.100
CD8..within.100
CD138..within.100
FOXP3..within.100
GZMB..within.100
CD4..FOXP3..within.100
CD8..FOXP3..within.100
CD4..GZMB..within.100
CD8..GZMB..within.100
Total.Cells.within.100
"""


def parseit():
    summary_out = open('./change_this_to_your_data_output_filename.csv', 'w', newline='')
    summary_writer = csv.writer(summary_out, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    calc_dict = {}

    my_data_input_folder_name = 'data_P2_1000'
    data_src = os.path.join('./' + my_data_input_folder_name)
    for filename in os.listdir(data_src):
        print('   ' + filename)
        with open(os.path.join(data_src, filename), 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    column_index = row
                    line_count += 1
                else:
                    slide_id = row[column_index.index('Slide.ID')]
                    if slide_id not in calc_dict:
                        calc_dict[slide_id] = []
                    else:
                        if '+' in row[column_index.index('Phenotype.CD138')]:
                            calc_dict[slide_id].append(int(row[column_index.index('CD138..within.1000')]))
    print('creating CSV')
    summary_writer.writerow(['Slide ID', 'MIN', 'MAX', 'MEAN', 'STDEV'])
    for sl_id in calc_dict:
        dat = calc_dict[sl_id]
        summary_writer.writerow([sl_id, min(dat), max(dat), statistics.mean(dat), statistics.stdev(dat)])


if __name__ == '__main__':
    parseit()

