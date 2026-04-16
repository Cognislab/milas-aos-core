# ISC: Inner Safety Calculation (簡易実装例)

class InnerSafetyCalc:
    def __init__(self, safety, stability, load):
        self.safety = safety
        self.stability = stability
        self.load = load

    def safety_score(self):
        return sum(self.safety.values()) / len(self.safety)

    def load_balance(self):
        return 1.0 - abs(self.load["surface"] - self.load["deep"])

    def total_score(self):
        return (self.safety_score() * 0.5 +
                self.stability * 0.3 +
                self.load_balance() * 0.2)


if __name__ == "__main__":
    safety = {"physical": 0.8, "emotional": 0.6, "cognitive": 0.7}
    stability = 0.65
    load = {"surface": 0.4, "deep": 0.5}

    calc = InnerSafetyCalc(safety, stability, load)
    print("Inner Safety Score:", calc.total_score())
