import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# hours = [1, 2, 3, 4, 5, 6]
# marks = [30, 35, 50, 60, 70, 85]

# plt.figure(figsize=(8,5))
# sns.scatterplot( x=hours, y=marks)
# plt.show()

# raj = pd.DataFrame({
#     "date": ["2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05","2024-01-06"],
#     "hours": [1,2,3,4,5,6],
#     "marks": [30,35,50,60,70,85],
#     "gender": ["Male","Male","Female","Female","Male","Female"]
# })


# sns.scatterplot(x='hours', y='marks', hue='gender', data=raj)
# plt.title("example")
# plt.show()



# a= pd.DataFrame({
#     "date": [
#         "2024-01-01","2024-01-02","2024-01-03","2024-01-04","2024-01-05",
#         "2024-01-06","2024-01-07","2024-01-08","2024-01-09","2024-01-10"
#     ],
#     "hours": [1,2,3,4,5,2,3,4,5,6],
#     "marks": [30,40,50,60,70,35,45,55,65,80],
#     "gender": ["Male","Male","Male","Male","Male","Female","Female","Female","Female","Female"]
# })


# plt.figure(figsize=(8,6))
# sns.scatterplot(x='hours',y ='marks', hue='gender', data=a)
# plt.title('class report')
# plt.show()

# plt.figure(figsize=(8,6))
# sns.violinplot(x='hours',y ='marks', data=a)
# plt.title('class report')
# plt.show()

# df = pd.DataFrame({
#     "hours": [1,2,3,4,5,2,3,4,5,6],
#     "marks": [30,40,50,60,70,35,45,55,65,80],
#     "gender": ["Male","Male","Male","Male","Male",
#                "Female","Female","Female","Female","Female"]
# })

# sns.violinplot(x='hours',y='marks',data=df)
# plt.show()



# df = pd.DataFrame({
#     "food_type": [
#         "Pizza","Burger","Pizza","Biryani","Burger",
#         "Pizza","Biryani","Biryani","Burger","Pizza"
#     ],
#     "city": [
#         "Hyderabad","Mumbai","Hyderabad","Delhi","Mumbai",
#         "Delhi","Hyderabad","Mumbai","Delhi","Mumbai"
#     ]
# })

# sns.countplot(x='food_type',data=df,hue='city')
# plt.show()


data = [
    [10, 20, 30],
    [15, 25, 35],
    [20, 30, 40]
]

df = pd.DataFrame(data, columns=["A","B","C"] )

sns.heatmap(data=df,annot=True)
plt.show()








