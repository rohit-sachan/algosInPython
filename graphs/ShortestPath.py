"""
Given a list of currency exchange rates like this:
EUR/USD => 1.2
USD/GBP => 0.75
GBP/AUD => 1.7
AUD/JPY => 90
GBP/JPY => 150
JPY/INR => 0.6
write a method



double convert(String sourceCurrency, double amount, String destCurrency);


For example, convert(EUR, 100, INR)
Write two implementations

1. The method should minimize the number of intermediate conversions.

2. Method should give conversion steps to get maximum conversion rate

"""
from graphs.Graph import Graph, GraphWeighted

pairs = [
    ('EUR', 'USD', 1.2),
    ('USD', 'GBP', .75),
    ('GBP', 'AUD', 1.7),
    ('AUD', 'JPY', 90),
    ('GBP', 'JPY', 150),
    ('JPY', 'INR', .6)
         ]
graph = GraphWeighted(pairs)

print(graph.__str__())
print(graph.find_path_bfs('EUR', 'INR'))
# print(graph.get_adj('GBP'))