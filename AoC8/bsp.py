import re

s = """Step A must be finished before step N can begin.
Step P must be finished before step R can begin.
Step O must be finished before step T can begin."""
data = re.findall("Step (.*) must be finished before step (.*) can begin.", s)
print(data) # [('A', 'N'), ('P', 'R'), ('O', 'T')]