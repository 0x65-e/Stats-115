
def expect(xDistribution, function):
    return sum([ function(x) * p_x for x, p_x in xDistribution.items() ])

 
def getVariance(xDistribution):
    mu = expect(xDistribution, lambda x: x)
    return expect(xDistribution, lambda x: (x - mu) ** 2)


def main():
    xDistributionExample1={1: 1/5, 2: 2/5, 3: 2/5}
    functionExample1=lambda x: x ** 2
    print(expect(xDistributionExample1, functionExample1))
    print(getVariance(xDistributionExample1))
    
    xDistributionExample2={1: 1/6, -1/2: 1/3, 1/3: 1/4, -1/4: 1/12, 1/5: 1/6}
    functionExample2=lambda x: 1/x
    print(expect(xDistributionExample2, functionExample2))
    print(getVariance(xDistributionExample2))


if __name__ == '__main__':
    main()