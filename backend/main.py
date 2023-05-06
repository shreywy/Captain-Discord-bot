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
    elif style == "shakespeare":
        style = 'fabd149b-066d-4c74-9259-092f7f638bfd-ft'
    elif style == "programmer":
        style = '2d60718a-6428-4d76-bdfa-e7ab09df9ae6-ft'
    elif style == "toronto":
        style = '9f1426dc-5bab-41ba-84f1-b5ddf77e7d79-ft'
        
    text = "respond in under 25 words:" + text
    
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

    print(getResponse("programmer", 'damn austin you looking mad fine'))
    