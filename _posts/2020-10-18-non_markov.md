---
title: 'Non-Markovian random walks'
date: 2020-10-18
permalink: /posts/2018/10/non-markov
tags:
  - stochastic processes
  - excursion set theory
---

A brief review of random walks in cosmology and generating non-Markovian random walks based on Cholesky decomposition. This review is based on one of my papers originally published as: <i>The Excursion set approach: Stratonovich approximation and Cholesky decomposition</i> (Nikakhtar et al. MNRAS 478 (4), 5296–5300)

### Cosmological motivation:
Non-linear structure formation is an important arena in modern cosmology where fundamental questions about the essence of dark energy, dark matter and the physics of the early universe, as well as outstanding questions in galaxy formation and evolution, are addressed. Many planned satellite- and ground-based projects (e.g. Euclid, LSST) will use the abundance and clustering of non-linear structures to address these questions.

In a seminal paper, Press and Schechter (1974) argued that it should be possible to estimate this late-time abundance from knowledge of the initial fluctuation field. They did so by combining the spherical collapse model of Gunn & Gott (1972) with the assumption that the initial fluctuation field was Gaussian. The Excursion Set approach of Bond et al. (1991) casts the Press-Schechter argument in terms of a random walk, barrier crossing problem. In this approach, one associates a random walk with each position in the initial field: the walk height represents the smoothed initial overdensity field at that position, and the number of steps is related to the smoothing scale. The height of the barrier to be crossed is determined by the collapse model, so the first up-crossing distribution is related to the abundance of nonlinear objects. To compute the non-Markovian (the most general case) first up-crossing distribution, we must generate trajectories with the correct ensemble properties. Here, we describe how to do so efficiently.

### Cholesky decomposition method:
Here, we will use $\delta_R(\textbf{x})$ to denote the linearly evolved overdensity at position $\textbf{x}$ smoothed on scale $R$. In the $\Lambda$CDM model, $S \equiv \langle \delta_R^2 \rangle$ is a monotonic function of the smoothing scale $R$ and in the excursion set formalism, it is usual to work with $S$ rather than $R$. The value of the smoothed density contrast $\delta_S$, when plotted as a function of $S$, traces out a trajectory which resembles the evolution of a stochastic process. There is a different trajectory associated with each position $\textbf{x}$ in the Universe. The properties of the ensemble defined by choosing a random set of positions $\textbf{x}$ will depend on the correlations of the underlying field, and on the nature of the smoothing filter. To see this explicitly, note that the correlation between heights on two scales is given by

$$ C_{ij} \equiv \langle \delta_i \delta_j \rangle = \int \frac{dk}{k} \frac{k^3P(k)}{2\pi^2} \tilde{W}(kR_i) \tilde{W}(kR_j),$$

where $P(k)$ is the power spectrum, $\tilde{W}$ is the Fourier transform of the window function, and $C_{ii} \equiv S_i$ is the variance of $\delta$ when smoothed on scale $R_i$. If the joint distribution of walk heights on all steps is multivariate Gaussian, then all the information about correlations is encoded in the quadratic form $\sum_{ij} \delta_i C_{ij}^{-1} \delta_j$. In practice, how should one use this quadratic form?  The Cholesky method which we describe here, can be thought of as writing

$$ \delta_n = \langle \delta_n| \delta_{n-1}, \ldots, \delta_1 \rangle + \sigma_{n|n-1,\ldots,1} \xi_n. $$

For Gaussian statistics, $\xi_n$ is a zero-mean unit variance Gaussian random number, the first term on the right-hand side is a linear function of the previous heights $(\delta_1, \ldots, \delta_{n-1})$, and the second term depends on the scales $S_1,\ldots,S_n$, but not on the heights themselves. This results in a substantial speed-up because each $\delta_n$ is only determined by steps previous to it.  Note that, other than ensuring that up crossing scales be well resolved, there is no requirement that steps be evenly spaced in $S$. The matrix $C$ is real, symmetric, and positive-definite, so it has a unique decomposition, $C = LL^T$, in which $L$ is a lower triangular matrix.  This decomposition is known as Cholesky's decomposition. We use $L$ to generate the ensemble of trajectories as follows.

First, consider a vector $\textbf{\xi}$, which is Gaussian white noise with zero mean and unit variance (i.e. $\langle \xi_m \xi_n \rangle = \delta_{mn}$). If we generate our desired trajectories as

$$ \delta_i = \sum_{j} L_{ij} \xi_j, $$

then the $\delta_i$ will have correlations between heights given by

$$ \langle \delta_i \delta_j \rangle = \sum_{n,m} L_{im} L_{jn} \langle \xi_m \xi_n \rangle = LL^T = C. $$

Since $L$ is triangular, each $\delta_i$ really only requires a sum over $j \le i$, so this method is fast. The matrix $L$ is given by

$$
\begin{equation}
L = \begin{pmatrix}
		1 & 0 & 0 & \cdots & 0 \\
		c_{12} & \sqrt{1 - c_{12}^2} & 0 & \cdots & 0 \\
		c_{13} & \frac{c_{23} - c_{12}c_{13}}{\sqrt{1 - c_{12}^2}} & \sqrt{1 - c_3 R_2^{-1} c_3^T} & \cdots & 0 \\
		\vdots & \vdots & \vdots & \ddots & \vdots \\
		c_{1n} & \frac{c_{2n} - c_{12}c_{1n}}{\sqrt{1-c_{12}^2}} & \frac{c_{3n} - c_3^{*n} R_2^{-1} c_3^T }{\sqrt{1 - c_3 R_2^{-1} c_3^T}} &\cdots & \sqrt{1 - c_n R_{n-1}^{-1} c_n^T}
	\end{pmatrix},
\end{equation} 
$$

sd