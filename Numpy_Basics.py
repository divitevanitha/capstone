import numpy as np
numpyBasic_array = np.array([1,2,3,4,3,6,1,3.6,9])
print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)
print(numpyBasic_array.size)


#2D_arrays

array_1D = np.array(([[[1,2,3],[3,4,5]],[[1,2,3],[3,4,5]]]))
array_2D = np.array([[1,2,3],[3,4,5],[6,7,8]])
print(array_2D)
print(array_1D)
print("Dimensions:{}".format(array_2D.ndim))
print("Dimensions:{}".format(array_1D.ndim))
print("shape:{}".format(array_2D.shape))
print("shape:{}".format(array_1D.shape))
print("Array Dtype:{}".format(array_2D.dtype))
print("Array Dtype:{}".format(array_1D.dtype))

array_2D = np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)
#accessing arrays
array_x = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(array_x)
print(array_x.size)

print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[:,-3])
print(array_x[1])

#step_start:end:stepsize
print(array_x[0,0:4:3])
print(array_x[:,0:4:2])
array_x[0,2] = 10
array_x[:,2] = 10
print(array_x)


#3d_array
array_3d = np.array(([[[1,2],[3,4]],[[5,6],[7,8]]]))
print(array_3d[:,:,0])

#3d array updation

array_3d[:,0,:] = 100
print(array_3d)
print(array_3d[:,0,:])
array_3d[:,0,:] = [[10,10],[20,20]]
print(array_3d)


array_3d = np.array([[[1,2],[3,4]],[[1,2],[3,4]]])
print(array_3d)
print(array_3d.shape)

#common arrays
#one's two's empty
print(np.zeros(3))
print(np.ones(3))
two_d = np.zeros((3,2,3))
print(two_d)
three_d = np.zeros((2,3,3))
print(three_d)
four_d = np.zeros((2,3,3,2))
print(four_d)
print(np.full((2,2),3))
print(np.full((2,2),[2,5],dtype="int32"))
array_a = [1,2,3]
print(np.full_like(array_a,4))
array_r = [1,2,3]
array_repeat = np.repeat(array_r,3,axis=0)
print(array_repeat)
array_r = [[1,2,3],[4,5,6]]
array_repeat = np.repeat(array_r,3,axis=1)
print(array_repeat)

array_zeros = np.zeros((3,3))
array_zeros[1,1] = 7
print(array_zeros)

updated_array = np.zeros((5,5))
updated_array[1:-1, 1:-1] = array_zeros
print(updated_array)

#copying arrays
array_x = np.array([1,2,3,4])
array_y = array_x
array_y[0]=7
print(array_x)
print(array_y)

array_x = np.array([1,2,3,4])
array_y = array_x.copy()
array_y[0]=7
print(array_x)
print(array_y)

#math operations
array_math = np.array([1,2,3])
print("Declared array:{}".format(array_math))
print("add 10 to array:{}".format(array_math+10))
print("sub 10 from array:{}".format(array_math-10))
print("raise to power array:{}".format(array_math**2))
print("mul array :{}".format(array_math*5))
print("div array:{}".format(array_math/2))

array = np.array([1,2,3])
print("Declared array:{}".format(array))
print("add 10 to array:{}".format(array+10))
print("sub 10 from array:{}".format(array-10))
print("raise to power array:{}".format(array**2))
print("mul array :{}".format(array*5))
print("div array:{}".format(array/2))

#statistics
n_a = [[1,1,1,1],[0,0,0,0,0,0,0]]
print(n_a)

array_stats = [[3, 2, 1, 8], [4, 5, -6, 0]]

print(np.min(array_stats))
print(np.min(array_stats, axis=0))
print(np.min(array_stats, axis=1))

print(np.max(array_stats))
print(np.max(array_stats, axis=1))

print(np.sum(array_stats, axis=1))
print(np.sum(array_stats, axis=0))

# reshape

array_stats = np.array([[1, 2, 3, 7], [4, 5, -6, 4]])

print(array_stats.reshape((4, 2)))

# stacking

a_v1 = np.array([1, 2, 3])

a_v2 = np.array([1, 2, 3])

a_v3 = np.array([7, 8, 9])

print(np.array([a_v1, a_v2, a_v3]))

print(np.hstack([a_v1, a_v2, a_v3]))

# arange - array range

one_d = np.arange(6)
print(one_d)

two_dim = np.arange(12).reshape(4, 3)
print(two_dim)
print(two_dim.shape)

three_dim = np.arange(24).reshape(2, 3, 4)
print(three_dim)
print(three_dim.shape)

print(np.arange(5))

array_one = np.array([10, 20, 30, 40])
array_two = np.arange(10, 50, 10)

print(array_one * array_two)  # array multiplication
print(array_one @ array_two)  # matrix multiplication -- sum of final elements
print(array_one.dot(array_two))

print(array_two)

print(array_two - array_one)

# nupmy array as a list

array_l = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 23, 45, 6, 7])

# numpy arrays can be indexed as list

print(array_l[[1, 3, 5, 7, 4]])



############################################################



data_from_text_file = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',')

print(data_from_text_file)

data_from_text = data_from_text_file.astype('int32')
print(data_from_text)

print(data_from_text > 10)
# advance indexing

print(data_from_text[data_from_text > 0])


print(data_from_text[data_from_text < 0])
# fill values

fill_values = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',', dtype=np.int32)
print(fill_values)

fill_values = np.genfromtxt('Numpy_Data.txt' ,delimiter= ',', dtype=np.int32, filling_values = 100)
print(fill_values)



def numpy_function(x,y):
    return 15 * x + y

b = np.fromfunction(numpy_function, (3, 3), dtype=int )

print(b)

