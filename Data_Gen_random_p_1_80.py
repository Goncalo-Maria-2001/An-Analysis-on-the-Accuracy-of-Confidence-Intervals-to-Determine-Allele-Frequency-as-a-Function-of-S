from scipy.special import comb
import numpy as np
import random


def pmfSamplingDistYiN(M, NN, pi, Pii, yiN):
    """
    M: Total population size
    NN: Sample size
    pi: True frequency of allele A in the population
    Pii: Frequency of homozygotes for the allele A in the population
    yiN: Number of allele A in the sample
    """
    MaxFunc = max((yiN / 2) - (M * pi) + (M * Pii), yiN - NN, 0)
    MinFunc = min(M * Pii, yiN / 2, M - NN + yiN - (2 * M * pi) + (M * Pii))

    LowerBound = int(np.ceil(MaxFunc))
    UpperBound = int(np.floor(MinFunc))

    Numerator1 = 0

    for i in range(LowerBound, UpperBound + 1):
        Summand = (comb(M * Pii, i, exact=True) *
                   comb(2 * M * (pi - Pii), yiN - (2 * i), exact=True) *
                   comb(M + (M * Pii) - (2 * M * pi), NN + i - yiN, exact=True))
        Numerator1 += Summand

    probOut = Numerator1 / comb(M, NN, exact=True)

    return probOut


def AcceptanceRegion(M, NN, pi0, Pii0, yiNobs, alpha):
    SumProb = 0
    yiNlow = 0

    while SumProb <= alpha / 2:
        dummy1 = pmfSamplingDistYiN(M, NN, pi0, Pii0, yiNlow)
        SumProb += dummy1
        yiNlow += 1
    yiNlow -= 1
    SumProb -= pmfSamplingDistYiN(M, NN, pi0, Pii0, yiNlow)

    SumProb2 = 1
    yiNup = 2 * NN
    while SumProb2 >= 1 - (alpha / 2):
        dummy1 = pmfSamplingDistYiN(M, NN, pi0, Pii0, yiNup)
        SumProb2 -= dummy1
        yiNup -= 1
    yiNup += 1
    SumProb2 += pmfSamplingDistYiN(M, NN, pi0, Pii0, yiNup)

    test = yiNlow <= yiNobs <= yiNup

    return {
        'lowerbound': yiNlow,
        'upperbound': yiNup,
        'result': int(test)
    }


def CIforpiCasePiiUnknown(M, NN, yiNobs, alpha):
    pi0List = []
    Pii0List = []
    out = []

    for i in range(2 * M + 1):
        pi0 = i / (2 * M)
        if pi0 >= (yiNobs / (2 * M)) and pi0 <= (1 - ((2 * NN - yiNobs) / (2 * M))):
            for k in range(i + 1):
                Pii0 = k / (2 * M)
                if Pii0 >= max(0, 2 * pi0 - 1) and Pii0 <= pi0:
                    out1 = AcceptanceRegion(M, NN, pi0, Pii0, yiNobs, alpha)
                    if out1['result'] == 1:
                        pi0List.append(pi0)
                        Pii0List.append(Pii0)
                    out2 = list(out1.values()) + [pi0, Pii0]
                    out.append(out2)

    if len(pi0List) > 0:
        piCIlow = min(pi0List)
        piCIup = max(pi0List)
        PiiCIlow = min(Pii0List)
        PiiCIup = max(Pii0List)
    else:
        largestAlpha = [0]
        for outCounter in range(len(out)):
            pi0 = out[outCounter][3]
            Pii0 = out[outCounter][4]
            if yiNobs < out[outCounter][0]:
                Sumprob = 0
                for m in range(yiNobs):
                    Sumprob += pmfSamplingDistYiN(M, NN, pi0, Pii0, m)
                largestAlpha.append(Sumprob * 2)
            if yiNobs > out[outCounter][1]:
                Sumprob2 = 0
                for m in range(2 * NN, yiNobs, -1):
                    Sumprob2 += pmfSamplingDistYiN(M, NN, pi0, Pii0, m)
                largestAlpha.append(Sumprob2 * 2)
        alphaMaxIdx = np.argmax(largestAlpha)
        piCIlow = out[alphaMaxIdx][3]
        piCIup = piCIlow
        PiiCIlow = out[alphaMaxIdx][4]
        PiiCIup = PiiCIlow

    return [piCIlow, piCIup]

p = 1/4
Data_random_p_1_80 = []
for k in range(1,81,1):
    for blhe in range(10):
        print(CIforpiCasePiiUnknown(100, k, int(max(k*(p + random.uniform(-k/10,k/10)),0)), 0.05))
        Data_random_p_1_80.append(CIforpiCasePiiUnknown(100, k, int(max(k*(p + random.uniform(-k/10,k/10)),0)), 0.05))
print(Data_random_p_1_80)