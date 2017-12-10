# Split the dataset into three parts using TimeSeriesSplit

Now that you have imported the data, lets split the data using TimeSeriesSplit function from Sklearn


## Write a function `q02_data_splitter()` which splits the data into train_index, valid_index using TimeSeriesSplit function

- Use TimeSeriesSplit function from Sklearn to split the dataset into 3 parts. The output should be a list of tuples, with each tuple representing (train_index, valid_index).

## Tip:
- Load the data from the previous question(Which we have already loaded it for you)
- Use random seed= 9  and random state for the TimeSeriesSplit function to 200

### Parameters:

Function should take data, split_time and column name as input and output two DataFrames.

| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | str | compulsory |  | file path of csv file |


### Returns:

| Return | dtype | description |
| --- | --- | --- |
| List | list | List of array of data |
