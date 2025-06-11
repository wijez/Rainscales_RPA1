import pandas as pd
import numpy as np

data_nv = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['An', 'Bình', 'Cường', 'Dương', np.nan, 'Hạnh'],
    'Age': [25, np.nan, 30, 22, 28, 35],
    'Department': ['HR', 'IT', 'IT', 'Finance', 'HR', np.nan],
    'Salary': [700, 800, 750, np.nan, 710, 770]
}

df_nv = pd.DataFrame(data_nv)

data_pb = {
    'Department': ['HR', 'IT', 'Finance', 'Marketing'],
    'Manager': ['Trang', 'Khoa', 'Minh', 'Lan']
}

df_pb = pd.DataFrame(data_pb)


print(df_nv.isnull())
print("\nSố lượng ô thiếu mỗi cột:")
print(df_nv.isnull().sum())

print("\n xóa những dòng có hơn 2 giá trị thiếu:")
df_nv = df_nv[df_nv.isnull().sum(axis=1) <= 2]

df_nv.fillna({
    'Name': 'Chưa rõ', 
    'Age': df_nv['Age'].mean(), 
    'Salary': df_nv['Salary'].ffill(),
    'Department': 'Unknown',
    }, inplace=True)

df_nv['Salary'] = df_nv['Salary'].astype(int)
df_nv['Age'] = df_nv['Age'].astype(int)
df_nv['Salary_after_tax'] = df_nv['Salary'] * 0.9

print("Các thành viên có tuổi lớn hơn 25 thuộc phòng IT:", end='\n')
it_members = df_nv[(df_nv['Department'] == 'IT') & (df_nv['Age'] > 25)]
print(it_members[['ID', 'Name', 'Age']].to_string(index=False))

print("Nhóm theo Department và tính lương trung bình:", end='\n')
average_salary_by_department = df_nv.groupby('Department')['Salary'].mean()
print(average_salary_by_department)

print("Manager của mỗi nhân viên", end='\n')
df_merge = pd.merge(df_nv,df_pb, on='Department', how='left')
print(df_merge, end='\n')

new_employees = pd.DataFrame({
    'ID': [107, 108],
    'Name': ['Lan', 'Minh'],
    'Age': [26, 24],
    'Department': ['IT', 'HR'],
    'Salary': [720, 750]
})

new_employees['Salary_after_tax'] = new_employees['Salary'] * 0.9
df_final = pd.concat([df_nv, new_employees], ignore_index=True)

print("\nBảng dữ liệu sau khi xử lý:")
print(df_final)