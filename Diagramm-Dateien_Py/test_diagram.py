import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 8))

plt.title("Ausgaben in den Monaten")

x = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
y = [5, 8, 3, 4, 5, 6, 7, 8, 9, 10, 12, 1]

plt.xlabel('Monate')
plt.ylabel('Ausgaben (€)')

# Plot the original data
plt.plot(x, y, label='Tatsächliche Ausgaben')
plt.scatter(x, y, color='red')

# Calculate trendline
x_numeric = np.arange(len(x))
z = np.polyfit(x_numeric, y, 1)
p = np.poly1d(z)

# Plot the trendline
plt.plot(x, p(x_numeric), "r--", label='Trendlinie')

plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()