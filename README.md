# ECE-2112-PA-3

**Made by: Julius Miguel S. Mendizabal | 2ECE-C**

The content of this repository contains the Programming Assignment 3 for our course "Advance Computer Programming" this S.Y. 2025-2026. This project covers two python problems pertaining to Module 3 - Python Data Analysis (Pandas).

*All problems were first initialized with the code below to load the Pandas library and easily call the functions using 'pd'.
```python
import pandas as pd
```
# **Problem 1**

This first problem is divided into two parts, part a and part b.

In part a, we're tasked to load the corresponding .csv file into a data frame named cars using pandas. We are able to do this using the code below. 
```python
cars = pd.read_csv('Cars.csv') # this code will run for all the cells after this
```
Note: the `'Cars.csv'` must be in the same folder as the .ipynb or .py file.

<img width="378" height="60" alt="image" src="https://github.com/user-attachments/assets/35647059-1c2b-43d3-a70a-d39744544e3f" />


In part b, we're tasked to display the first five and last five rows of the resulting cars above. By using `pd.concat`, we can concatenate the two functions `cars.head()`, which gets the first five rows by default, and `cars.tail()`, which gets the last five rows by default, thus combine the output of these two into a single dataframe.
```python
cars_preview = pd.concat([cars.head(), cars.tail()])
cars_preview
```
The output of the code above is as follows:

<img width="652" height="383" alt="image" src="https://github.com/user-attachments/assets/8faae74d-3be2-42b0-9704-4e8850ac5eaf" />


# **Problem 2**

This second problem is divided into four parts, part a, part b, part c, and part d.

In part a, we're tasked to display the first five rows with odd-numbered columns of cars. By using the `.iloc` function, we can slice the number of rows needed which is `[0:5]` and get the odd-numbered columns by specifying it `[1,3,5,7,9,11]`, all through their index locations.
```python
odd_cols = cars.iloc[0:5,[1,3,5,7,9,11]]
odd_cols 
```
The output of the code above is as follows:

<img width="306" height="209" alt="image" src="https://github.com/user-attachments/assets/b7aff748-ca74-4cbb-88e9-b7a6a65581ed" />


In part b, we're tasked to display the row that contains the 'Model' of 'Mazda RX4'. Through this code `cars[cars['Model'] == 'Mazda RX4']`, we can call the row with the 'Model' name 'Mazda RX4', by default this shows all columns at this row of 'Model' name 'Mazda RX4'.
```python
mazda_rx4 = cars[cars['Model'] == 'Mazda RX4']
mazda_rx4
```
The output of the code above is as follows:

<img width="584" height="69" alt="image" src="https://github.com/user-attachments/assets/c96ba699-7cce-40e5-a3ca-9e1b4a95eb27" />


In part c, we're asked how many cylinders ('cyl') does the car model 'Camaro Z28' have? Through the `.loc` function we can filter value of 'cyl' from the 'Model' that matches with 'Camaro Z28'. In the print line, we can insert the filtered value of 'cyl' assigned to `camaro_cyl` through the f-string function as you can see below.
```python
camaro_cyl = cars.loc[cars['Model'] == 'Camaro Z28', 'cyl'].values[0]
print(f"Camaro Z28 has {camaro_cyl} cylinders.")
```
The output of the code above is as follows:

<img width="248" height="27" alt="image" src="https://github.com/user-attachments/assets/8db64742-4699-412c-ac38-ee4b2a916b56" />


In part d, we're tasked to determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have. In the code below, we first assigned the name of the models we're finding to variable 'models'. Then, using the `.loc` function, we can filter for the values of the 'cyl' and 'gear' from their corresponding models, `.isin()` helps by filtering the rows whether the values of 'models' are in the list of 'Model'.

```python
models = ['Mazda RX4 Wag', 'Ford Pantera L', 'Honda Civic']
subset = cars.loc[cars['Model'].isin(models), ['Model', 'cyl', 'gear']]
subset
```
The output of the code above is as follows:

<img width="245" height="137" alt="image" src="https://github.com/user-attachments/assets/6f32c3be-6e99-4c31-9e8b-1b0abf86795a" />


Thank you for reading! 

To see the main python programs for Programming Assignment 3, click this link https://github.com/juliusmendizabal/ECE-2112-PA-3 and download the .ipynb file or the .py file. Open on Jupyter Notebook, then run all cells.
