---
title: 'Non-Markovian random walks'
date: 2018-10-18
permalink: /posts/2018/10/non-markov
tags:
  - excursion set theory
  - stochastic processes
---

A brief review of random walks in cosmology and generating non-Markovian random walks based on Cholesky decomposition. This review is based on one of my papers originally published as: <i>The Excursion set approach: Stratonovich approximation and Cholesky decomposition</i> (Nikakhtar et al. MNRAS 478 (4), 5296–5300)

# Cosmological motivation:
Non-linear structure formation is an important arena in modern cosmology where fundamental questions about the essence of dark energy, dark matter and the physics of the early universe, as well as outstanding questions in galaxy formation and evolution, are addressed. Many planned satellite- and ground-based projects (e.g. Euclid, LSST) will use the abundance and clustering of non-linear structures to address these questions.

In a seminal paper, Press and Schechter (1974) argued that it should be possible to estimate this late-time abundance from knowledge of the initial fluctuation field. They did so by combining the spherical collapse model of Gunn & Gott (1972) with the assumption that the initial fluctuation field was Gaussian. The Excursion Set approach of Bond et al. (1991) casts the Press-Schechter argument in terms of a random walk, barrier crossing problem. In this approach, one associates a random walk with each position in the initial field: the walk height represents the smoothed initial overdensity field at that position, and the number of steps is related to the smoothing scale. The height of the barrier to be crossed is determined by the collapse model, so the first up-crossing distribution is related to the abundance of nonlinear objects. To compute the non-Markovian (the most general case) first up-crossing distribution, we must generate trajectories with the correct ensemble properties. Here, we describe how to do so efficiently.

# Cholesky decomposition method:
Here, we will use $\delta_R(\bf{x})$ to denote the linearly evolved overdensity at position $\bf{x}$ smoothed on scale $R$. In the $\Lambda$CDM model, $S \equiv \langle \delta_R^2 \rangle$ is a monotonic function of the smoothing scale $R$ and in the excursion set formalism, it is usual to work with $S$ rather than $R$. The value of the smoothed density contrast $\delta_S$, when plotted as a function of $S$, traces out a trajectory which resembles the evolution of a stochastic process. There is a different trajectory associated with each position $\bf{x}$ in the Universe. The properties of the ensemble defined by choosing a random set of positions $\bf{x}$ will depend on the correlations of the underlying field, and on the nature of the smoothing filter. To see this explicitly, note that the correlation between heights on two scales is given by

$$ C_{ij} \equiv \langle \delta_i \delta_j \rangle = \int \frac{dk}{k} \frac{k^3P(k)}{2\pi^2} \tilde{W}(kR_i) \tilde{W}(kR_j),$$

where $P(k)$ is the power spectrum, $\tilde{W}$ is the Fourier transform of the window function, and $C_{ii} \equiv S_i$ is the variance of $\delta$ when smoothed on scale $R_i$.