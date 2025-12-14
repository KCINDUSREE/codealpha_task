import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Units_Sold': [120, 150, 180, 170, 200],
    'Revenue': [24000, 30000, 36000, 34000, 40000]
}

df = pd.DataFrame(data)
print(df)

plt.bar(df['Month'], df['Units_Sold'])
plt.xlabel('Month')
plt.ylabel('Units Sold')
plt.title('Monthly Units Sold')
plt.show()

plt.plot(df['Month'], df['Revenue'])
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Monthly Revenue Trend')
plt.show()

plt.scatter(df['Units_Sold'], df['Revenue'])
plt.xlabel('Units Sold')
plt.ylabel('Revenue')
plt.title('Units Sold vs Revenue')
plt.show()

input("Press Enter to exit...")
