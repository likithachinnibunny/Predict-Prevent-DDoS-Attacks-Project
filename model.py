def train_model(data, labels):
    """
    Simple rule-based model (simulating ML behavior)
    """
    def predict(features):
        traffic, requests = features
        if traffic > 300 or requests > 80:
            return 1
        return 0

    return predict
