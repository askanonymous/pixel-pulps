import csv
def countndpreprocess(csv_reader):
    for row in csv_reader:
        if row['PREVAILING_WAGE'] != '' and row['PREVAILING_WAGE'] != 'NoneType':
          count = count + 1
          if row['PW_UNIT_OF_PAY'] == 'Hour':
              row['PREVAILING_WAGE'] = 2080 * float(row['PREVAILING_WAGE'])
              sum = sum + row['PREVAILING_WAGE']
          elif row['PW_UNIT_OF_PAY'] == 'Bi-Weekly':
              row['PREVAILING_WAGE'] = 26 * float(row['PREVAILING_WAGE'])
              sum = sum + row['PREVAILING_WAGE']
          elif row['PW_UNIT_OF_PAY'] == 'Week':
              row['PREVAILING_WAGE'] = 52 * float(row['PREVAILING_WAGE'])
              sum = sum + row['PREVAILING_WAGE']
          elif row['PW_UNIT_OF_PAY'] == 'Month':
              row['PREVAILING_WAGE'] = 12 * float(row['PREVAILING_WAGE'])
              sum = sum + row['PREVAILING_WAGE']
          else:
            row['PREVAILING_WAGE'] = float(row['PREVAILING_WAGE'])
            sum = sum + row['PREVAILING_WAGE']
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def calculate_median(arr):
    sorted_arr = quick_sort(arr)
    n = len(sorted_arr)
    
    if n % 2 == 1:
        # If the length of the array is odd, return the middle element
        return sorted_arr[n // 2]
    else:
        # If the length of the array is even, return the average of the two middle elements
        middle1 = sorted_arr[(n // 2) - 1]
        middle2 = sorted_arr[n // 2]
        return (middle1 + middle2) / 2
def calculate_25th_percentile(arr):
    sorted_arr = quick_sort(arr)
    n = len(sorted_arr)
    
    # Calculate the position for the 25th percentile
    position = 0.25 * (n + 1)
    
    if position.is_integer():
        # If the position is an integer, return the value at that position
        return sorted_arr[int(position) - 1]  # Subtract 1 because indexing is 0-based
    else:
        # Interpolate between the values at the positions above and below
        lower_position = int(position)
        upper_position = lower_position + 1
        lower_value = sorted_arr[lower_position - 1]
        upper_value = sorted_arr[upper_position - 1]
        
        # Interpolate using linear interpolation
        interpolation_factor = position - lower_position
def calculate_75th_percentile(arr):
    sorted_arr = quick_sort(arr)
    n = len(sorted_arr)
    
    # Calculate the position for the 75th percentile
    position = 0.75 * (n + 1)
    
    if position.is_integer():
        # If the position is an integer, return the value at that position
        return sorted_arr[int(position) - 1]  # Subtract 1 because indexing is 0-based
    else:
        # Interpolate between the values at the positions above and below
        lower_position = int(position)
        upper_position = lower_position + 1
        lower_value = sorted_arr[lower_position - 1]
        upper_value = sorted_arr[upper_position - 1]
        
        # Interpolate using linear interpolation
        interpolation_factor = position - lower_position
        return lower_value + interpolation_factor * (upper_value - lower_value)

        
    