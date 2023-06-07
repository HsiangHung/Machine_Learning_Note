# GAN

## MinMax Loss

The value function for GAN is [[Google]][Google ML Developer - Loss Functions]

$$\min_{G} \max_{D} V(G, D) = \mathbb{E}_x [ \log{\big( D(x) \big)} ] + \mathbb{E}_z[ \log{\big( 1-D(G(z)) \big)} ],$$

where $D(x)$ is the discriminator's estimate of the probability that real data instance $x$ is real, whereas $G(z)$ is the generator's output when given noise $z$, so $D(G(z))$ is the discriminator's estimate of the probability that a fake instance is real. 

$\mathbb{E}_x$ is the expected value over all real data instances, whereas $\mathbb{E}_z$ is the expected value over all random inputs to the generator, i.e. the expected value over all generated fake instances $G(z)$.

The generator tries to minimize this function while the discriminator tries to maximize it. Looking at it as a min-max game, this formulation of the loss seemed effective. 

In practice, it saturates for the generator, meaning that the generator quite frequently stops training if it doesn’t catch up with the discriminator.


#### Reference

* [Google ML Developer - Loss Functions]: https://developers.google.com/machine-learning/gan/loss
[[Google] Google ML Developer - Loss Functions](https://developers.google.com/machine-learning/gan/loss)

* [Understanding GAN Loss Functions]: https://neptune.ai/blog/gan-loss-functions
[[neptune.ai] Understanding GAN Loss Functions](https://neptune.ai/blog/gan-loss-functions)


## Convergence and Evaluate GAN



* [How good is my GAN?]: https://inria.hal.science/hal-01850447/document
[[Konstantin Shmelkov et al.] How good is my GAN?](https://inria.hal.science/hal-01850447/document)

* [GAN — Why it is so hard to train Generative Adversarial Networks!]: https://jonathan-hui.medium.com/gan-why-it-is-so-hard-to-train-generative-advisory-networks-819a86b3750b
[[Jonathan Hui] GAN — Why it is so hard to train Generative Adversarial Networks!](https://jonathan-hui.medium.com/gan-why-it-is-so-hard-to-train-generative-advisory-networks-819a86b3750b)








## Time-Series GAN

* TimeGAN: [[Jinsung Yoon et al.]][Time-series Generative Adversarial Networks]

* Probabilistic autoregressive model (PAR): [[Open source - SDV]][PAR Model]



#### Reference

* [Time-series Generative Adversarial Networks]: https://papers.nips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html
[[Jinsung Yoon et al.] Time-series Generative Adversarial Networks](https://papers.nips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html)


* [Qualitative and Quantitative Evaluation of Multivariate Time-Series Synthetic Data Generated Using MTS-TGAN: A Novel Approach]: https://www.mdpi.com/2076-3417/13/7/4136
[[Parul Yadav et al.] Qualitative and Quantitative Evaluation of Multivariate Time-Series Synthetic Data Generated Using MTS-TGAN: A Novel Approach](https://www.mdpi.com/2076-3417/13/7/4136)


* [PAR Model]: https://sdv.dev/SDV/user_guides/timeseries/par.html
[[Open source - SDV] PAR Model](https://sdv.dev/SDV/user_guides/timeseries/par.html)





## Tabluar data GAN




