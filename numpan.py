# Q1 - In Pandas, a Series object can be created using various types of data like list-arrays, dictionary
# Q2
import pandas as pd
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
mon = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
series_mon = pd.Series(num, index = mon)
print(series_mon)
# Q3
import pandas as pd
mat_and_com_groups = {
    "MatMIE": 30,
    "MatDAIS": 25,
    "COMIE": 40,
    "COMEC": 45
}
series_students = pd.Series(mat_and_com_groups)
print(series_students)
# Q4
import pandas as pd
import numpy as np
exam_day = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
main_data = pd.DataFrame(exam_day, index = labels)
print(main_data)
# Q5
import pandas as pd
import numpy as np
exam_day = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
main_data = pd.DataFrame(exam_day, index=labels)
cyyt = main_data.query('attempts > 2')
print(cyyt)