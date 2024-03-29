# Machine Learning Notes

This repo is used to summarize ML knowledge I have learned and the relevant blogs.




## Install Keras and Tensorflow in Virtual Evn with Jupyter

First [install tensorflow](https://www.tensorflow.org/install/pip#package-location), then [install Keras](https://keras.io/#installation).

### 1. Create a virtual environment using Conda

In **Create a virtual environment (recommended)** section, choose `Conda` tag, rather than `UBUNTU/MAC OS` (choosing this tag won't successfully implement tensorflow in Jupyter notebook). In your shell (it indicates `xxxx:~ hsiang$`), type

`conda create -n <yourenvname> pip python=3.6`

or 

`conda create -n <yourenvname> python=3.6 anaconda`

`<yourenvname>` is any virtual environment name; can be `zoo`, `LSTM_test` and `Boo`, whatever you like. Second way designates using anaconda to set up virtual environment. See [Create virtual environments for python with conda](https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/)

Assume we use `venv` as virtual name, then activate `venv` by
    
`source activate venv`

or 

`conda activate venv`

For example, if you name your virtual environment as `LSTM_test`, after activating the environment, you will see

`(LSTM_test) xxxx:~ hsiang$   `

in your terminal. To quit the mode, just type `source deactivate` or `conda deactivate`.

To view environments and delete, use 

`conda env list`

and 

`conda remove --name <yourenvname> --all`

See [Conda Remove Environment – How to Delete an Env](https://www.freecodecamp.org/news/how-to-delete-an-environment-in-conda/).


### 2. Install TensorFlow package

Within the virtual environment, we also need to install the TensorFlow pip package using its complete URL.

`(LSTM_test) xxxx:~ hsiang$ pip install --ignore-installed --upgrade complete_URL`

For MacOS (CPU-only) and Python 3.6, the above comment will become

`(LSTM_test) xxxx:~ hsiang$ pip install --ignore-installed --upgrade  https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.12.0-py3-none-any.whl`

### 3. Run Pip Install TensorFlow

Choose `VIRTUALENV INSTALL` tag:

`(LSTM_test) xxxx:~ hsiang$ pip install --upgrade tensorflow`

### 4. Pip Install Keras

Within the environment, run

`(LSTM_test) xxxx:~ hsiang$ pip install keras`

to install Keras. Now within the environment, type `jupyter notebook`, you should be able to import tensorflow and keras!


## Access to Github via Teriminal

From August 13, 2021, Github does not support to type password authentication. 
```
(base) hsianghsuanhung@x86_64-apple-darwin13 Statistics % git push 
Password for 'https://<old_token>@github.com': 
remote: Support for password authentication was removed on August 13, 2021.
remote: Please see https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls for information on currently recommended modes of authentication.
fatal: Authentication failed for 'https://github.com/HsiangHung/Machine_Learning_Note.git/'
```

To push code, or update via `git push` in the terminal, we need to go through the token. (refer the stackoverflow page [Password authentication is temporarily disabled as part of a brownout. Please use a personal access token instead [duplicate]](https://stackoverflow.com/questions/68191392/password-authentication-is-temporarily-disabled-as-part-of-a-brownout-please-us/68192584#68192584)):

1. Generate a token from web, if expires or forget. Follow the process: [Creating a fine-grained personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token) and then create a new token on [Personal access tokens (classic)](https://github.com/settings/tokens). A valid token should look `ghp_xxxxx....`
2. Once we have a valid token, we use 

   `git push https://ghp_xxxxxx@github.com/<username>/Machine_Learning_Note.git`

   to push update.