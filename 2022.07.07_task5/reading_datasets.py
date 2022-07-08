import pickle
import json
import csv

def load_data(filename):
    a_file = open(filename, "rb")
    output = pickle.load(a_file)
    a_file.close()
    return output

def read_task5(location, split = 'train'):
    filename = location + split + '.tsv'

    data = []
    with open(filename) as tsv_file:
        tsv_reader = csv.reader(tsv_file, delimiter='\t')
        for i, row in enumerate(tsv_reader):
            if i > 0:
                tweet_id = row[0]
                sentence = row[1].strip()
                label = row[2]
                data.append((sentence, label))

    return data


if __name__ == '__main__':
    location = '../2022.07.07_task5/'
    split = 'train'
    
    data = read_task5(location, split)
    print(len(data))

    data = read_task5(location, 'dev')
    print(len(data))
    
    data = read_task5(location, 'test')
    print(len(data))

    




