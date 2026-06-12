import pandas as pd
# print(pandas)
# a=pandas.Series([1,2,3,4])
# print(a)
# name=pandas.Series([189,'raju','prashanth',2003,'bujji','kittu'])   #series
# print(name)

# data Frame
# cn=pandas.DataFrame({'Names':["divyakumar","munna","beena","salar"],'ages':[32,33,42,18]})
# print(cn.info())
# students={'student_ID':[101,102,103,104],'student_name':['ansar','varun','sandeep','deepthi'],'Grades':["A","B","F","D"]}
# see=pd.DataFrame(data=students,index=[1,2,3,4])
# print(see)

# school={'s_id':[1,2,3,4,5,6,7,8,9,10], 
#         's_name':['Divya','Sahithi','kittu','Ramya','Shivani','Vijju','Raj','Sandeep','Ansar','Praveen']}
# print(pd.DataFrame(data=school))

# df=pd.read_json('d1.json')
# print(df)
# df=pd.read_csv("C:/Users/prash/Downloads/sample_names.csv")
# # print(df.head(2))
# # print(df.tail(1))
# print(df.info())
# df=pd.read_csv("./Sales_Q2.csv")
# print(df.info())
# print(df.describe(include='all'))
# print(df.shape)
# print(df.index)
# print(df.columns)
# print(df.dtypes)
# print(df.loc[3,'Region'])
# a=input("Enter the region: ")
# print(df[df["Region"]==a])
# print(df['ProductID'])  
# a=pd.read_csv("./employee_practice_data.csv")
# print(a.head(7))
# print(a.tail(5))
# print(a.info())
# print(a.describe())
# print(a.loc[a['department']=="Sales"])
# print(a[a["salary"]>65000])

# print(pd.read_csv("./employee_practice_data.csv"))
# print(a.loc[3,"region"])
# print(a.loc[15])
# print(a.loc[:,"region"])
# print(a[a["salary"]>50000])
# print(a[a["rating"]>4])
# print(a[a["rating"]>4].info())
# top_performers=a[a['salary']>45000]
# print(top_performers)
# print(a.iloc[8,0])
# print(a.iloc[4,6])
# print(a.iloc[0:6,0:2])
# print(a.iloc[:6,:4])
# b=a.iloc[1:5,1:5]
# print(b)
# print(a.iloc[-5:,::-4])
# print(a.iloc[5,::2])
# print(a.at[15,'salary'])
# print(a.iat[14,1])
# print(a)  
# print(a.get("place"))
# print(a.query("salary>40000 and department=='IT'"))
# print(a.query(" salary>=40000 and rating==3" ))
# print(a.query('department=="Sales" and rating==4',inplace=True))
# print(a.query("department== 'IT' and region=='East' ",inplace=False))
# print(a.query('salary>50000',inplace=True))
# print(a.head(3))
# h=a[a['rating'].between(1,3)]
# print(h)
# print(a.isna()) **

# df=pd.read_csv("./employee_sales_data.csv")
# print(df)
# print(df.iloc[:3,:9])
# print(df.iloc[5:10])
# print(df.iloc[:,:4])
# print((df.loc[7]))
# print(df.loc[0,"salary"])

# #Retrieve the salary value of the employee at index 3 using at.
# print(df.at[3,'salary'])

#  #Retrieve the department value of the employee at index 0 using at.
# print(df.at[0,'department'])

#  #Retrieve the value at row index 2 and column index 4 using iat.
# print(df.iat[2,4])
#  #Retrieve the value at row index 5 and column index 6 using iat.
# print(df.iat[5,6])
#  #Select all employees where salary is greater than 60,000 using query.
# print(df.query('salary>60000'))
#  #Select employees from the IT department using query.
# print(df.query('department=="IT" '))

# df=pd.read_csv("employee_sales_data.csv")
# print(df)
# print(df["experience_years"]>5)
# print(df[df["experience_years"]>5])
# print(df[(df["experience_years"]>5) & (df["rating"]>4.5)])
# print(df[(df["experience_years"]>5) | (df["rating"]>4.5)])
# print(df[df["name"].isin(["Charlie","Ian","Bolli"])])
# print(df["name"].isin(["Charlie","Ian","Bolli"]))
# print(df["experience_years"].between(1,5))
# print(df[df["experience_years"].between(1,5)])
# print(df.notnull())
# print(df.isnull())
# print(df.isna())
# print(df.dropna(axis=1))
# print(df.dropna(axis=0))
# print(df["rating"].fillna(3.0))
# print(df.fillna(2.0, inplace=True)) 
# print(df.fillna(df["rating"].mean(),inplace=True))
# print(df.fillna(df["rating"].mean(),inplace=False))
# print(df.fillna({'rating':2.0}))
# print(df.replace("Charlie","Bujji"))
# a=df.replace("Charlie","Bujji",inplace=True)
# print(a.to_csv("./nnn.csv"))
# print(a)

# Display all rows where the rating column is null using isnull().
# print(df[df["rating"].isnull()])

# Display rows where experience_years is missing using isna().
# print(df[df["experience_years"].isna()])
# Display rows where rating is not null using notnull().
# print(df[df["rating"].notnull()])
# Display rows where experience_years is not null using notna().
# print(df[df["experience_years"].notna()])
# Select employees where salary > 50000 AND department is Sales.
# print(df[(df["salary"]>5) & (df["department"]=="Sales")])
# Select employees where department is IT OR department is HR.
# print(df[(df["department"]=="IT")|(df["department"]=="HR")])
# Select employees where salary > 60000 AND rating > 4.
# print(df[(df["salary"]>60000) & (df["rating"]>4)])
# Select employees whose department is Sales or Marketing using isin().
# print(df[(df["department"]=="Sales") | (df["department"]=="Marketing")])
# Select employees whose region is North or South.
# print(df[(df["region"]=="North") | (df["region"]=="South")])
# Select employees whose salary is between 45000 and 65000.
# print(df[df["salary"].between(45000,65000)])
# Select employees whose experience_years is between 3 and 7.
# print(df[df["experience_years"].between(3,7)])
# Remove rows where rating is missing.
# print(df.dropna(axis=0))
# Remove columns that contain any missing values using axis=1.
# print(df.dropna(axis=1))
# Fill missing values in the rating column with 0.
# print(df.fillna(0.0))
# print(df.fillna({"rating":0}))
# Example idea:
# fillna({"rating":0})


# Rename the column experience_years to experience.
# print(df.rename(columns={"experience_years":"experience"},inplace=True))
# Rename the column sales to total_sales.
# print(df.rename(columns={"sales":"total_sales"}))
# Rename multiple columns:

#     department → dept

#     region → location.

# print(df.rename(columns={"department":"dept","region":"location"}))
# Sort the dataset by salary in ascending order.
# print(df.sort_values("salary",ascending=True))
# Sort the dataset by salary in descending order and display the top 5 employees.
# print(df.sort_values("salary",ascending=False).head(5))
# Sort employees first by department and then by salary.
# print(df.sort_values(["department","salary"],ascending=[True, False]))
# Sort employees by rating in descending order, and display the top 3 highest rated employees.
# print(df.sort_values("rating",ascending=False).head(3))
# Sort the dataset by index in ascending order.
# print(df.sort_index(ascending=True))
# Sort the dataset by index in descending order.
# print(df.sort_index(ascending=False))
# Create a rank column based on salary (highest salary = rank 1).
# df["rank"]=df["salary"].rank(method="dense",ascending=True).head(5)
# print(df)
# Rank employees based on sales.
# df["rank"]=df["sales"].rank(method="max",ascending=False)
# print(df)
# Create a rank of employees within each department based on salary.
# df["rank"]=df.groupby("department")["salary"].rank(method="dense",ascending=False)
# print(df)
# Identify rows where duplicate employee_id values exist using duplicated().
# print(df.duplicated())
# Display all rows that are duplicates based on employee_id.
# print(df.drop_duplicates())
# Remove duplicate rows based on employee_id, keeping only the first occurrence
# print(df.drop_duplicates(keep="first"))

#  Find the total salary of all employees using sum().
# print(df["salary"].sum())

#  Find the minimum salary in the dataset using min().
# print(df["salary"].min())
#  Find the maximum sales value using max().
# print(df["salary"].max())
#  Find the most common department using mode().
# print(df["department"].mode())
#  Find the median salary of employees.
# print(df["salary"].median())
# #  Calculate the standard deviation of salary using std().
# print(df["salary"].std())
# #  Calculate the variance of sales values using var().
# print(df["salary"].var())
# #  Count the number of non-null ratings using count().
# print(df["rating"].count())
# #  Find how many employees belong to each department using value_counts().
# print(df["department"].value_counts())
# #  Using groupby, calculate the average salary for each departme
# print(df.groupby("department")["salary"].mean(
# print(df.T) 
# first=pd.read_csv("./employees_dataset.csv")
# sec=pd.read_csv("./performance_dataset.csv")
# print(pd.concat([first,sec],axis=0))
# print(pd.concat([first,sec],axis=1))
# # print(pd.concat([first,sec],axis=1,ignore_index=True))
# print(pd.concat([first,sec],axis=1,join='outer'))
# print(first.merge(sec),how="inner")
# print(pd.merge(first,sec,how='inner'))
# print(pd.merge(first,sec,how='cross'))
# print(pd.merge(first,sec,how='left'))
# print(pd.merge(first,sec,how='left_anti'))
# print(pd.merge(first,sec,how='right'))
# print(pd.merge(first,sec,how='right_anti'))
# print(first.join(sec))
# print(first.join(sec,rsuffix='2'))
# print(first.join(sec,lsuffix='1'))
# print(first.join(sec,rsuffix='2',lsuffix='1'))
# print(first.join(sec,rsuffix='2',lsuffix='1',on='employee_id'))
# d1={
#     "company":['aadani','tata','jio','birla','amul'],
#     "revenu":[20,40,None,10,5]
# }

# d2={
#     "company":['aadani','tata','jio','birla','amul'],
#     "revenu":[20,40,50,10,5]
# }
# d1=pd.DataFrame(d1)
# d2=pd.DataFrame(d2)
# print(d1)
# print(d2)
# print(d1.combine_first(d2))
# print(d1.T)
# print(d1)
# print(first.set_index('employee_id'))
# print(d1.reindex(['a','b','c'],columns=['a','b']))
# print(first.sort_index(ascending=False))


# Use set_index() to set employee_id as the index in both datasets.
# print(first.set_index('employee_id'))
# Use merge() to combine the two datasets using employee_id so that the final table contains employee information along with region, sales, and rating.
# print(pd.merge(first,sec))

# Use join() to combine the two datasets using the index and compare the result with merge().
# print(first.join(sec,lsuffix=2))
# Use concat() with axis=0 to stack the two datasets vertically and observe the output.
# print(pd.concat([first,sec]))
# Use concat() with axis=1 to combine the datasets horizontally.
# print(pd.concat([first,sec],axis=1))
# Use combine_first() so that missing values from one dataset are filled using values from the other dataset.
# print(first.combine_first(sec))
# Apply .T (transpose) on the employee dataset and observe how rows become columns.
# print(first.T)
# After setting employee_id as index, use reset_index() to convert the index back into a column.
# print(first.reset_index())
# print(pd.pivot_table(first,index="employee_id",columns='department',values="salary"))
# df=pd.read_csv("./employee_sales_data.csv")
# print(df)
# print(pd.pivot_table(df,index="employee_id",columns="region",values="salary"))
# print(pd.pivot_table(df, index="employee_id", columns="region", values="sales", aggfunc="mean"))
# print(pd.melt(df))
# print(pd.melt(df,id_vars=["employee_id","region"],value_vars=["rating","sales"],var_name="items"))
# print(pd.pivot(df,columns=["department","region"]))
# print(df.unstack)
# df=pd.read_csv("./employee_practice_dataset_records.csv")
# print(df)
# Create a pivot table showing the total sales for each department.
# print(pd.pivot_table(df,index="department",values="sales",aggfunc="sum"))
# Create a pivot table showing the average salary for each department.
# print(pd.pivot_table(df,index="department",values="salary",aggfunc="mean"))
# Create a pivot table showing the total sales for each department in each region.
# print(pd.pivot_table(df,index="department",columns="region" , values="salary",aggfunc="mean"))
# Create a pivot table showing the average rating for each department in each region.
# print(pd.pivot_table(df,index="department", columns="region", values="rating",aggfunc="mean"))
# Use pivot() to create a table where departments are rows, regions are columns, and sales are the values.
# print(pd.pivot(df, index="department", columns="region", values="sales"))  
# print(pd.pivot_table(df, index="department", columns="region", values="sales"))
# Use pivot() to create a table where regions are rows, departments are columns, and salary is the value.
# print(pd.pivot(df, index="region", columns="department", values="sales"))
# print(pd.pivot_table(df, index="region", columns="department", values="sales"))
# Use melt() to convert a dataset where regions are columns (North, South, East, West) into a long format where region becomes a column.
# print(pd.melt(df,id_vars=['employee_id',"region"],value_vars=['sales','salary'],value_name="pay",var_name="Type"))
# Use melt() to convert sales columns into rows while keeping department as the identifier.
# print(pd.melt(df,id_vars="department",value_vars="sales",value_name="pay",var_name="Type"))
# Create a pivot table of department and region sales and apply stack() to convert columns into rows.
# print(pd.pivot_table(df,index="department",columns="region", values="sales").stack())
# Group the dataset by department and region, calculate total sales, and apply unstack() to convert region values into columns.
# print(df.groupby(["department","region"])["sales"].sum().unstack())
# df["new"]=df.groupby("department")["salary"].transform (lambda a: a.mean())
# print(df)

# df=pd.read_csv("./data.csv")
# print(df)

# Convert the name column to uppercase using a string method.
# print(df["name"].str.upper())
# df["name"]=df["name"].str.upper()
# print(df)
# Convert the email column to lowercase.
# df["email"]=df["email"].str.lower()
# print(df)
# Find the length of each name and store it in a new column called name_length.
# df["len"]=df["name"].str.len()
# print(df)
# Extract the email domain (text after @) from the email column and store it in a new column called domain.
# df["domain"] = df["email"].str.split('@').str[1]
# print(df)
# Check which emails contain "gmail" and display those rows.
# print(df[df["email"].str.contains
# ("gmail")])
# Replace "gmail.com" with "googlemail.com" in the email column.
# print(df["email"].str.replace("gmail","googlemail"))
# df["email"]=df["email"].str.replace("gmail","googlemail")
# print(df)
# Using transform(), create a new column that shows the average salary of each department.
# print(df.groupby("department")['salary'].transform("mean"))
# df["avg"]=df.groupby("department")["salary"].transform("mean")
# print(df)
# Using transform(), create a new column that shows the total sales_q1 of each department.
# df["ts"]=df.groupby("department")["sales_q1"].transform("sum")
# print(df)
# Using transform(), create a new column that shows the maximum salary in each region.
# df["maximum_salary"]=df.groupby("region")["salary"].transform("max")
# print(df)
# Using transform(), create a new column that shows the average rating of each department.
# df["avg"]=df.groupby("department")["rating"].transform("mean")
# print(df)

# data={
#     "dept":["it","hr","hr","mgr"],
#     "region":['E','E','S','N'],
#     "sales":[150,100,180,90],
#     "salary":[90,80,85,100]
# }
# a=pd.DataFrame(data)
# # print(a)
# b=a.groupby(['dept','region'])['sales'].sum()
# # print(b)
# print(b.unstack(level=0,fill_value=0))
# d= df.groupby(["region","department"])['salary'].mean()
# # print(d)
# print(d.unstack(level=1))

df=pd.read_csv("./data.csv")
# Convert the join_date column from string to datetime format.
df['date']=pd.to_datetime(df["join_date"])
# print(df)
# print(df.info())
# Create a new column that extracts the year from the join_date column.
# df['year']=df['date'].dt.year
# print(df)
# Create a new column that extracts the month number from the join_date column.
# df["join_month"]=df["date"].dt.month
# print(df)
# Create a new column that shows the weekday name for each join_date.
# df['wd']=df["date"].dt.day_name()
# print(df)
# Create a new column that shows the quarter of the year for each join_date.
# df["q_d"]=df["date"].dt.quarter
# print(df)
# Format the join_date column into the format YYYY/MM/DD using a datetime formatting method.
# print(df["date"].dt.strftime("%Y-%m-%d"))
# Create a new column called next_review_date by adding 30 days to the join_date column.
# df["njd"]=df['date']+pd.Timedelta(days=30)
# print(df)
# Calculate the number of days between the current date and join_date.
# df['a']=pd.Timestamp.today()-df["date"]
# print(df)
# Create a date range starting from "2024-01-01" with 7 periods.
# print(pd.date_range(start="2024-01-01", periods=7))
# Set the join_date column as the index of the DataFrame.

df = df.set_index("date")
print(df)

# df['ss']=df["date"]+pd.DateOffset(days=2)
# print(df)
