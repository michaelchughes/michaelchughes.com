Title: Machine Learning for Clinicians: Advances for Multi-Modal Health Data
Date: 2018-08-01
save_as: mlhc2018_tutorial.html

## A Tutorial at <a href="https://www.mlforhc.org/">MLHC 2018</a>

##### Thursday August 16, 2018, 13:30-16:30

##### Li Ka Shing Learning and Knowledge Center, Room LK120, Stanford University


<ul class="list-group">
  <li class="list-group-item">
    <p class="list-group-item-text">
      Quick Links:&nbsp;&nbsp;
      <a href="talks/MLHC2018Tutorial_MLforClinicians_Overview.pdf">
      [Overview Slides PDF]
      </a>
        &#8226;
      <a href="talks/MLHC2018Tutorial_MLforClinicians_Part1.pdf">
      [Part 1 Slides PDF]
      </a>
        &#8226;
      <a href="talks/MLHC2018Tutorial_MLforClinicians_Part2.pdf">
      [Part 2 Slides PDF]
      </a>
        &#8226;
      <a href="talks/MLHC2018Tutorial_MLforClinicians_Part3.pdf">
      [Part 3 Slides PDF]
      </a>
        &#8226;
      <a href="talks/mlhc2018_tutorial_references.pdf">
      [Bibliography PDF]
      </a>
    </p> 
  </li>
</ul>

<!--
# Survey

<ul class="list-group">
    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            <a href="https://goo.gl/forms/lSG1t8t63BPOxkdo2">
            ML that Matters Survey (Google Forms)
            </a>
        </h4>
        <p>
If you are a clinician, please take this short survey to help us understand the clinical problems that matter to you!
        </p>
    </li>
</ul>
-->

# Goals

This tutorial is intended for clinicians and other healthcare professionals who wish to become familiar with recent advances in machine learning and how these might be applied to medical applications. Within machine learning, we will focus mostly on supervised methods for making predictions, starting at basic predictors from static, vector-valued data and building up to multi-modal, time-varying signals. One motivating example will be the combination of demographics, vital sign data, diagnosis or procedural code data, text data, and image data available in an in-patient hospital setting. 

The tutorial has 3 parts. The first part will provide a common foundation of common methods used training basic single-data-source predictors (e.g. predict length of stay from patient vital signs) as well as best practices for evaluating these predictors. The second part will cover methods for learning rich representations that can handle *structured* data such as time series, text, and images. The final part will cover recent methods that address 6 key methodological challenges arising from healthcare applications, such as
missing data,
methods for combining labeled and unlabeled data (semi-supervised learning),
methods for learning from multiple data sources (multimodal learning),
explainable/interpretable models,
models that try to account for causality,
and sequential decision-making (reinforcement learning).

Throughout each part, we hope to provide a practical tour of major methodological approaches, give examples of cutting-edge applications to the healthcare domain, and cut through the hype to identify key limitations and remaining open problems.

We hope to give you tools to navigate successful collaborations with machine learning researchers, as well as the ability to critically evaluate claims about machine learning methods in the literature. We hope that after completing this tutorial, you could be a more competent reviewer for the computational side of a submitted MLHC paper.


# Target Audience

This is targeted at clinicians and other healthcare professionals who might have limited exposure to machine learning methods in the past. This is probably right for you if you have some basic understanding of methods linear regression/logistic regression or decision trees, but wish to know more about how the latest methodological advances in machine learning might be applied to healthcare problems.

This tutorial is not necessarily designed for professional data scientists or machine learning researchers, though you are welcome to attend.


# Content

## 01:30-01:45 Overview (15 min) <a href="{static}/talks/MLHC2018Tutorial_MLforClinicians_Overview.pdf">[slides PDF]</a>

* Tutorial Goals
* Success Stories: ML for Sepsis Prediction
* Context: ML as a piece of a much larger puzzle

## 01:45-02:20 Part 1: Making Predictions (45 min) <a href="{static}/talks/MLHC2018Tutorial_MLforClinicians_Part1.pdf">[slides PDF]</a>


* Evaluation of Predictions
* * Train/Valid/Test
* * Performance Metrics
* * * TPR, FPR, AUC, etc.
* * Calibration
* * Decision-Theory and Utility

* Basic Methods for Regression and Classification
* * Linear models
* * Decision trees and Random Forests
* * Simple Neural Nets

* Predictions with Uncertainty
* * Gaussian Processes


## 02:20-02:30 <<< Questions + Break >>>
## 02:30-03:15 Part 2: Learning Representations (45 min) <a href="{static}/talks/MLHC2018Tutorial_MLforClinicians_Part2.pdf">[slides PDF]</a>

* Representations using Bag-of-Words
* * Topic Models

* Learned Representations for Images
* * Convolutional Networks

* Learned Representations for Time Series
* * RNNs

* Learned Representations for Text
* * RNNs
* * Embeddings

* Tricks of the Trade
* * Dropout, Data Augmentation, etc.

* Models that Generate Data
* * Autoencoders (AEs) & Denoising AEs
* * Deep Generative Models
* * Variational Autoencoders (VAEs)
* * GANs

## 03:15-03:30 <<< Questions + Break >>>
## 03:30-04:30 Part 3: Addressing Health Data Challenges <a href="{static}/talks/MLHC2018Tutorial_MLforClinicians_Part3.pdf">[slides PDF]</a>

We consider 6 key challenges for ML that arise from health applications. We will summarize

* Missing data
* * Imputation strategies that work
* * Modeling strategies that work
* Incomplete/partial labels (Semi-supervised learning)
* * Two stage strategies
* * End-to-end strategies
* Multi-modal data
* * Learning joint/shared representations
* * Learning coordinated representations
* Interpretability
* * Methods designed to be inspected (SLIM)
* * Methods to explain a fixed, pre-trained predictor
* * Methods to optimize predictors to be more interpretable
* Causality
* * Potential Outcomes framework for Counterfactuals
* * Examples on health data
* Sequential Decision Making / Reinforcement Learning
* * Recent Successes from "deep" RL
* * Limitations for Health Applications
* * Evaluation Methods on Observational data


# Resources


## Bibliography

<ul class="list-group">
    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            <a href="talks/mlhc2018_tutorial_references.pdf">
            ML for Clinicians References (PDF)
            </a>
        </h4>
        <p>
            Companion bibliography for this tutorial. Contains all cited references following the tutorial outline.
        </p>
    </li>
</ul>

## Related Tutorials

<ul class="list-group">

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at KDD 2018:
            <a href="http://dl4health.org/">
            Deep Learning For Computational Healthcare
            </a>
        </h4>
        <p>
            Presenters:
            Cao Xiao &#8226; Edward Choi  &#8226; Jimeng Sun (Georgia Tech)
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at KDD 2018:
            <a href="https://mlhealthcare.github.io/">
            Explainable Models for Healthcare AI
            </a>
        </h4>
        <p>
            Presenters:
            Muhammad Aurangzeb Ahmad &#8226;
            Dr. Carly Eckert M.D &#8226;
            Ankur Teredesai &#8226;
            Vikas Kumar
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at KDD 2018:
            <a href="http://www.kmd.ovgu.de/KMD+Events/Data+Science+for+Health.html">
 Knowledge Discovery from Cohorts, Electronic Health Records and further Patient-related data
            </a>
        </h4>
        <p>
            Presenters:
            Panagiotis Papapetrou (Stockholm) and Myra Spiliopoulou (Magdeburg)
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at ICML 2018:
            <a href="https://mlhealthtutorial.com/">
Machine Learning for Personalised Health
            </a>
        </h4>
        <p>
            Presenters: Lamiae Azizi (U. Sydney), Konstantina Palla (Microsoft Research), Danielle Belgrave (Microsoft Research, Imperial College London Dept. of Medicine)
        </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at ICML 2017:
            <a href="https://sites.google.com/view/icml2017-deep-health-tutorial/home/">
Deep Learning Models for Health Care - Challenges and Solutions
            </a>
        </h4>
        <p>
            Presenters: Yan Liu (USC) and Jimeng Sun (Georgia Tech)
        </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at UAI 2017:
            <a href="http://www.auai.org/uai2017/media/tutorials/suchi.pdf">
Machine Learning and Counterfactual
Reasoning for "Personalized" DecisionMaking
in Healthcare
            </a>
        </h4>
        <p>
            Presenters: 
            Suchi Saria and Hossein Soleimani (Johns Hopkins)
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            Tutorial at NIPS 2016:
            <a href="https://nips.cc/Conferences/2016/Schedule?showEvent=6204">
ML Foundations and Methods for Precision Medicine and Healthcare
            </a>
        </h4>
        <p>
            Presenters: 
            Suchi Saria and Peter Schulam (Johns Hopkins)
        </p>
    </li>



</ul>

## Related Conferences and Workshops

<ul class="list-group">
    <li class="list-group-item">
        <h4 class="list-group-item-heading">
            <a href="https://mlmhworkshop.github.io/mlmh-2018/">
            KDD 2018 Workshop on Machine Learning for Medicine and Healthcare
            </a>
        </h4>
        <p> Very recent workshop (Aug. 2018)
        </p>
    </li>
</ul>



