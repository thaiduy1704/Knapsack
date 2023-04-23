def str_to_item(s):
    s = [int(el) for el in s.split()]
    return (s[0], s[1])


def readData(file):
    with open(file, 'r') as reader:
        lines = reader.readlines()
        lines = map(lambda s: s.replace('\n', ''), lines)
        lines = filter(lambda s: s != '', lines)
        lines = list(lines)
        c = int(lines[1])
        items = lines[2:]
        items = list(map(str_to_item, items))
        values = [item[0] for item in items]
        weights = [[item[1] for item in items]]
        capacities = [c]
        return values, weights, capacities


def main():
    values, weights, capacities = readData('test.kp')
    print(values[0], weights[0][0])


if __name__ == '__main__':
    main()