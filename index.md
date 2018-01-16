---
layout: default
---

# CS 294: Fairness in Machine Learning 

UC Berkeley, Fall 2017  
Time: Monday and Friday 2:30PM - 3:59PM  
Location: Soda 405  
Instructor: Moritz Hardt

Grading policy: 50% in class participation, 50% project

Undergraduate enrollment policy: With permission from the instructor only. Email
transcript, and description of any relevant prior projects or research experience.

Students will receive access to a slack channel for class related discussions.

## Updates
* See these <a href="http://mrtz.org/nips17">NIPS 2017 tutorial slides</a> and <a href="https://vimeo.com/248490141">video</a> for a two-hour introduction to the topic.
* **Important**: Projects will be presented on **Tuesday, Dec 12** from 11:30--2:30.
* *8/15/2017* --- The class has reached its enrollment cap. Additional
 participants are waitlisted for now. If you would like to participate and
 couldn't enroll, please come to the first day of class and talk to me.

## Summary

This is an intensive graduate seminar on fairness in machine learning. The focus
is on understanding and mitigating *discrimination based on sensitive
characteristics*, such as, gender, race, religion, physical ability, and sexual
orientation. Recent years have shown that unintended discrimination arises
naturally and frequently in the use of machine learning and algorithmic 
decision making.

We will work systematically towards a technical understanding of this problem
mindful of its social and legal context. 

## Lectures

* [Day 1](1.html) (8/25) Overview talk
* [Day 2](2.html) (8/28) Barocas and Selbst
* [Day 3](3.html) (9/1) Blasts from the past
* [Day 4](4.html) (9/8) Intro to oboservational measures
* Day 5 (9/11) Discussing some project ideas
* Day 6 (9/15) Guest lecture by [Kristian Lum](https://hrdag.org/people/kristian-lum-phd/) on recidivism prediction
* Day 7 (9/18) Fairness through Awareness
* Day 8 (9/22) Simpson's paradox
* Day 9 (9/25) First few chapters of Pearl textbook
* Day 10 (9/29) Chapter 4, 5 in Peters textbook
* Day 11 (10/2) Chapter 6 in Peters textbook 
* Day 12 (10/6) Chapter 7, 8 in Peters textbook 
* Day 13 (10/9) Causal fairness papers
* Day 14 (10/13) More causal fairness papers
* Day 15 (10/16) Causality recap and outlook
* Day 16 (10/20) Measurement
* Day 17 (10/24) Hand Chapter 2
* Day 18 (10/27) Hand Chapter 3
* Day 19 (10/31) Hand Chapter 4, failure points of measurement
* Day 20 (11/3) Raw Data is an Oxymoron
* Day 21 (11/6) Discussing project ideas
* *No class on 11/10 due to Veteran's Day.*
* Day 22 (11/13) Introduction to sampling
* Day 23 (11/17) Closer look at crime surveys and measurement
* Day 24 (11/20) Critiques of algorithmic decision making
* *No class on 11/24 due to Thanksgiving.*
* Day 25 (11/27) 
* Day 26 (11/30)
* Day 27 (12/4)
* Day 28 (12/8)
* Day 29 (12/10) **Project presentations**, special time 11:30--2:30

# Outline (preliminary)

Last updated: August 17, 2017

* [Sources of unfairness](#sources)
* [Statistical measures of discrimination](#statistical)
* [Trade-offs and impossibility results](#tradeoffs)
* [Beyond observational measures](#beyond)
* [Measurement, sampling](#measurement)
* [Legal and policy perspectives](#policy)


<a name="sources"></a>
## Sources of unfairness


[Big Data: A Report on Algorithmic Systems, Opportunity, and Civil Rights](https://obamawhitehouse.archives.gov/sites/default/files/microsites/ostp/2016_0504_data_discrimination.pdf)  
The White House. 2016.

[Bias in computer systems](http://dl.acm.org/citation.cfm?id=230561)  
Batya Friedman, Helen Nissenbaum. 1996

[The Hidden Biases in Big Data](https://hbr.org/2013/04/the-hidden-biases-in-big-data)  
Kate Crawford. 2013.

[Big Data’s Disparate Impact](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2477899)  
Solon Barocas, Andrew Selbst. 2014.

Blog post: [How big data is unfair](https://medium.com/@mrtz/how-big-data-is-unfair-9aa544d739de)  
Moritz Hardt. 2014

[Semantics derived automatically from language corpora contain human-like
biases](http://science.sciencemag.org/content/356/6334/183)  
Aylin Caliskan, Joanna J. Bryson, Arvind Narayanan

<a name="statistical"></a>
## Statistical measures of discrimination

[Sex Bias in Graduate Admissions: Data from Berkeley](http://science.sciencemag.org/content/187/4175/398)  
P. J. Bickel, E. A. Hammel, J. W. O'Connell. 1975.

Simpson’s paradox  
Pearl (Chapter 6)  
[Tech report](http://bayes.cs.ucla.edu/R264.pdf)

[Certifying and removing disparate impact](https://arxiv.org/abs/1412.3756)  
Michael Feldman, Sorelle Friedler, John Moeller, Carlos Scheidegger, Suresh
Venkatasubramanian

[Equality of Opportunity in Supervised
Learning](https://arxiv.org/abs/1610.02413)  
Moritz Hardt, Eric Price, Nathan Srebro. 2016.

Blog post: [Approaching fairness in machine learning](http://blog.mrtz.org/2016/09/06/approaching-fairness.html)  
Moritz Hardt. 2016.

### COMPAS and criminal justice

[Machine Bias](https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing)  
Julia Angwin, Jeff Larson, Surya Mattu and Lauren Kirchner, ProPublica  
Code review:  
[github.com/probublica/compas-analysis](https://github.com/propublica/compas-analysis)  
[github.com/adebayoj/fairml](https://github.com/adebayoj/fairml)

[COMPAS Risk Scales: Demonstrating Accuracy Equity and Predictive
Parity](https://www.documentcloud.org/documents/2998391-ProPublica-Commentary-Final-070616.html)  
Northpointe Inc.

[Fairness in Criminal Justice Risk Assessments: The State of the
Art](https://arxiv.org/abs/1703.09207)  
Richard Berk, Hoda Heidari, Shahin Jabbari, Michael Kearns, Aaron Roth. 2017.

[Courts and Predictive
Algorithms](http://www.datacivilrights.org/pubs/2015-1027/Courts_and_Predictive_Algorithms.pdf)  
Angèle Christin, Alex Rosenblat, and danah boyd. 2015.  
[Discussion
paper](http://www.datacivilrights.org/pubs/2015-1027/WDN-Courts_and_Predictive_Algorithms.pdf)

[Limitations of mitigating judicial bias with machine
learning](https://www.nature.com/articles/s41562-017-0141)  
Kristian Lum. 2017.

<a name="tradeoffs"></a>
## Trade-offs and impossibility results

### Classification, Calibration, Precision, Recall

[Probabilistic Outputs for Support Vector Machines and Comparisons to
Regularized Likelihood Methods](http://citeseer.ist.psu.edu/viewdoc/summary?doi=10.1.1.41.1639)  
John C. Platt. 1999.

[Inherent Trade-Offs in the Fair Determination of Risk Scores](https://arxiv.org/abs/1609.05807)  
Jon Kleinberg, Sendhil Mullainathan, Manish Raghavan. 2016.

[Fair prediction with disparate impact: A study of bias in recidivism prediction
instruments](https://arxiv.org/abs/1610.07524)  
Alexandra Chouldechova. 2016.

[Attacking discrimination with smarter machine learning](https://research.google.com/bigpicture/attacking-discrimination-in-ml/)  
An interactive visualization by Martin Wattenberg, Fernanda Viégas, and Moritz
Hardt. 2016.

[Algorithmic decision making and the cost of fairness](https://arxiv.org/abs/1701.08230)  
Sam Corbett-Davies, Emma Pierson, Avi Feller, Sharad Goel, Aziz Huq. 2017.

[The problem of Infra-marginality in Outcome Tests for Discrimination](https://5harad.com/papers/threshold-test.pdf)  
Camelia Simoiu, Sam Corbett-Davies, Sharad Goel. 2017.

### Inherent limitations of observational measures

[Equality of Opportunity in Supervised
Learning](https://arxiv.org/abs/1610.02413)  
Moritz Hardt, Eric Price, Nathan Srebro. 2016.

<a name="beyond"></a>
## Beyond observational measures

### Causal reasoning

Background reading:  
Pearl (Chapter 1--3)  
Pearl (Section 4.5.3)

[Elements of Causal Inference](http://www.math.ku.dk/~peters/elements.html)  
Peters, Janzing, Sch&ouml;lkopf

[On causal interpretation of race in regressions adjusting for confounding and
mediating variables](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4125322/)  
Tyler J. VanderWeele and Whitney R. Robinson. 2014.

### Causal fairness criteria

[Counterfactual Fairness](https://arxiv.org/abs/1703.06856)  
Matt J. Kusner, Joshua R. Loftus, Chris Russell, Ricardo Silva. 2017.

[Avoiding Discrimination through Causal
Reasoning](https://arxiv.org/abs/1706.02744)  
Niki Kilbertus, Mateo Rojas-Carulla, Giambattista Parascandolo, Moritz Hardt,
Dominik Janzing, Bernhard Schölkopf. 2017.

[Fair Inference on Outcomes](https://arxiv.org/abs/1705.10378)  
Razieh Nabi, Ilya Shpitser

### Similarity modeling, matching 

[Fairness Through Awareness](https://arxiv.org/abs/1104.3913)  
Cynthia Dwork, Moritz Hardt, Toniann Pitassi, Omer Reingold, Rich Zemel. 2012.

[On the (im)possibility of fairness](https://arxiv.org/abs/1609.07236)  
Sorelle A. Friedler, Carlos Scheidegger, Suresh Venkatasubramanian. 2016.

[Why propensity scores should not be
used](https://gking.harvard.edu/files/gking/files/psnot.pdf)  
Gary King, Richard Nielson. 2016.


<a name="measurement"></a>
## Measurement, sampling

[Raw Data is an Oxymoron](https://mitpress.mit.edu/books/raw-data-oxymoron)  
Edited by Lisa Gitelman. 2013.

Blog post: [What's the most important thing in Statistics that's not in the
textbooks](http://andrewgelman.com/2015/04/28/whats-important-thing-statistics-thats-not-textbooks/)  
Andrew Gelman. 2015.

[Deconstructing Statistical Questions](http://statlab.bio5.org/sites/default/files/fall2014/hand-deconstructin.pdf)  
David J. Hand. 1994.

[Statistics and the Theory of
Measurement](http://www.lps.uci.edu/~johnsonk/CLASSES/MeasurementTheory/Hand1996.StatisticsAndTheTheoryOfMeasurement.pdf)  
David J. Hand. 1996.

[Measurement Theory and Practice: The World Through
Quantification](http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470685670.html)  
David J. Hand. 2010

[Survey Methodology, 2nd Edition](http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470465468.html)  
Robert M. Groves, Floyd J. Fowler, Jr., Mick P. Couper, James M. Lepkowski,
Eleanor Singer, Roger Tourangeau. 2009

[Sampling: Design and Analysis](http://www.cengage.com/c/sampling-design-and-analysis-2e-lohr)  
Sharon L. Lohr  
Chapter 7.6, 8, 12, 14, 15


## Unsupervised learning

[Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word
Embeddings](https://arxiv.org/abs/1607.06520)  
Tolga Bolukbasi, Kai-Wei Chang, James Zou, Venkatesh Saligrama, Adam Kalai. 2016.

[Men Also Like Shopping: Reducing Gender Bias Amplification using Corpus-level
Constraints](https://arxiv.org/abs/1707.09457)  
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, Kai-Wei Chang. 2017.

<a name="policy"></a>
## Legal and policy perspectives

[Big Data’s Disparate Impact](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2477899)  
Solon Barocas, Andrew Selbst. 2014.

[It’s Not Privacy, and It’s Not Fair](https://www.stanfordlawreview.org/online/privacy-and-big-data-its-not-privacy-and-its-not-fair)  
Cynthia Dwork, Deirdre K. Mulligan. 2013.

[The Trouble with Algorithmic
Decisions](http://journals.sagepub.com/doi/abs/10.1177/0162243915605575)  
Tal Zarsky. 2016.

[How Copyright Law Can Fix Artificial Intelligence's Implicit Bias
Problem](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3024938)  
Amanda Levendowski. 2017.


## Background reading

[A Theory of Justice](http://www.hup.harvard.edu/catalog.php?isbn=9780674000780&content=reviews)  
John Rawls

[Equality of
Opportunity](http://www.hup.harvard.edu/catalog.php?isbn=9780674004221)  
John E. Roemer

[Causality](http://bayes.cs.ucla.edu/BOOK-2K/)  
Judea Pearl

[Elements of Causal Inference](http://www.math.ku.dk/~peters/elements.html)  
Peters, Janzing, Sch&ouml;lkopf

[Counterfactuals and Causal
Inference](http://www.cambridge.org/catalogue/catalogue.asp?isbn=9781107065079)  
Morgan and Winship

[Equity](http://press.princeton.edu/titles/5379.html)  
Peyton Young

[Weapons of Math Destruction](https://weaponsofmathdestructionbook.com/)  
Cathy O’Neil. 
