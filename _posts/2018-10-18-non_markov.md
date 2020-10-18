---
title: 'Non-Markovian random walks'
date: 2018-10-18
permalink: /posts/2018/10/non-markov
tags:
  - excursion set theory
  - stochastic processes
---

A brief review of random walks in cosmology and generating non-Markovian random walks based on Cholesky decomposition. This review is based on one of my papers originally published as: The Excursion set approach: Stratonovich approximation and Cholesky decomposition
Nikakhtar et al. MNRAS 478 (4), 5296–5300 (2018), [arXiv](https://arxiv.org/abs/1802.04207)

# Cosmological motivation:
Non-linear structure formation is an important arena in modern cosmology where fundamental questions about the essence of dark energy, dark matter and the physics of the early universe, as well as outstanding questions in galaxy formation and evolution, are addressed. Many planned satellite- and ground-based projects (e.g. Euclid, LSST) will use the abundance and clustering of non-linear structures to address these questions.

In a seminal paper, Press and Schechter (1974) argued that it should be possible to estimate this late-time abundance from knowledge of the initial fluctuation field. They did so by combining the spherical collapse model of Gunn & Gott (1972) with the assumption that the initial fluctuation field was Gaussian. The Excursion Set approach of Bond et al. (1991) casts the Press-Schechter argument in terms of a random walk, barrier crossing problem. In this approach, one associates a random walk with each position in the initial field: the walk height represents the smoothed initial overdensity field at that position, and the number of steps is related to the smoothing scale. The height of the barrier to be crossed is determined by the collapse model, so the first up-crossing distribution is related to the abundance of nonlinear objects. To compute the non-Markovian (the most general case) first up-crossing distribution, we must generate trajectories with the correct ensemble properties. Here, we describe how to do so efficiently.

# Cholesky decomposition method:
