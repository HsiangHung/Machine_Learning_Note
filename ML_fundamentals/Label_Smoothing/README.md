
# Label Smoothing 


## What is Label Smoothing?

Label Smoothing is a regularization technique used in machine learning to prevent models from overfitting to the training data. In traditional classification tasks, we aim to assign a single label to each input example. However, in many cases, the true label for an example may not be completely certain. 

For example, in image classification, there may be **ambiguity** as to whether an image contains a certain object or not. In such cases, a model that assigns a very high probability to a single label may be **overconfident** and lead to poor generalization. This can lead to poor performance on the validation or test set, as the model has not learned to capture the underlying patterns in the data. [[Saturn Cloud]][Label Smoothing in PyTorch A Guide for Data Scientists]


## Why is Label Smoothing Important?
 
Label Smoothing addresses this problem by modifying the targets used in training. Instead of using a one-hot encoding of the true label, we use a **smoothed distribution** over all the labels. This has the effect of reducing the confidence of the model in its predictions and encourages it to learn more robust features; then the model can learn the data generalizing to unseen examples. 

Label Smoothing is one technique that can help prevent overfitting by encouraging models to learn more robust features. By reducing the confidence of the model in its predictions, Label Smoothing can make the model more resilient to noise in the data and help avoid overfitting to the training set. This can lead to better generalization and improved performance on the validation or test set.

## Label Smoothing

Assume in a multiclass classification problem $y_i=\lbrace 1, 2, \cdots, K \rbrace$, the ground truth distribution is $p(y_i \vert x_i)$ and the predicted label distribution (with a model with parameters $\theta$) is $q_{\theta}(y_i \vert x_i)$. The ground truth $y$ is a one-hot encoded vector.

The cross entropy loss function would be

$$L = \sum^N_{i=1}H_i(p, q_{\theta})$$




## Example: Label Smoothing in PyTorch

In PyTorch, we can use the `nn.KLDivLoss` function to compute the Kullback-Leibler divergence between two distributions. We can use this function to compute the loss between the smoothed label distribution and the model’s predicted distribution. See detail on [[Saturn Cloud]][Label Smoothing in PyTorch A Guide for Data Scientists].

```Python
import torch.nn as nn
import torch.nn.functional as F

class LabelSmoothingLoss(nn.Module):
    def __init__(self, smoothing=0.1, dim=-1):
        super(LabelSmoothingLoss, self).__init__()
        self.smoothing = smoothing
        self.dim = dim

    def forward(self, pred, target):
        target = F.one_hot(target, num_classes=pred.size(-1))
        target = target.float()
        target = (1 - self.smoothing) * target + self.smoothing / pred.size(-1)
        log_pred = F.log_softmax(pred, dim=self.dim)
        loss = nn.KLDivLoss(reduction='batchmean')(log_pred, target)
        return loss
```

To use this loss function in training, we simply replace the traditional cross-entropy loss with the `LabelSmoothingLoss` function:
```Python
import torch.optim as optim

model = MyModel()
criterion = LabelSmoothingLoss(smoothing=0.1)
optimizer = optim.Adam(model.parameters())

for epoch in range(num_epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
```

This space is dedicated to some fundamental theory on Machine Learning.

Some recommended summary:

* [Label Smoothing in PyTorch A Guide for Data Scientists]: https://saturncloud.io/blog/label-smoothing-in-pytorch-a-guide-for-data-scientists/
[[Saturn Cloud] Label Smoothing in PyTorch A Guide for Data Scientists](https://saturncloud.io/blog/label-smoothing-in-pytorch-a-guide-for-data-scientists/)







