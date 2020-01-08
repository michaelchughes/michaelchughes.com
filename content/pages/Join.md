Title: Join My Lab
Date: 2018-09-01
save_as: join.html

Join my research team at Tufts CS! Become part of the growing and energetic [Tufts ML Research Group](https://www.cs.tufts.edu/research/ml/).

In Fall-Winter 2019-2020, I am actively recruiting:

* 1 **postdoc** for an exiting funded project on time-series analysis [Job Ad / Application Instructions](https://groups.google.com/d/msg/ml-news/DWI0sZtSBpU/p3wrL682BAAJ)
* 1-2 **new Ph.D. students** to join in Spring or Fall 2020
* current undergrad and masters students

Keep reading below for the skills I'm looking for, some possible high-level project ideas, etc.

Jump to: [Project Ideas](#project_ideas) &#8226; [Current Tufts Students](#current_tufts_students) &#8226; [Prospective Students](#prospective_students) &#8226; [Prerequisite Skills](#prereq_skills)


<a name="project_ideas"></a>
## Possible projects/topics

Possible project ideas, based on what I've done in the past with links to sample research papers:

#### Statistical Machine Learning

* **Semi-supervised training of latent variable models** [[My AISTATS 2018 paper]({static}/papers/HughesEtAl_AISTATS_2018.pdf)]: How do we learn from datasets when labeled measurements are rare but unlabeled measurements are easy? Labels we wish to predict are often expensive, time-consuming, or dangerous to collect (e.g. does a patient respond to this medication?), but we have many thousands of *unlabeled* data measurements that might be useful (patient records). How can we make sure this works even when our model is wrong?

* **Bayesian nonparametric models** [[My NIPS 2015 paper]]({static}/papers/HughesStephensonSudderth_NIPS_2015.pdf), [[Bayesian Nonparametrics in Python (BNPy) package]](https://bnpy.readthedocs.io) : Many clustering algorithms require the number of clusters to be chosen in advance before any model fitting. Can we apply Bayesian nonparametric models to 'let the data speak' and learn a posterior distribution over possible clusterings that adapts to the complexity of the data at hand? How do we avoid the local optima that might result?

* **Latent Variable Models with Neural Networks for Recognition**: I'm excited about [deep generative models](https://www.shakirm.com/slides/DeepGenModelsTutorial.pdf) and variational autoencoders as ways to do fast inference for flexible model families. See my [[AABI 2019 paper]({static}/papers/ZhangHughes_AABI_2019.pdf)] with Lily Zhang on amortized VI for model comparison for some ideas of directions here.

* **Models that are Robust to Missing Data**: How do we make good statistical predictions when some measurements are missing, or measurements happen at many different frequencies (some every minute, some irregularly every dozen hours or so)? 


#### Machine Learning applications in Healthcare

* **Intensive Care Interventions** [[My AMIA CRI 2017 paper]({static}/papers/GhassemiWuHughesEtAl_AMIACRI2017.pdf)], [[MIMIC dataset](https://mimic.physionet.org/)]: Patients in the intensive care units of hospitals are evolving all the time. Can we predict when they will need mechanical ventilators based on sensor readings? Could we do so far enough in advance that we might helpfully change clinical workflow? 

* **Depression**: Patients who suffer from depression often look to antidepressant drugs, but currently psychiatrists have trouble knowing which of many drugs will work for that patient. Can we use probabilistic ML to predict which drug will work for a patient based on their history?

* **Fertility Medicine**: Couples who struggle to get pregnant look to in-vitro fertilization (IVF), which requires several medication-based interventions. Can we learn from previous records to predict which drugs will give patients the best chance? Can our models give insight into the science behind why predictions might work?


<a name="current_tufts_students"> </a>
## Current students at Tufts

I'm excited to work with strong undergraduate, Masters, and Ph.D. students to make exciting machine learning research happen. I don't generally pursue research projects with students who are brand new to probabilistic machine learning or data analysis, but if you have even a small bit of prior experience I would love for you to join the team. See below for a quick recap of skills I hope students have before joining a project.

If you think you have the right background and are willing to commit **at least** two semesters (or at least 1 semester + summer) to research, please send me an email with:

* what project ideas seem most exciting to you?
* quick list of courses you've completed at Tufts or other schools relevant to machine learning / data analysis
* pointer to a previous course project report / github repository / etc. to demonstrate ML skills or coding skills
* statement confirming you're willing to give several hours a week for multiple semesters (or a semester + summer)

I know this is not a casual commitment, but I will work hard with you to deliver a meaningful experience that results in some kind of open-source software release and/or publication in a workshop or conference.
If you look at [my CV](/cv.html), you'll see all the students marked with ^u (for ugrad), ^m (for masters), or ^d (for doctoral) that I've mentored in the past, so I have a pretty decent track record.

<a name="prospective_students"> </a>
## Prospective students

#### Prospective Ph.D. students: Apply to Tufts First

You should apply to the Tufts CS Ph.D. program. If you mention me by name in your research statement, I'll be able to consider the application carefully.

* [CS Ph.D. Program Overview](https://engineering.tufts.edu/cs/current/phd/computer-science)
* [Application](https://gradase.admissions.tufts.edu/apply/)
* Deadlines: apply for Fall admission (deadline mid December) OR Spring admission (deadline mid Sept.)

#### Prospective M.S. or Post-Bacc. students: Apply to Tufts First

Generally, I plan to take M.S. students to join the lab after they have been accepted into a program *and* complete some machine-learning coursework successfully. You should apply to one of the possible Tufts CS masters programs, including

* [M.S. in Data Science](https://asegrad.tufts.edu/academics/explore-graduate-programs/data-science)
* [M.S. in Computer Science](https://engineering.tufts.edu/cs/prospective/masters)
* [Post Bacc. Certificates in Data Science or Computer Science](https://engineering.tufts.edu/cs/prospective/certificate-postbac)

#### Note about Email for Prospective Students External to Tufts

Please do contact me via email if you are interested in working with me. This helps me know who to look for in the applicant pool. It helps if you clearly articulate why your research interests overlap with mine by mentioning a topic listed on this page.

I get **tons** of email, so I regret that I am unable to respond to about 95% of the unsolicited messages I get seeking admission to our Masters/PhD. If you mention the word "dinosaur" in the subject line, I'll be more likely to respond.

If you don't get a response, this doesn't mean I'm not interested. Usually I wait to see a full application, and if I like what I see I will reach out to schedule a Skype interview. 


<a name="prereq_skills"></a>
## Prerequisite Skills

Preferred candidates for PHD study will have a strong machine learning mathematical background *and* strong Python data science development background.

#### Probabilistic Machine Learning Skills

My group's work in statistical machine learning requires some prior understanding of concepts like Bayesian data analysis, supervised machine learning, optimization algorithms (e.g. gradient descent), unsupervised machine learning (e.g. k-means cluster/PCA) or deep learning. Good evidence for your probabilistic ML capabilities would include:

* Evidence that you can complete a self-directed research project involving fitting a probabilistic model to data and interpreting its results. This might be a self-study project or a project from previous coursework. The key skill here is to be able to translate inference algorithm pseudocode from a research paper into a concrete code implementation without much guidance.

* Successful completion of ML coursework at Tufts or another university, including at least a course like COMP 135 (Intro to ML), but preferably a course with more mathematical content like COMP 136 (Statistical Pattern Recognition) or other special-topics-level courses taught by ML faculty. If you did a final project for that course, sending me your report/slides would be a great litmus test.


#### Python Data Science Development Skills

A key goal of my group is to develop open-source Python software so that non-experts can apply our novel machine learning algorithms to their datasets in meaningful ways. For examples of previous open-source work, see our [Bayesian Nonparametrics in Python (BNPy) package](https://bnpy.readthedocs.io) or our recent [Prediction-constrained topic models package](https://github.com/dtak/prediction-constrained-topic-models).

I am keen to make these packages more usable and would love some help extending their features. 

Good evidence of software capabilities would include:

* An open-source repository on github showcasing some small-but-interesting project produced using common Python data science stack packages (numpy, scipy, pandas, scikit-learn, PyTorch, tensorflow, etc.)

* If you did some closed-source contributions (perhaps at an internship), please describe them in a brief paragraph. Try to give examples of concrete algorithms you've implemented or the scale of datasets you've worked with.


