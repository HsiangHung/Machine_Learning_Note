
# Statistical Testing

The conversion matrix of testing is [[Massa]][S. Massa, Kolmogorov Smirnov Test & Power of Tests]

<a href="https://www.codecogs.com/eqnedit.php?latex=\begin{matrix}&space;\textrm{&space;Pred&space;}&space;/&space;\textrm{Actual&space;}&space;&&space;H_0&space;\textrm{&space;False}&space;&&space;H_0&space;\textrm{&space;True}&space;\\&space;H_0&space;\textrm{&space;False}&space;&&space;1-\beta&space;&&space;\alpha&space;\textrm{&space;(Type&space;I&space;error)}&space;\\&space;H_0&space;\textrm{&space;True}&space;&&space;\beta&space;\textrm{&space;(Type&space;II&space;error)}&space;&&space;1-\alpha&space;\end{matrix}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\begin{matrix}&space;\textrm{&space;Pred&space;}&space;/&space;\textrm{Actual&space;}&space;&&space;H_0&space;\textrm{&space;False}&space;&&space;H_0&space;\textrm{&space;True}&space;\\&space;H_0&space;\textrm{&space;False}&space;&&space;1-\beta&space;&&space;\alpha&space;\textrm{&space;(Type&space;I&space;error)}&space;\\&space;H_0&space;\textrm{&space;True}&space;&&space;\beta&space;\textrm{&space;(Type&space;II&space;error)}&space;&&space;1-\alpha&space;\end{matrix}" title="\begin{matrix} \textrm{ Pred } / \textrm{Actual } & H_0 \textrm{ False} & H_0 \textrm{ True} \\ H_0 \textrm{ False} & 1-\beta & \alpha \textrm{ (Type I error)} \\ H_0 \textrm{ True} & \beta \textrm{ (Type II error)} & 1-\alpha \end{matrix}" /></a>

where <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha&space;=&space;\textrm{Pr}(\textrm{reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;True})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha&space;=&space;\textrm{Pr}(\textrm{reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;True})" title="\alpha = \textrm{Pr}(\textrm{reject H}_0| \textrm{H}_0 \textrm{ is True})" /></a> is the probability, that given the null hypothesis is true, you reject. <a href="https://www.codecogs.com/eqnedit.php?latex=\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta&space;=&space;\textrm{Pr}(\textrm{fail&space;to&space;reject&space;H}_0|&space;\textrm{H}_0&space;\textrm{&space;is&space;False})" title="\beta = \textrm{Pr}(\textrm{fail to reject H}_0| \textrm{H}_0 \textrm{ is False})" /></a> is the probability, that given the null hypothesis is false, you fail to reject. Ideally, we wish not only lower <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a>, but also lower <a href="https://www.codecogs.com/eqnedit.php?latex=\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\beta" title="\beta" /></a>.


<a href="https://www.codecogs.com/eqnedit.php?latex=1-\beta" target="_blank"><img src="https://latex.codecogs.com/gif.latex?1-\beta" title="1-\beta" /></a> is the power. Higher power has more reliable statistical testing.






# Reference



[S. Massa, Kolmogorov Smirnov Test & Power of Tests]: http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf
[[Massa] S. Massa, Kolmogorov Smirnov Test & Power of Tests](http://www.stats.ox.ac.uk/~massa/Lecture%2013.pdf)
