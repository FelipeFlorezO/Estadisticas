import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')
tips.head()

tips.corr()
sns.heatmap(tips.corr())
