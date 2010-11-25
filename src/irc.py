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
}
def set_variable(name,value):
    '''Set the variable, name, to a value, value. These variables are multipliers and other variables used during the calculation of the spam ranking. These can be tweaked with this function to achieve the mest results.'''
    variables[name]=value
def get_variable(name):
    '''Return the values of a variable, name, which is used to calculate the spam ranking. This can be used with set_variable to tweak the outcome of the program.'''
    return variables[name]
