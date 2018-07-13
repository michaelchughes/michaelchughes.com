Title: Research Projects
Date: 2018-04-01
save_as: research.html

### Active Research Projects

Recently, I'm motivated by two exciting clinical applications:

* antidepressant recommendations for patients with major depression
* forecasting need for interventions in the Intensive Care Unit (ICU)

These applications have inspired new contributions to machine learning:

* **Semi-supervised learning**: Our new 
<a href="https://arxiv.org/pdf/1707.07341.pdf">
*Prediction Constrained*
</a>
training objective fits latent variable models so that they provide accurate predictions (e.g. drug recommendations) *and* interpretable generative models, even when labeled examples are rare.

* **Explainable AI**: Our new 
<a href="https://arxiv.org/pdf/1711.06178.pdf">
*Tree Regularization*
</a>
method lets you optimize deep neural networks so learned class boundaries are similar to decision trees.

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
