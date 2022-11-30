# RL use case identification

Welcome to the RL use case identification workshop by appliedAI and Zeiss! In this archive you will find two notebooks that will be used during the workshop as well as some accompanying code.

Executing the second notebook will take some time because RL agents are trained there. You might want to execute it once entirely before the presentation (if you don't, it is completely fine). In case you execute the notebook on colab, make sure to download the created `logs` and `sac_*` directories to persist them on your computer, as the will be removed when you restart the colab session. You can then upload them to new colab sessions, load the models and view the logs without having to retrain.  

## Local setup

For a local setup install the requirements (into a virtual environment of your choice), start jupyter and open the notebooks. To enable training on a GPU, please follow the [torch installation instructions](https://pytorch.org/get-started/locally/) for your system. 

*Note*1: Some requirements for a local install might be missing. If you run into missing packages, just install them and restart the kernel.

*Note2*: On Windows one may run into issues when using the tensorboard widget within a notebook. You could try the comand from [this discussion](https://github.com/tensorflow/tensorboard/issues/2481) to fix it.

## Colab based setup

The notebooks have been designed to run smootly on [google colab](https://colab.research.google.com/), you can access it for free with a google account and even use GPUs there. In fact, training on colab runs significantly faster than on a windows laptop with a GPU (not tested on ubuntu)... For a colab based setup do the following:

1. Start a colab session by uploading one of the notebooks. For the notebook titled *Part 2* we recommend using a GPU-enabled runtime.
2. Upload the three files `requirements.txt`, `visualization.py` and `clockwise.png` to colab. Use the directory symbol on the left hand side to access the file-upload button.
3. You will need to repeat this process for each notebook you open.

That's it, after uploading the files everything should run smoothly

