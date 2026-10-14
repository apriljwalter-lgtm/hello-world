import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'age': np.random.randint(18, 90, size=100),  # Random ages between 18 and 89
    'hospital_mortality': np.random.choice([0, 1], size=100)  # Random binary values (0 or 1)
})

df

plt.hist(df[df['hospital_mortality'] == 1]['age'], bins=5)
plt.title('Age of Non-Surviving Patients')
plt.xlabel('Age')
plt.ylabel('Count')
plt.savefig('age_histogram.pdf')
plt.show()
