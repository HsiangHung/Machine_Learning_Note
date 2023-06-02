# GAN

## MinMax Game

The value function for GAN is

$$\min_{G} \max_{D} V(G, D) = \mathbb{E}_{x \sim p(x)} [ \log{\big( D(x) \big)} ] + \mathbb{E}[ \log{\big( 1-D(G(x)) \big)} ]$$

The generator tries to minimize this function while the discriminator tries to maximize it. Looking at it as a min-max game, this formulation of the loss seemed effective. 

In practice, it saturates for the generator, meaning that the generator quite frequently stops training if it doesn’t catch up with the discriminator.

## Tabluar data GAN


## Time-Series GAN

* TimeGAN: [[Jinsung Yoon et al.]][Time-series Generative Adversarial Networks]




## Reference

* [Time-series Generative Adversarial Networks]: https://papers.nips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html
[[Jinsung Yoon et al.] Time-series Generative Adversarial Networks](https://papers.nips.cc/paper_files/paper/2019/hash/c9efe5f26cd17ba6216bbe2a7d26d490-Abstract.html)


