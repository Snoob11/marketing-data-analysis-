# anova 
import pandas as pd
from numpy import repeat
from pingouin import anova, rm_anova, mixed_anova, print_table

# Load dataset
df = pd.read_csv('C:/Users/socie/OneDrive/Documents/thesis 1 and 2/thesis 2/data/data qualitative.csv',sep = ';')


# ONE-WAY ANOVA
aov = anova(dv='12', between=['Frame'], data=df, detailed=False)
print_table(aov, floatfmt=".3f")
