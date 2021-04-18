Title: Mike Hughes - Machine Learning Research
Date: 2018-07-01
save_as: index.html

Welcome! My research spans statistical machine learning and its applications in healthcare and the sciences.

I am an Assistant Professor in the Dept. of Computer Science at Tufts University and a primary faculty member for the 
[Tufts Machine Learning research group](https://www.cs.tufts.edu/research/ml/).
Previously, I was a postdoctoral fellow in computer science at Harvard SEAS, advised by 
<a href="https://finale.seas.harvard.edu/">Prof. Finale Doshi-Velez</a>. 
I did my Ph.D. in CS at Brown University in May 2016, advised by <a href="https://www.ics.uci.edu/~sudderth/">Prof. Erik Sudderth</a> (now at UC-Irvine).

### Research Highlights

My lab pursues advances to core machine learning methods as well as high-impact applications.

First, I'm interested in fundamental problems in statistical machine learning:

* probabilistic models for multivariate time-series with irregular or missing data
* scalable inference for latent variable models (see our [AABI 2019 paper]({static}/papers/ZhangHughes_AABI_2019.pdf))
* effective semi-supervised learning with latent variable models (see our [AISTATS 2018 paper]({static}/papers/HughesEtAl_AISTATS_2018.pdf))
* Bayesian nonparametric approaches to growing model complexity as data demands (see our [BNPy Python package](https://github.com/bnpy/bnpy) and [NeurIPS 2015 paper]({static}/papers/HughesStephensonSudderth_NIPS_2015.pdf))
* model-based reinforcement learning with open-world, partially-observable state (see our [AISTATS 2020 paper]({static}/papers/FutomaHughesDoshiVelez_AISTATS_2020.pdf))
* optimizing deep learning models to be more interpretable (see our [AAAI 2020]({static}/papers/WuParbhooHughesEtAl_AAAI_2020.pdf) and [AAAI 2018](https://arxiv.org/pdf/1711.06178.pdf) papers)

Second, I'm interested in several exciting clinical applications of these techniques:

* antidepressant drug recommendations for patients with major depression
* forecasting deterioration and need for interventions in the Intensive Care Unit (ICU)
* forecasting chemotherapy risks for acute myeloid leukemia patients

For more, see my [Research page]({static}/research.html)


### News

<ul class="list-group">

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Apr 2021] New work on probabilistic models for COVID-19 forecasting, with collaborators from Tufts Medical Center
        </h4>
        <ul>
            <li>
                Preprint on a new <a href="{static}/papers/VisaniEtAl_arXiv_2021.pdf"> ACED-HMM model for COVID-19 hospitalized patient trajectories </a>, led by first author Gian Marco Visani (Tufts CS undergrad '21)
            </li>
            <li> Workshop paper on <a href="{static}/papers/LeeEtAl_ICLRWorkshopMLPreventingCombatingPandemics_2021.pdf"> COVID-19 patient count forecasting at a single hospital</a>, led by first author Alexandra Lee (Tufts CS undergrad '20)
            </li>
        </ul>
    </li>
    
    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Dec 2020] Invited Talk at I Can't Believe It's Not Better Workshop at NeurIPS 2020
        </h4>
        <ul>
            <li>
                I'll be an invited speaker at the <a href="https://i-cant-believe-its-not-better.github.io/schedule/">I Can't Believe It's Not Better! Workshop</a> at NeurIPS 2020
            </li>
            <li>
                I'll talk about our recent work on Prediction Constrained training, covering in progress work <a href="https://arxiv.org/pdf/2012.06718.pdf">(Hope et al. arXiv 2020)</a> as well as recent publications at AISTATS 2018 and AISTATS 2020.
            </li>
            <li> <a href="https://slideslive.com/38938369/i-cant-believe-supervision-for-latent-variable-models-is-not-better-the-case-for-prediction-constrained-training"> Video recording </a>
            <li>
                Slides: <a href="{static}/talks/20201211_Talk_TheCaseForPredictionConstrainedTraining_CantBelieveNotBetterWorkshop.pdf"> The Case For Prediction Constrained Training [PDF] </a>
            </li>
        </ul>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [May 2020] Paper applying our latest ML methods to psychiatry accepted to JAMA Network Open
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/HughesPradierRossEtAl_JAMANetworkOpen_2020.pdf">
                Assessment of a Prediction Model for Antidepressant Treatment Stability Using Supervised Topic Models
                </a>
            </li>
            <li>
                Read this to understand how to use our latest prediction-constrained topic models to recommending personalized antidepressants.
            </li>
            <li>
                <a href="https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2766073"> Full paper and supplement available at jamanetwork.com </a>
            </li>
            <li>
                Special thanks to awesome clinical collaborators Roy Perlis MD and Tom McCoy MD.
            </li>
        </ul>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Jan 2020] Paper accepted at <a href="https://www.aistats.org/">AISTATS 2020</a>
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/FutomaHughesDoshiVelez_AISTATS_2020.pdf">
                POPCORN: Partially Observed Prediction-Constrained Reinforcement Learning
                </a> by Joseph Futoma, Michael C. Hughes, and Finale Doshi-Velez
            </li>
        </ul>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Dec 2019] Two papers accepted at <a href="http://www.approximateinference.org/">AABI 2019</a>
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/ZhangHughes_AABI_2019.pdf">
                Amortized Variational Inference for Rapid Model Comparison
                </a>, with first author <a href="https://www.linkedin.com/in/lilyhzhang">Lily Zhang</a
            </li>
            <li>
                <a href="{static}/papers/PradierHughesDoshiVelez_AABI_2019.pdf">
                Challenges in Computing and Optimizing Upper Bounds of Marginal Likelihood based on Chi-Square Divergences 
                </a>, with Melanie F. Pradier and Finale Doshi-Velez
            </li>

        </ul>

    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Nov 2019] Paper Accepted at <a href="">AAAI 2020</a>
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/WuParbhooHughesEtAl_AAAI_2020.pdf">
                Regional Tree Regularization for Interpretability in Deep Neural Networks
                </a>
            </li>
        </ul>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Aug 2019] Paper Accepted at <a href="">MLHC 2019</a>
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/NestorEtAl_MLHC_2019.pdf">
                    Feature Robustness in Non-stationary Health Records:
                    Caveats to Deployable Model Performance in Common Clinical Machine Learning Tasks
                </a>
            </li>
        </ul>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [June 2019] Invited Talk at <a href="">BNP 12</a>
        </h4>
        <ul>
            <li>"Scalable and Reliable Variational Inference for Dirichlet Process Clustering with Sparse Assignments"
            </li>
            <li>
            "Venue: \\href{https://www.stats.ox.ac.uk/bnp12/programme.html}{12th International Conference on Bayesian Nonparametrics}"
            </li>
        </ul>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Dec 2018] Two short papers accepted to workshops at NeurIPS 2018
        </h4>
        <ul>
            <li>
                <a href="{static}/papers/FutomaHughesDoshi_RLPOWorkshop2018.pdf">
                    Prediction-Constrained POMDPs
                </a> at RLPO @ NeurIPS2018
            </li>
            <li>
                <a href="{static}/papers/NestorEtAl_ML4HWorkshop2018.pdf">
                    Rethinking clinical prediction: Why machine learning must consider year of care and feature aggregation
                </a> at ML4Health @ NeurIPS 2018
            </li>
        </ul>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Aug 2018] I'm organizing 2 Workshops at NeurIPS 2018:
        </h4>
        <ul>
            <li>
            <a href="https://sites.google.com/view/nipsbnp2018">
            All of Bayesian Nonparametrics (BNP @ NeurIPS 2018)
            </a>
            </li>
            <li>
            <a href="https://ml4health.github.io/2018/">
                Machine Learning for Health (ML4H @ NeurIPS 2018)
            </a>
            </li>
        </ul>
        <p> Please consider submitting a short paper!
        </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Aug 2018] I'll present a tutorial -- 
        <a href="mlhc2018_tutorial.html">
            "Machine Learning for Clinicians: Advances for Multi-Modal Health Data"
        </a>
        -- <a href="https://www.mlforhc.org"> at MLHC 2018</a>.
        </h4>
        <p>
            Goal: make healthcare professionals aware of the latest tools from ML and help them be research effective collaborators.
        <a href="mlhc2018_tutorial.html">
                Please visit the 
                Tutorial Website 
            </a>
            (with outline, slides, and full bibliography).
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Aug 2018] I have joined the faculty at Tufts' Computer Science Department!
        </h4>
        <p>
            I'm actively looking for students (ugrad and Ph.D.) for various research projects. Please contact me if interested.
        </p>
    </li>



    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Apr 2018] <a href="{static}/images/SoCalNLPBestPaperCertificate.jpg">Best Paper Award</a> at <a href="https://socalnlp.github.io/symp18/index.html">SoCalNLP 2018</a>
        </h4>
        <p>
            Our winning <a href="{static}/papers/HughesHopeWeinerEtAl_SoCalNLP_2018.pdf">2-page short paper</a> was a compact summary of our AISTATS 2018 paper: <a href="{static}/papers/HughesEtAl_AISTATS_2018.pdf">Semi-Supervised Prediction-Constrained Topic Models</a>.
            Thanks to co-author Gabe for presenting the work, to the SoCal NLP organizers for hosting, and to Amazon for sponsoring the award.
        </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Jan 2018] Paper accepted to AISTATS 2018.
        </h4>
        <p>
            Our paper -- <a href="{static}/papers/HughesEtAl_AISTATS_2018.pdf">Semi-Supervised Prediction-Constrained Topic Models</a> -- describes a new framework for training topic models and other latent variable models to improve <i>supervised</i> predictions while still providing good generative models with interpretable topics. The new approach fixes core issues with past methods like sLDA, and shines especially in semi-supervised tasks, when only a small fraction of training examples are labeled.
        </p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Dec 2017] Presenting at NIPS 2017 Workshops
    </h4>
    <p class="list-group-item-text">
        &#8226;
        <a href="/papers/HughesEtAl_NIPSML4H_2017.pdf">
            Poster: Prediction-constrained Topic Models for Antidepressant Recommendation
        </a>
        at
        <a href="https://ml4health.github.io/2017/">
            ML for Health Workshop (NIPS ML4H 2017)
        </a>
    </p>
    <p class="list-group-item-text">
        &#8226;
        <a href="https://arxiv.org/pdf/1711.06178.pdf">
            Poster and Talk (by Mike Wu): Optimizing deep models with tree-regularization
        </a>
        at
        <a href="https://sites.google.com/view/timl-nips2017/schedule?authuser=0">
            Transparent and Interpretable ML workshop (NIPS TIML 2017)
        </a>
        (will also appear in AAAI '18)
    </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Nov 2017] Paper accepted to AAAI 2018.
        </h4>
        <p class="list-group-item-text">
            <a href="https://arxiv.org/pdf/1711.06178.pdf">
            Beyond Sparsity: Tree Regularization of Deep Models for Interpretability
            [PDF]
            </a>
        </p> 
        <p>
            Our paper describes a new regularization method to <emph>optimize</emph> recurrent neural networks to have more interpretable decision boundaries (closer to the decision trees that clinicians like).
        </p>
    </li>


    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Nov 2017] Invited talk at <a href="https://www.ll.mit.edu">MIT Lincoln Laboratory</a>
    </h4>
    <p class="list-group-item-text">
        "Optimizing Machine Learning Models for Clinical Interpretability"
    </p>
    <p class="list-group-item-text">
        Slides:
        <a href="https://www.dropbox.com/s/4aj9j1c2yw3kybj/20171114_LincolnLab.pdf?dl=0">
         [slides.pdf, 5 MB]
        </a>
    </p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Sep 2017] Organizing 
    <a href="https://ml4health.github.io/2017/">
        Machine Learning for Health (ML4H) workshop at NIPS 2017
    </a>
    </h4>
    <p>Please <a href="https://ml4health.github.io/2017/pages/call-for-papers.html#submission_instructions">submit some awesome papers!</a></p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Mar 2017] Presented paper on ICU intervention prediction at 
        <a href="https://www.amia.org/jointsummits2017/papers/">
            AMIA CRI '17
        </a>
    </h4>
    <p class="list-group-item-text">
        Nominated for Clinical Informatics Research Award (1 of 7 nominees)
    </p>
    <p class="list-group-item-text">
        <a href="/papers/GhassemiWuHughesEtAl_AMIACRI2017.pdf">
        paper [PDF] 
        </a>
        &#8226;
        <a href="/talks/20170328_AMIACRI2017.pdf">
         slides [PDF]
        </a>
    </p>
    </li>


    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Feb 2017] Invited talk on BNPy at Boston Bayesians meetup
    </h4>
    <p class="list-group-item-text">
        <a href="https://www.meetup.com/Boston-Bayesians/events/237060774/">
        Event website and talk abstract
        </a>
    </p>
    <p class="list-group-item-text">
        Slides from my talk:
        <a href="https://www.dropbox.com/s/rpdyra2pznfr98i/20170207_BNPyTalk_BostonBayesians.pptx?dl=0">
         [slides.pptx, 73 MB]</a>
        <a href="https://www.dropbox.com/s/agf93kdfbbnthn5/20170207_BNPyTalk_BostonBayesians_Small.pdf?dl=0">
         [slides.pdf, 23 MB]</a>
    </p>
    </li>


    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Dec 2016] BNPy software tutorial at NIPS 2016 workshop
    </h4>
    <p class="list-group-item-text">
        Slides from my talk:
        <a href="https://www.dropbox.com/s/oalse0q7q0c7fmt/20161207_bnpytalk.pptx?dl=0">
         [slides.pptx]</a>
        <a href="https://www.dropbox.com/s/2c0c7rtp5uxk0hj/20161207_bnpytalk.pdf?dl=0">
         [slides.pdf]</a>
    </p>
    <p class="list-group-item-text">
        New: <a href="https://bnpy.readthedocs.io/en/latest/index.html">
        BNPy project website </a>
        with example gallery
    </p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Dec 2016] Posters at NIPS 2016 Workshops
    </h4>
    <p class="list-group-item-text">
        <a href="/papers/HughesElibolMcCoyPerlisDoshi_MLHCWorkshopAtNIPS2016.pdf">
        Fast per-document inference for supervised topic models</a>
        at
        <a href="http://www.nipsml4hc.ws/home">
            ML for Health workshop.
        </a>
    </p>
    <p class="list-group-item-text">
        <a href="/papers/JiHughesSudderth_PracticalBNPWorkshop_2016.pdf">
        HDP models for natural images</a>
        at
        <a href="https://sites.google.com/site/nipsbnp2016/">
            Practical BNP workshop.
        </a>
    </p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Sep 2016] Organizing Workshop at NIPS '16: Practical Bayesian Nonparametrics
    </h4>
    <p class="list-group-item-text" style="overflow-wrap: break-word; word-wrap: break-word; word-break: break-all;">
        Please consider submitting to our workshop: 
    <a href="https://sites.google.com/site/nipsbnp2016/">https://sites.google.com/site/nipsbnp2016/</a> 
    </p>
    </li>

  <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Aug 2016] Started post-doc at Harvard
    </h4>
    <p class="list-group-item-text">
        You can now find me at my new office in Maxwell-Dworkin (MD 209).
    </p>
    </li>

    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [May 2016] Successful Ph.D. defense!
    </h4>
    <p class="list-group-item-text">
        Many thanks to family and friends who supported me along the way.
    </p>
    </li>


    <li class="list-group-item">
    <h4 class="list-group-item-heading">
    [Jan 2016] Invited talks on my thesis.
    </h4>
    <p class="list-group-item-text">
    I visited several research groups at Northeastern, U. Washington, and MIT to
    discuss results from my thesis work trying to make 
    effective variational inference for clustering that scales to millions of examples.
    <a href="https://dl.dropboxusercontent.com/u/568924/InvitedTalk_ScalableInferenceThatAdaptsClusters_v20160123.pdf">
    [slides PDF] </a>
    <a href="https://dl.dropboxusercontent.com/u/568924/InvitedTalk_ScalableInferenceThatAdaptsClusters_v20160123.pptx">
    [slides PPTX] </a>
    </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Dec 2015] Invited talk at NIPS 2015 workshop.
        </h4>
        <p class="list-group-item-text">
            I gave an invited talk at the <a href="https://sites.google.com/site/nipsbnp2015">
            Bayesian Nonparametrics: The Next Generation workshop </a>
            about my thesis work building 
            effective variational inference for models based 
            on the Dirichlet process and its hierarchical variants.
          <a href="https://dl.dropboxusercontent.com/u/568924/NIPSBNP2015_v1210.pdf"> [slides PDF] </a>
    </p>
    </li>


    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [Sept 2015] Paper accepted at NIPS 2015.
        </h4>
        <p class="list-group-item-text">
            <a href="/papers/HughesStephensonSudderth_NIPS_2015.pdf">
            Our paper [PDF] 
            </a>
            describes a new algorithm for Bayesian nonparametric hidden Markov models that can handle hundreds of sequences and add or remove hidden states during a single training run.
        </p>
    </li>

    <li class="list-group-item">
        <h4 class="list-group-item-heading">
        [May 2015] Paper accepted at AISTATS 2015.
        </h4>
        <p class="list-group-item-text">
            <a href="/papers/HughesKimSudderth_AISTATS_2015.pdf">
            Our paper [PDF] 
            </a>
            describes a new algorithm for topic models
            that can effectively remove redundant or junk topics during a single training run.
        </p>
    </li>

    
</ul>
