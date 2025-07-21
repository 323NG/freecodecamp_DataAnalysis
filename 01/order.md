create a function named calculated()
uses numpy to output the mean, variance, std dev, max, min, and sum of the rows, columns, and elements in a 3x3 matrix

if the input should be list containing 9 digits.
the funtion need to return 3x3 numpy array
and a dictionary containing the mean, variance, std dev, max, min, and sum

should be like this
{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

if list is not containing 9 elements, it should raise a value KeyError
with the message "list must containe nine numebers."

the values in the returned dict should be lists and not numpy arrays

calculate([0,1,2,3,4,5,6,7,8])

return:
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}