import matplotlib.pyplot as plt
import numpy as np
import scipy, pylab
from scipy import stats

mu = (0, 3.2)
sigma = (1, 1.5)
alpha = 0.05

x = np.linspace(-4, 9, 2000)
y1 = scipy.stats.norm.pdf(x, loc=mu[0], scale=sigma[0])
y2 = scipy.stats.norm.pdf(x, loc=mu[1], scale=sigma[1])

critical_point = scipy.stats.norm.ppf(1 - alpha, loc=mu[0], scale=sigma[0])
critical_point0 = 2*x[np.nanargmax(y1)]-critical_point
critical_point2 = 2*x[np.nanargmax(y2)]-critical_point

#plotting
plt.plot(x, y1, x, y2,  color='grey', alpha = 0.2)
plt.fill_between(x, y1, y2, facecolor='grey', alpha=0.2)
plt.fill_between(x, y2, where=np.logical_or(critical_point >= x, x > critical_point2), facecolor='orange')
plt.fill_between(x, y1, where=np.logical_or(critical_point <= x, x < critical_point0), facecolor='yellow')
plt.ylabel('Probability density function')
plt.xlabel('x')
plt.text(critical_point -1, max(y1) - .05, 'Null hypothesis H0\n $\sigma = {},  \mu = {}$'.format(sigma[0], mu[0]), style="italic", color = 'grey')
plt.text(critical_point2 - .5, max(y2) - .05, 'Alternative hypothesis H1\n  $\sigma = {},  \mu = {}$'.format(sigma[1], mu[1]), style="italic", color = 'grey')
pylab.annotate ('Type II Error',
                    xy=(critical_point -1, 0.02),
                    xytext = (critical_point + 1, 0.02+ 0.06),
                    arrowprops = {'facecolor': 'black', 'width': 0.01, 'headwidth' : 4})
pylab.annotate (' ',
                xy=(critical_point2 +1, 0.02),
                xytext = (critical_point2 -1, 0.02+ 0.06),
                arrowprops = {'facecolor': 'black', 'width': 0.01, 'headwidth' : 4})
pylab.annotate ('Type I Error',
                    xy=(critical_point0-0.4, 0.02),
                    xytext = (critical_point0 + 1.1, 0.02+ 0.15),
                    arrowprops = {'facecolor': 'black', 'width': 0.01, 'headwidth' : 4})
pylab.annotate (' ',
                    xy=(critical_point+0.4, 0.02),
                    xytext = (critical_point - 1.1, 0.02+ 0.15),
                    arrowprops = {'facecolor': 'black', 'width': 0.01, 'headwidth' : 4})

plt.show()


'''
popmean = mu[0]
onesample_results = scipy.stats.ttest_1samp(y1, popmean)
p_value = onesample_results[1]
'''