from scipy.stats import binom, norm
import numpy as np
import matplotlib.pyplot as plt

z = norm.ppf(0.995)

num_simulations = 500

sample_sizes = np.arange(1, 81)
mean_moes_p_deviation = []


def compute_confidence_interval(n, phat, z):
    se = np.sqrt(phat * (1 - phat) / n)
    moe = z * se
    ci = (phat - moe, phat + moe)
    return ci, moe


for n in sample_sizes:
    moes = []

    for _ in range(num_simulations):
        p = 1/4 + random.uniform(-(1/40), (1/40))

        sample_count = binom.rvs(n, p, size=1)
        phat = sample_count[0] / n

        _, moe = compute_confidence_interval(n, phat, z)
        moes.append(moe)

    mean_moes_p_deviation.append(np.mean(moes))

x = np.arange(1,81,1)
fit = np.polyfit(np.log(x),mean_moes_p_deviation, 1)
print(fit)
y_predicted = []
for i in range(1, 81):
    y_predicted.append(fit[1] + np.log(i) * fit[0])

plt.yticks([0.05,0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90,
            0.95, 1.00])
plt.plot(sample_sizes, mean_moes_p_deviation, marker='o', linestyle='-', color='blue')
plt.plot(x, y_predicted, color='c')
plt.xlabel('Sample Size (n)')
plt.ylabel('Average Margin of Error')
plt.title('Average Margin of Error for Random Proportion CI Using Normal Approximation')
plt.grid(True)
plt.show()
