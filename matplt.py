import matplotlib.pyplot as plt
# import pandas as pd
# import seaborn as sns
# import numpy as np

# x=[5,2,7]
# y=[2,16,4]
# plt.title("infomation")
# plt.plot(x,y)
# plt.show()

# x=[1,2,3]
# y1=[10,20,30]
# y2=[15,25,35]
# plt.plot(x,y1, marker='o', label='Product A',linestyle="--")
# plt.plot(x,y2, marker='o',label='Product B')
# plt.title("Company")
# plt.xlabel("month")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()

# x=[1,2,3,4,5,6,7,]
# y=[15,10,20,15,30,25,40]
# plt.plot(x,y,'o' ,ms=5,mec='r',mfc='y',color='k' ,linestyle="solid")
# plt.grid()
# plt.show()
# plt.plot(y,color='b',linewidth=5)
# plt.show()

# x=[1,2,3]
# y1=[10,20,30]
# y2=[15,25,35]

# plt.subplot(2,1,1)
# plt.plot(x,y1)

# plt.subplot(2,1,2)
# plt.plot(x,y2)

# plt.show()

# data = {
#     "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
#     "Sales": [200, 250, 300, 280, 350, 400],
#     "Profit": [50, 70, 90, 60, 100, 120],
#     "Expenses": [150, 180, 210, 220, 250, 280],
#     "Product": ["A", "B", "C", "A", "B", "C"],
#     "Region": ["North", "South", "East", "West", "North", "South"]
# }

# df = pd.DataFrame(data)
# print(df)

# x=df['Month']
# y=df['Sales']
# plt.plot(x,y)
# plt.title("Sales vs Month ")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.show()

# x=df['Month']
# y=df['Profit']
# plt.plot(x,y)
# plt.title("Sales vs Month ")
# plt.xlabel('months')
# plt.ylabel('profit')
# plt.show()

# plt.bar(df["Month"],df["Sales"])
# plt.show()

# plt.bar(df["Month"],df["Profit"])
# plt.show()


# df['Product'].value_counts().plot(kind='pie')
# plt.show()
# df["Region"].value_counts().plot(kind='pie')
# plt.show()

# x=df['Month']
# y=df['Expenses']
# plt.plot(x,y)
# plt.title("Expenses vs Month ")
# plt.xlabel('months')
# plt.ylabel('profit')
# plt.show()

# df['Expenses'].value_counts().plot(kind='pie')
# plt.show()

# plt.bar(df["Month"],df["Expenses"])
# plt.show()


# x=df['Month']
# y=df['Sales']
# plt.plot(x,y,'o',linestyle=':')
# plt.title("Sales vs Month ")
# plt.xlabel('months')
# plt.ylabel('sales')
# plt.show()

# x=df['Month']
# y=df['Profit']
# plt.plot(x,y,'o',linestyle='--')
# plt.title("Sales vs Month ")
# plt.xlabel('months')
# plt.ylabel('Profit')
# plt.show()

# labels = ['A', 'B', 'C']
# values = [40, 30, 30]

# plt.pie(values)
# plt.show()

# plt.pie(df["Sales"],autopct='%1.3f%%',labels=df['Month'],explode=[0.2,0,0.5,0,0,0] )
# plt.show()
 
# plt.bar(df['Month'],df['Sales'],color='k',align='edge')
# plt.show()

# plt.scatter([1,2,3,4,5,6],[15,20,25,30,35,40])
# plt.show()

# plt.scatter(df['Month'],df['Sales'],marker='*',alpha=0.6)
# plt.show()

# # Dataset 1 (Group A)
# hours_A = [1,2,3,4,5,6,2,3,4,5]
# marks_A = [28,35,45,55,65,70,33,48,52,60]

# # Dataset 2 (Group B)
# hours_B = [1,2,3,4,5,6,2,3,4,5]
# marks_B = [32,40,50,60,72,85,38,55,63,75]

# plt.scatter(hours_A, marks_A, color='blue', label='Student Group A',alpha=0.5)
# plt.scatter(hours_B, marks_B, color='red', label='Student Group B',alpha=0.5)

# plt.xlabel('Hours')
# plt.ylabel('Marks')

# plt.show()



# x=[1,2,3,4,5,6,7,8,9]
# y=[200,150, 100,250, 300, 280, 350, 400,150,]
# plt.plot(x,y)
# plt.xlabel("Months")
# plt.ylabel("Salary")
# plt.show()/

# plt.figure()
# plt.axes()
# plt.show()

# name=['dad','mom','daughter','son']
# age=[50,45.21,18]
# print(list(zip(name,age)))

# marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 60, 65, 70]

# plt.hist(marks,bins=6)

# sns.histplot(marks,bins=6,kde=True)
# plt.show()
 
# from matplotlib.animation import FuncAnimation
# x,y=[],[]
# fig,ax=plt.subplots()
# line,=ax.plot([],[],marker='*')
# ax.set_xlim(0,10)
# ax.set_ylim(0,100)
# def update(frame):
#     x.append(frame)
#     y.append(frame*10)
#     line.set_data(x,y)
#     return line,
# ani=FuncAnimation(fig,update,frames=10,interval=10)
# plt.show()



