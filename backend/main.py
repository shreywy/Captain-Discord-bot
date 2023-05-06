import cohere

def getSets():
    sets = ['backend\\datasets\\shakespeare.txt','backend\\datasets\\programmer.txt','backend\\datasets\\torontomans.txt']
    datasets = [[],[],[]]
    for i in range(len(sets)):
        with open(sets[i],'r') as f:
            datasets[i] = f.read().split('\n')
    return datasets

def getResponse(style, text):
    
    if style == "":
        style = 'command-xlarge-nightly'
    
    co = cohere.Client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE') # This is your trial API key
    response = co.generate(
    model=style,
    prompt=text,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return ('Prediction: {}'.format(response.generations[0].text))


if __name__ == '__main__':
    #datasets = getSets()

    print(getResponse("", 'describe a dog'))
    