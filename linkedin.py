# # import pandas as pd

# # # Create Series
# # s = pd.Series([1,2,3,4])
# # print(s)

# # # Create DataFrame manually
# # data = {
# #     "Names":["divyakumar","munna","beena","salar"],
# #     "ages":[32,33,42,18]
# # }
# # df1 = pd.DataFrame(data)
# # print(df1)

# # # Create DataFrame from dictionary
# # students = {
# #     "student_ID":[101,102,103,104],
# #     "student_name":["ansar","varun","sandeep","deepthi"],
# #     "Grades":["A","B","F","D"]
# # }
# # students_df = pd.DataFrame(students)
# # print(students_df)


# # # Read data from file
# # df = pd.read_csv("employee_sales_data.csv")
# # # df = pd.read_json("d1.json")

# # print(df.head())
# # print(df.tail())


# # # Basic data inspection
# # print(df.info())
# # print(df.describe())
# # print(df.shape)
# # print(df.columns)
# # print(df.dtypes)


# # # Accessing data
# # print(df["salary"])          # column
# # print(df.loc[3,"salary"])    # label based
# # print(df.iloc[3,2])          # position based
# # print(df.at[3,"salary"])     # fast single value
# # print(df.iat[3,2])           # fast single value

# # # Filtering data
# # print(df[df["salary"] > 50000])

# # print(df[(df["salary"] > 60000) & (df["rating"] > 4)])

# # print(df[(df["department"] == "IT") | (df["department"] == "HR")])


# # # Special filters
# # print(df[df["department"].isin(["Sales","Marketing"])])

# # print(df[df["salary"].between(45000,65000)])


# # # Query method
# # print(df.query("salary > 60000"))
# # print(df.query("department == 'IT'"))


# # # Missing values
# # print(df.isnull())
# # print(df.notnull())

# # print(df[df["rating"].isnull()])

# # # Handling missing values
# # df.dropna()
# # df.dropna(axis=1)
# # df.fillna(0)
# # df["rating"].fillna(df["rating"].mean())
# # # Replace values
# # df.replace("Charlie","Bujji")

# # # Save file
# # df.to_csv("output.csv")

# import pandas as pd
# df = pd.read_csv("employee_sales_data.csv")

# # Rename columns
# print(df.rename(columns={"experience_years":"experience"}))
# print(df.rename(columns={"sales":"total_sales"}))
# print(df.rename(columns={"department":"dept","region":"location"}))

# # Sorting data
# print(df.sort_values("salary"))
# print(df.sort_values("salary",ascending=False).head(5))
# print(df.sort_values(["department","salary"],ascending=[True,False]))
# print(df.sort_values("rating",ascending=False).head(3))
# print(df.sort_index())
# print(df.sort_index(ascending=False))

# # Ranking
# df["salary_rank"]=df["salary"].rank(method="dense",ascending=False)
# print(df)
# df["sales_rank"]=df["sales"].rank(method="max",ascending=False)
# print(df)
# df["dept_rank"]=df.groupby("department")["salary"].rank(method="dense",ascending=False)
# print(df)

# # Duplicate handling
# print(df.duplicated())
# print(df.drop_duplicates())
# print(df.drop_duplicates(keep="first"))

# # Statistical analysis
# print(df["salary"].sum())
# print(df["salary"].min())
# print(df["salary"].max())
# print(df["department"].mode())
# print(df["salary"].median())
# print(df["salary"].std())
# print(df["salary"].var())
# print(df["rating"].count())
# print(df["department"].value_counts())
# print(df.groupby("department")["salary"].mean())



# import pandas as pd

# # Load datasets
# first = pd.read_csv("./employees_dataset.csv")      # Contains employee details
# sec = pd.read_csv("./performance_dataset.csv")      # Contains performance metrics


# # TRANSPOSE
# # Convert rows into columns and columns into rows
# print(first.T)


# # CONCAT
# # Combine datasets together

# # Vertical concatenation (stack rows)
# print(pd.concat([first, sec], axis=0))

# # Horizontal concatenation (add columns)
# print(pd.concat([first, sec], axis=1))

# # Concatenate with outer join (keep all columns)
# print(pd.concat([first, sec], axis=1, join='outer'))


# # MERGE (SQL-like joins)
# # Combine datasets using common columns

# # Inner join → only matching rows
# print(pd.merge(first, sec, how="inner"))

# # Cross join → every row with every other row
# print(pd.merge(first, sec, how="cross"))

# # Left join → keep all rows from first dataset
# print(pd.merge(first, sec, how="left"))

# # Right join → keep all rows from second dataset
# print(pd.merge(first, sec, how="right"))


# # JOIN
# # Join datasets based on index

# print(first.join(sec))                       # basic join
# print(first.join(sec, rsuffix='_sec'))       # add suffix to avoid column conflict
# print(first.join(sec, lsuffix='_first'))
# print(first.join(sec, rsuffix='_sec', lsuffix='_first'))

# # Join using specific column
# print(first.join(sec, on='employee_id', rsuffix='_sec'))


# # COMBINE_FIRST
# # Fill missing values in one dataset using another dataset

# d1 = {
#     "company": ['adani','tata','jio','birla','amul'],
#     "revenue": [20,40,None,10,5]
# }

# d2 = {
#     "company": ['adani','tata','jio','birla','amul'],
#     "revenue": [20,40,50,10,5]
# }

# d1 = pd.DataFrame(d1)
# d2 = pd.DataFrame(d2)

# print(d1)
# print(d2)

# # Fill missing values in d1 using values from d2
# print(d1.combine_first(d2))


# # INDEX OPERATIONS

# # Set employee_id as index
# print(first.set_index('employee_id'))

# # Reset index back to column
# print(first.reset_index())

# # Sort by index
# print(first.sort_index(ascending=False))


# # REINDEX
# # Change row and column labels
# print(d1.reindex(['a','b','c'], columns=['a','b']))


# # PIVOT TABLE
# # Summarize data using aggregation

# print(pd.pivot_table(first,
#                      index="employee_id",
#                      columns="department",
#                      values="salary"))


# # Load another dataset
# df = pd.read_csv("./employee_sales_data.csv")

# # Pivot sales by region
# print(pd.pivot_table(df,
#                      index="employee_id",
#                      columns="region",
#                      values="salary"))

# # Pivot with aggregation
# print(pd.pivot_table(df,
#                      index="employee_id",
#                      columns="region",
#                      values="sales",
#                      aggfunc="mean"))


# # MELT
# # Convert wide format to long format
# print(pd.melt(df))

# print(pd.melt(df,
#               id_vars=["employee_id","region"],
#               value_vars=["rating","sales"],
#               var_name="items"))


# # PIVOT
# # Reshape dataset into table format
# print(pd.pivot(df,
#                columns=["department","region"]))


# # STACK / UNSTACK
# # Convert columns to rows and vice versa
# print(df.stack())
# print(df.unstack())

# import matplotlib.pyplot as plt

from matplotlib import pyplot as plt 

# Sample Data
months = ["Jan","Feb","Mar","Apr","May"]
sales = [200, 250, 300, 280, 350]

hours = [1,2,3,4,5]
marks = [35,40,50,65,80]

marks_dist = [35,40,45,50,55,60,65,70,75,80,85,90]

labels = ["A","B","C","D"]
values = [30, 25, 20, 25]

# Create subplots (2 rows, 2 columns)
fig, ax = plt.subplots(2,2, figsize=(10,8))

#  Line Plot
ax[0,0].plot(months, sales, marker='o')
ax[0,0].set_title("Sales Trend")
ax[0,0].set_xlabel("Months")
ax[0,0].set_ylabel("Sales")

#  Scatter Plot
ax[0,1].scatter(hours, marks)
ax[0,1].set_title("Study vs Marks")
ax[0,1].set_xlabel("Hours")
ax[0,1].set_ylabel("Marks")

#  Histogram
ax[1,0].hist(marks_dist, bins=5, edgecolor='black')
ax[1,0].set_title("Marks Distribution")

#  Pie Chart
ax[1,1].pie(values, labels=labels, autopct='%1.1f%%')
ax[1,1].set_title("Category Share")

# Adjust layout
plt.tight_layout()

plt.savefig("sales_plot.png")

plt.show()
















