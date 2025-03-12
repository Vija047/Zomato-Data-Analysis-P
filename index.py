import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  

# Load the dataset
df = pd.read_csv("./Zomato data .csv")

# Display initial info
print(df.head())
print(df.info())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Fill missing values with "unknown"
df.fillna("unknown", inplace=True)

# Function to handle rate conversion
def handleRate(value):
    try:
        value = str(value).split('/')  # Split on '/'
        return float(value[0])  # Convert first part to float
    except ValueError:
        return np.nan  # If conversion fails, return NaN

# Apply function to the 'rate' column
if 'rate' in df.columns:
    df['rate'] = df['rate'].apply(handleRate)
else:
    print("Column 'rate' not found in the dataset!")

# Display modified DataFrame
print(df.head())

# Print final DataFrame structure
print(df.info())
y = df["online_order"].value_counts()

# Plot the data
# plt.pie(y ,height=22 ,color='red')  
# plt.xlabel("Online Order Options")  # Label for x-axis
# plt.ylabel("Count")  # Label for y-axis

# ) Which mode (online or offline) has received the maximum rating?
# order_counts = df["online_order"].value_counts()

# plt.figure(figsize=(6,6))  # Set figure size
# plt.pie(order_counts, labels=order_counts.index, autopct="%1.1f%%", startangle=90, colors=["lightblue", "lightcoral"])
# plt.title("Online Order Availability") 

x = df["name"][:10]  # Take the first 10 restaurant names
y = df["rate"][:10]  # Take the first 10 ratings

# Create bar chart
plt.figure(figsize=(10,5))  # Set figure size
plt.bar(x, y, color="skyblue")  # Bar chart with colors

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Add labels and title
plt.xlabel("Restaurant Name")
plt.ylabel("Rating")
plt.title("Restaurant Ratings")

 # Title of the plot
plt.show()