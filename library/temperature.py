# Task 1
#Celsius to Fahrenheit
def c_to_f (c):

    f = (c * 9/5 ) + 32
    return f

# Celsius to Kelvin
def c_to_k (c):

    f = c + 273.15
    return f

# Fahrenheit to Celsius
def f_to_c (f):

    f = (f - 32) * 5/9
    return f

# Fahrenheit to Kelvin
def f_to_k (f):

    f = (f - 32) * 5/9 + 273.15
    return f

#Kelvin to Celsius
def k_to_c (k):

    f = k - 273.15
    return f

#Kelvin to Fahrenheit
def k_to_f (k):

    f = (k - 273.15) * 9/5 + 32
    return f
