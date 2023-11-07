from pomegranate import *
#  pip install pomegranate==0.14.8 

Burglar = DiscreteDistribution({"T": 0.001, "F": 0.999})
Earthquake = DiscreteDistribution({"T": 0.002, "F": 0.998})

Alarm = ConditionalProbabilityTable(
    [
        ["T", "T", "T", 0.95],
        ["T", "T", "F", 0.05],
        ["T", "F", "T", 0.94],
        ["T", "F", "F", 0.06],
        ["F", "T", "T", 0.29],
        ["F", "T", "F", 0.71],
        ["F", "F", "T", 0.001],
        ["F", "F", "F", 0.999],
    ],
    [Burglar, Earthquake],
)

JohnCalls = ConditionalProbabilityTable(
    [["T", "T", 0.90], ["T", "F", 0.10], ["F", "T", 0.05], ["F", "F", 0.95]],
    [Alarm],
)

MaryCalls = ConditionalProbabilityTable(
    [["T", "T", 0.70], ["T", "F", 0.30], ["F", "T", 0.01], ["F", "F", 0.99]],
    [Alarm],
)


s1 = State(Burglar, name="Burglar")
s2 = State(Earthquake, name="Earthquake")
s3 = State(Alarm, name="Alarm")
s4 = State(JohnCalls, name="JohnCalls")
s5 = State(MaryCalls, name="MaryCalls")


network = BayesianNetwork("Burglar Alarm Network")
network.add_states(s1, s2, s3, s4, s5)


network.add_edge(s1, s3)
network.add_edge(s2, s3)
network.add_edge(s3, s4)
network.add_edge(s3, s5)

network.bake()


result = network.predict_proba({"Burglar": "T", "Earthquake": "F", "JohnCalls": "F"})

print(result[4])
