import pandas as pd

# load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('Cars.csv')

# display the first five and last five rows of the resulting cars
cars_preview = pd.concat([cars.head(), cars.tail()])
cars_preview