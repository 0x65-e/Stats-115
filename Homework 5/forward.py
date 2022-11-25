


def expect(xDistribution, function):
    fxProduct=[px*function(x) for x, px in xDistribution.items()]
    expectation=sum(fxProduct)
    return expectation


def forward(xT_1Distribution, eT, transitionTable, sensorTable):
    # Calculate the prior distribution of xT only based on xT_1 and the transition function
    prior = { next_state: expect(xT_1Distribution, lambda state: transitionTable[state][next_state]) for next_state in xT_1Distribution.keys() }
    # Update the prior using Bayes' rule based on the sensor function and evidence
    posterior = { state: sensorTable[state][eT] * prior[state] for state in prior.keys() }
    # Renormalize the posterior to sum to 1
    alpha = sum(posterior.values())
    normalized_posterior = { state: prob / alpha for state, prob in posterior.items() }
    return normalized_posterior

def main():
    
    pX0={0:0.3, 1:0.7}
    e=1
    transitionTable={0:{0:0.6, 1:0.4}, 1:{0:0.3, 1:0.7}}
    sensorTable={0:{0:0.6, 1:0.3, 2:0.1}, 1:{0:0, 1:0.5, 2:0.5}}
    
    xTDistribution=forward(pX0, e, transitionTable, sensorTable)
    print(xTDistribution)

if __name__=="__main__":
    main()