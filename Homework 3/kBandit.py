import numpy as np
import matplotlib.pyplot as plt

def getSamplar():
    mu=np.random.normal(0,10)
    sd=abs(np.random.normal(5,2))
    getSample=lambda: np.random.normal(mu,sd)
    return getSample

def e_greedy(Q, e):
    if np.random.rand() < e:
        return np.random.choice(list(Q.keys()))
    else:
        best_value = None
        best_actions = list()
        for action, value in Q.items():
            if best_value == None or value > best_value:
                best_value = value
                best_choices = [ action ]
            elif value == best_value:
                best_choices.append(action)
        return np.random.choice(best_choices)
    
def upperConfidenceBound(Q, N, c):
    t = sum(N.values()) + 1
    best_value = None
    best_actions = list()
    for action, value in Q.items():
        ucb = value + c * np.sqrt(np.log(t) / N[action]) if N[action] else float('inf')
        if best_value == None or ucb > best_value:
            best_value = ucb
            best_choices = [ action ]
        elif ucb == best_value:
            best_choices.append(action)
    return np.random.choice(best_choices)

def updateQN(action, reward, Q, N):
    QNew, NNew = Q.copy(), N.copy()
    NNew[action] += 1
    QNew[action] += (reward - Q[action]) / NNew[action]
    return QNew, NNew

def decideMultipleSteps(Q, N, policy, bandit, maxSteps):
    actionReward = list()
    for _ in range(maxSteps):
        action = policy(Q, N)
        reward = bandit(action)
        actionReward.append((action, reward))
        Q, N = updateQN(action, reward, Q, N)
    return {'Q':Q, 'N':N, 'actionReward':actionReward}

def plotMeanReward(actionReward,label):
    maxSteps=len(actionReward)
    reward=[reward for (action,reward) in actionReward]
    meanReward=[sum(reward[:(i+1)])/(i+1) for i in range(maxSteps)]
    plt.plot(range(maxSteps), meanReward, linewidth=0.9, label=label)
    plt.xlabel('Steps')
    plt.ylabel('Average Reward')

def main():
    np.random.seed(2020)
    K=10
    maxSteps=1000
    Q={k:0 for k in range(K)}
    N={k:0 for k in range(K)}
    testBed={k:getSamplar() for k in range(K)}
    bandit=lambda action: testBed[action]()
    
    policies={}
    policies["e-greedy-0.5"]=lambda Q, N: e_greedy(Q, 0.5)
    policies["e-greedy-0.1"]=lambda Q, N: e_greedy(Q, 0.1)
    policies["UCB-2"]=lambda Q, N: upperConfidenceBound(Q, N, 2)
    policies["UCB-20"]=lambda Q, N: upperConfidenceBound(Q, N, 20)
    
    allResults = {name: decideMultipleSteps(Q, N, policy, bandit, maxSteps) for (name, policy) in policies.items()}
    
    for name, result in allResults.items():
         plotMeanReward(allResults[name]['actionReward'], label=name)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',ncol=2, mode="expand", borderaxespad=0.)
    plt.show()
    


if __name__=='__main__':
    main()
