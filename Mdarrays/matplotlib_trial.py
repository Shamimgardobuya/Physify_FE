a = np.arange(0,11)
b = a * 2
axes = fig.add_axes([0,0,0.7,0.8])
axes.set_xlabel('Days')
axes.set_ylabel('Infection Rates')
axes.set_title('Infection Rates Over Time')

axes.plot(x,y, label = "Bacteria")
axes.plot(a,b, label = "Virus")
axes.legend()