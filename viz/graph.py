import pandas as pd
import matplotlib.pyplot as plt
import io

# 1. Data is stored in a multi-line string in CSV format.
csv_data = """module,mean,stdev,ci95
bench.original,0.4465728155837496,0.017311768157518063,0.009795054925773617
bench.sourcery,0.00882640049985639,0.002336846309711533,0.0013221952690474024
bench.tabnine,0.2859903260835684,0.011269706852021511,0.006376436919008734
bench.local_llm,0.9852917379994324,0.025898277698151295,0.014653330048563826
"""

# 2. Use pandas and io.StringIO to read the string data into a DataFrame.
df = pd.read_csv(io.StringIO(csv_data))

# 3. Clean up the module names for better labels on the graph.
# This removes "bench.", replaces underscores with spaces, and capitalizes the words.
df['module'] = df['module'].str.replace('bench.', '').str.replace('_', ' ').str.title()

# 4. Sort the DataFrame by the 'mean' column to display the bars in a logical order.
df = df.sort_values('mean', ascending=False)

# 5. Set up and create the plot.
plt.figure(figsize=(10, 6)) # Define the figure size for better readability.
bars = plt.bar(
    df['module'],
    df['mean'],
    yerr=df['ci95'],      # Use the 95% confidence interval for error bars.
    capsize=5,            # Add caps to the error bars.
    color=['#ff6347', '#4682b4', '#32cd32', '#ffd700'] # Assign colors to bars.
)

# 6. Add labels, a title, and a grid to make the chart easier to read.
plt.ylabel('Mean Execution Time (seconds)')
plt.title('Performance Benchmark of AI Coding Assistants')
plt.xticks(rotation=0) # Keep the x-axis labels horizontal.
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 7. Loop through each bar to add its mean value as a text label on top.
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.3f}', va='bottom', ha='center')

# 8. Adjust layout to prevent labels from being cut off.
plt.tight_layout()

# 9. Save the generated graph to a file.
plt.savefig('benchmark_graph.png')

print("Graph has been saved as benchmark_graph.png")