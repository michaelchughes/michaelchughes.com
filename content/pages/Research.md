Title: Research Projects
Date: 2023-10-12
save_as: research.html

### Active Research Projects

The Hughes Lab at Tufts pursues research on machine learning methodology across several synergistic themes 

**1) Probabilistic models fit via efficient algorithms**

> Practitioners often wish for probabilistic models to help them manage uncertainty, yet also need algorithms that train these models on large datasets quickly and reliably. My lab is working on several ways to fit models that balance flexibility and efficiency. In one line of work (<a href="https://proceedings.mlr.press/v162/wojnowicz22a.html">Wojnowicz et al. ICML '22</a>, <a href="https://openreview.net/forum?id=wSZrMV2akW">Wojnowicz et al. AABI '23</a>), we consider using simpler surrogate models amenable to fast closed-form coordinate ascent variational methods during training, then at deployment plugging in the estimated model parameters (or estimated posterior distributions) into a more flexible model that would be hard to fit directly. We provide a formal statistical justification for this practice, in terms of bounds on likelihoods. In other work (Cheng et al. NeurIPS '21, Cheng et al. IEEE TSP '23), we've developed time series models that use tools from optimal transport that better account for gradual transitions between distinct behaviors (e.g. walking vs. running).

> Recent preliminary work includes efforts to handle missingness in irregular time series, especially when the mechanisms that give rise to missingness are complex (known as 'missing-not-at-random'). We are also developing models and efficient inference for discovering the group dynamics for collections of time series, such as the movements over time of many players on a basketball team.


**2) Learning from limited available labeled data, especially semi-supervised learning and self-supervised learning.**

> Modern deep learning of image classifiers requires large labeled training sets. Yet in many applications, especially in medicine, labels are difficult to acquire. The field of semi-supervised learning, which designs methods that can learn from small labeled data and large unlabeled data jointly, offers promise but does not work well on realistic unlabeled sets, which are collected for expediency and may contain extra label categories unlike the curated labeled set. My lab is working on several methods that can more effectively learn from limited available labeled data in the real world. First, our work on Fix-A-Step (Huang et al. AISTATS '23) shows how many modern semi-supervised methods can be repaired to work effectively on realistic unlabeled sets via a principled modification of the parameter update step in gradient descent. Second, other work (Huang et al. MLHC '21, Huang et al. MLHC '23) addresses the problem of *multiple instance learning* from limited labeled data.

> Recent preliminary work (Huang et al. arXiv '23) provides a much-needed comprehensive benchmark of methods from diverse fields (semi- and self-supervised learning) on realistic medical image classification problems. We've also recently developed a principled approach to self-supervised noise-contrasive estimation when there are available supervised labels (Feeney et al. arXiv '23).

**3) Training objectives designed to improve downstream decisions.**

> As supervised ML methods are increasingly deployed in high-stakes applications, almost all implementations continue to train using objectives like cross entropy or squared error chosen more for mathematical convenience than alignment with how the model will be used later on by stakeholders. My lab is working on several efforts to design new training objectives that yield better predictions and decisions while remaining tractable to train via modern gradient descent. Examples include work on avoiding excessive false alarms by enforcing a minimum precision constraint (Rath et al. AISTATS '22) as well as work on "prediction-constrained" training (Hughes et al. AISTATS '18, Futoma et al. AISTATS '20, Hope et al. TS workshop '21) that adds effective supervision to classic latent variable models like topic models, hidden Markov models, and partially-observable Markov decision processes (POMDPs).

> Recent preliminary work pursues how such training objectives can be translated to improve prediction of outcomes for hospitalized patients (Rath et al. IMLH '23) or improve using spatiotemporal forecasting models to decide where to intervene to counter-act the opioid epidemic (Heuton et al. IMLH '23).

Beyond these methods contributions, our work strives for reproducibility and open science. Every paper provides an associated link to code, usually on page one. We've also developed open datasets for ultrasound images of the heart (<a href="https://tmed.cs.tufts.edu/papers/HuangEtAl_MLHC_2021.pdf">Huang et al. MLHC '21>), fNIRS brain signals over time (<a href="https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/hash/bd686fd640be98efaae0091fa301e613-Abstract-round2.html">Huang et al. NeurIPS D&B '21</a>), and novelty detection in open worlds (<a href="https://openreview.net/pdf?id=4eL6z9ziw7">Feeney et al. TMLR '23</a>).


### Past Projects

My Ph.D. thesis work was motivated by several applied questions:

* can we find clusters of cooccuring words that thematically organize every New York Times article from the last 20 years?
* can we find clusters of cooccuring epigenetic modifiers that amplify or inhibit gene expression?

To answer these questions, we developed new variational inference 
algorithms for a broad family of Bayesian nonparametric models that include mixtures, topic models, sequential models, and relational models.
Our key innovations include scaling to millions of examples and adding data-driven split/merge proposal moves to avoid poor local minima.

Please try out 
<a href="https://github.com/bnpy/bnpy/">
<strong>BNPy</strong></a>, our open-source Python package.
