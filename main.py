from data_loader import load_data
from model import train_model
from prevention import prevent_attack

def main():
    data, labels = load_data("dataset.csv")

    model = train_model(data, labels)

    print("Running DDoS Prediction System...\n")

    for features in data:
        prediction = model(features)
        prevent_attack(prediction)

if __name__ == "__main__":
    main()
