df = pd.read_csv(r"D:\User Files\Excel\csv\diabetes.csv")

'''
The fig variable represents the Figure object, which is the top-level 
container for all plot elements (subplots, titles, etc.).
It allows you to control figure-level properties, such as saving the figure or setting its title.

axs variable is a numpy array containing each individual object
each represents a subplot which can be used later
'''

fig,axs = plt.subplots(9,1,figsize = (5,20))
i = 0
for col in df.columns:
    axs[i].boxplot(df[col], vert=False)
    axs[i].set_ylabel(col)
    i+=1
plt.show()

'''
