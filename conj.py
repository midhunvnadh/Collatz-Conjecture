from time import sleep
import json
import matplotlib.pyplot as plt


def checkEven(no):
    return no % 2 == 0


def printJSON(parsed):
    print(json.dumps(parsed, indent=4))


def getDetails(nos):
    min = nos[0]
    max = nos[0]
    sum = 0
    for x in nos:
        if (x > max):
            max = x
        sum = sum + x
    return {"max": max, "sum": sum, "iterations": len(nos)}


def main(start):
    start = abs(start)
    no = int(start)
    outcomes = []
    while (True):
        outcomes.append(no)

        if (no == 1 or no == -1):
            break

        if (checkEven(no)):
            no = int(no / 2)
        else:
            no = int((3 * no) + 1)
    return {"start": start, "details": getDetails(outcomes)}


results = []
xAxis = []
yAxis = []
for x in range(1, 100):
    data = main(x)
    results.append(data)
    xAxis.append(data["start"])
    yAxis.append(data["details"]["iterations"])

plt.plot(xAxis, yAxis)
plt.xlabel('Number')
plt.ylabel('Iterations')
plt.title('My first graph!')
plt.show()