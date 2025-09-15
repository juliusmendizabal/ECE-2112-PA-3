import pandas as pd

# load the corresponding .csv file into a data frame named cars using pandas
cars = pd.read_csv('Cars.csv')

# display the first five rows with odd-numbered columns (columns 1, 3, 5, 7...) of cars.
odd_cols = cars.iloc[0:5,[1,3,5,7,9,11]]
print(odd_cols)

# display the row that contains the 'Model' of 'Mazda RX4'
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
print(mazda_rx4)

# how many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"Camaro Z28 has {camaro_cyl} cylinders.")

# determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
print(subset)