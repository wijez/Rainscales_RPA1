import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'Age': [20, 21, 19, 22, 20, 21, 20, 22, 23, 19],
    'Gender': ['F', 'M', 'M', 'M', 'F', 'M', 'F', 'F', 'M', 'M'],
    'Score': [6.5, 4.0, 7.2, 8.0, 5.5, 3.0, 9.0, 6.0, 5.0, 4.5]
}

df_students = pd.DataFrame(data)

# Toàn bộ dữ liệu của bảng
print(df_students)


# 3 dòng đầu tiên
print(df_students.head(3)) 


# Theo index=2 và cột Name
print(df_students.loc[2, 'Name']) 


# Theo index=10 và cột Age
print(df_students.loc[9, 'Age'])


# Các cột Name và Score
print(df_students[['Name', 'Score']])


# Thêm một cột tên Pass với giá trị True nếu giá trị cột Score >= 5, ngược lại là False
df_students['Pass'] = df_students['Score'] >= 5


# Sắp xếp danh sách sinh viên theo điểm Score giảm dần.
df_sorted = df_students.sort_values(by='Score', ascending=False)
print(df_sorted)


