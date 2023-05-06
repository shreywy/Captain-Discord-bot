import cohere

def getSets():
    sets = ['backend\\datasets\\shakespeare.txt','backend\\datasets\\programmer.txt','backend\\datasets\\torontomans.txt', 'backend\\datasets\\plain.txt' ]
    datasets = [[],[],[]]
    for i in range(len(sets)):
        with open(sets[i],'r') as f:
            datasets[i] = f.read().split('\n')
    return datasets



if __name__ == '__main__':
    datasets = getSets()
    print(datasets)
    
    co = cohere.client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE')
    