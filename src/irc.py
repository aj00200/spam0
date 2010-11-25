import time
callback=None
def set_callback(callback_function):
    '''Set a callback function. This function will be called when all the calculations have been preformed and averaged based on the multipliers. It will send 2 parameters, the spam score, and the message that was recieved:
    callback(score,message)

This is used so that threading can be implemented at a later time if spam calculations end up taking a long time in the future.'''
    callback=callback_function
variables={
    #Multipliers for values in the final calculation
    'bayesian_value':1,
    'character_frequency_value': 1,
    'max_storage': 7
}
def set_variable(name,value):
    '''Set the variable, name, to a value, value. These variables are multipliers and other variables used during the calculation of the spam ranking. These can be tweaked with this function to achieve the mest results.'''
    variables[name]=value
def get_variable(name):
    '''Return the values of a variable, name, which is used to calculate the spam ranking. This can be used with set_variable to tweak the outcome of the program.'''
    return variables[name]

data={
    'nicks':{},
    'hosts':{},
    'channel':{}
}
def run_checks(nick,host,channel,message):
    '''Run checks on an IRC message.
    - nick: the nicname of the user sending the message,
    - host: the host of the user sending the message,
    - channel: the channel the message was sent in,
    - message: the actual message that was sent'''
    append_to_data(nick,host,channel,message)
def append_to_data(nick,host,channel,message):
    if nick in data['nicks']:
        data['nicks'][nick].append((time.time(),channel,message))
        if len(data['nicks'][nick]) > variables['max_storage']:
            data['nicks'][nick].pop(0)
    else:
        data['nicks'][nick]=[(time.time(),channel,message)]
