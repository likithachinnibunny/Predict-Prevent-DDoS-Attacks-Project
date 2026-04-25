import csv

def load_data(file_path):
    data = []
    labels = []

    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            features = [int(row["traffic"]), int(row["requests"])]
            label = int(row["attack"])

            data.append(features)
            labels.append(label)

    return data, labels
