# time plot using matplotlib

Visualizing is the key to extract insights from the data. We will use matplotlib box plot command to visualize the data.

## Let's write a function `box_plot()` that
* Takes input as file path. Uses first function to load the data.
* Create Boxplots a list of array values (x) for different `WorkDay` labels and their corresponding `Demand` values

'''
Ex:

Suppose we have a DataFrame:

Cookies | Holiday
50  | 0
100 | 1
200 | 0
68  | 1

If we need to plot a boxplot for cookies on grouping by Holidays

x = [[50, 200], [100, 68]]
labels = ["0", "1"]
'''

**Note : Check matplotlib boxplot documentations**


### Parameters:

Function should take list of time values and predictor variable as input and output a plot.

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory | | file path of the csv |



### Returns:
This function plots a time_plot using matplotlib plot command. This function returns nothing.
