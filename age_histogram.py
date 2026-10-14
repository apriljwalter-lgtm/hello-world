#Load the sample dataset
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'age': np.random.randint(18, 90, size=100),  # Random ages between 18 and 89
    'hospital_mortality': np.random.choice([0, 1], size=100)  # Random binary values (0 or 1)
})

df

#Create the histogram with 5 bins
plt.hist(df[df['hospital_mortality'] == 1]['age'], bins=5)
#Set the figure title
plt.title('Age of Non-Surviving Patients')
#Set the x-axis label
plt.xlabel('Age')
#Set the y-axis label
plt.ylabel('Count')
#Save the figure as a PDF
plt.savefig('age_histogram.pdf')
#Display the figure
plt.show()
