Software requirements:
Python 3 is required and the code was tested using python version 3.8.3.
Jupyter Notebook

Library requirements:
qiskit
qiskit-machine-learning
cvxpy
joblib
matplotlib>=3.4 (minimum version required for drawing normalized bar graphs)
symengine

The simplest way to install all dependencies is to follow these steps:
1. Download Anaconda individual edition https://www.anaconda.com/products/individual. Make sure to tick the box to add it to the PATH environment variable. This installation includes the Jupyter Notebook requirement and python 3 requirement.
2. Add the `conda-forge` channel to conda sources with ```conda config --add channels conda-forge```
3. Run the command ```conda install cvxpy joblib matplotlib>=3.4 symengine```
4. Run the commmand  ```pip install qiskit qiskit-machine-learning```

Alternative installations:
Jupyter notebook can alternatively be installed using pip with the following command, assuming pip is installed: ```pip install notebook```
The `conda` libraries can also be installed through pip but require Visual Studio to be installed.

Instructions to run:
The notebook can be started from a terminal in the folder containing `project.ipynb`.
This can be done with the command
```jupyter notebook```
which will open the browser interface and allow opening and interacting with the notebook.
