'''python
import numpy as np

rows represent crops:[Tomatoes, Carrots, Potatoes, Onions]
columns represent days:[Monday, Tuesday, Wednasdey, Thuesday, Friday, Satuarday, Sunday]
harvest_data = np.array([[50,55,60,52,58,65,70],[30,32,28,35,33,40,42],[100,95,105,110,98,120,125],[40,38,42,45,41,50,55]])

Your Task: 
part 1: Array properties and restructuring

Write code to print the shape, no, of dimensions, and total size of the harvest_data array

The farm manager wants a report where the rows are the days of the week and the columns are the crops. Use a numpy function to restructure the array to meet this requirment.

part 2: Statistical operations
3.Weekly Crop Yield: Calculate the total yield for each crop for the entire week.
4,Daily averages: Calculate the av yield across all crops for each indivisual day.
5.Best Day: Find the maximum yield produced by any single crop on any singe day.

Part 3:Broadcasting
6.Fertilizer Bonus: Due to new fertilizer used midway through the week, the expected yield for all crops on Friday, Saturday, and Sunday increased.

you have a bonus array: daily_bonus=np.array([0,0,0,0,5,10,15](representing extra kgs per day))

Use broadcasting toadd this bonus to the harvest_data.
Crop Shrinkage(Advanced Broadcasting): During transprt, different crops experience different rates of weight loss(shrinkage).

Tomatoes lose 5%, Carrots lose 2%, Potatoes lose 1%, and Onions lose 3%.

You have a shrinkage factor array: shrinkage=np.array([0.95,0.98,0.99,0.97]).

Use broadcasting to multiply the current harvest_data(after the fertilizer bonus) by these shrinnkage factors to get the final transported weight.(Hint: You may need to reshape the shrinkage array first)
'''

import numpy as np

# Rows represent crops:
# Tomatoes, Carrots, Potatoes, Onions
# Columns represent days:
# Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday

harvest_data = np.array([
    [50, 55, 60, 52, 58, 65, 70],
    [30, 32, 28, 35, 33, 40, 42],
    [100, 95, 105, 110, 98, 120, 125],
    [40, 38, 42, 45, 41, 50, 55]
])

# --------------------------------------------------
# PART 1: Array Properties and Restructuring
# --------------------------------------------------

print("Original Harvest Data:")
print(harvest_data)

print("\nShape:", harvest_data.shape)
print("Number of dimensions:", harvest_data.ndim)
print("Total size:", harvest_data.size)

# Restructure: rows = days, columns = crops
day_crop_data = harvest_data.T

print("\nRestructured Array (Rows = Days, Columns = Crops):")
print(day_crop_data)

# --------------------------------------------------
# PART 2: Statistical Operations
# --------------------------------------------------

# 3. Weekly Crop Yield
weekly_crop_yield = np.sum(harvest_data, axis=1)

print("\nWeekly Crop Yield:")
print(weekly_crop_yield)

# 4. Daily Average Yield
daily_average = np.mean(harvest_data, axis=0)

print("\nDaily Average Yield:")
print(daily_average)

# 5. Best Day / Maximum Single Crop Yield
best_yield = np.max(harvest_data)

print("\nMaximum Yield Produced by Any Crop on Any Day:")
print(best_yield)

# --------------------------------------------------
# PART 3: Broadcasting
# --------------------------------------------------

# 6. Fertilizer Bonus
daily_bonus = np.array([0, 0, 0, 0, 5, 10, 15])

# Broadcasting adds the daily bonus to every crop
fertilized_data = harvest_data + daily_bonus

print("\nHarvest Data After Fertilizer Bonus:")
print(fertilized_data)

# Crop Shrinkage
shrinkage = np.array([0.95, 0.98, 0.99, 0.97])

# Reshape so each crop gets its own shrinkage factor
shrinkage = shrinkage.reshape(4, 1)

# Broadcasting multiplication
final_weight = fertilized_data * shrinkage

print("\nFinal Transported Weight After Shrinkage:")
print(final_weight)
