The majority of the code is in the `project.ipynb` file, which requires jupyter notebook to run.
It can be installed using pip with the following command:

```pip install notebook```

The notebook should then be started from a terminal in the folder containing `project.ipynb`.
This can be done with the command

```jupyter notebook```

which will open the browser interface and allow opening and interacting with the notebook.

Library requirements:
qiskit latest version
qiskit-machine-learning
cvxpy
joblib
matplotlib>=3.4
symengine

Visual Studio build tools must be installed to successfully install the libraries. They are around 100MB
and can be installed without installing the Visual Studio IDE by running the installer from the below link and
not selecting any extra components when allowed.

https://visualstudio.microsoft.com/visual-cpp-build-tools/

Note that open terminals must be restarted after install to be able use the build tools.

These can be installed with the following command:

```pip install qiskit qiskit-machine-learning cvxpy joblib matplotlib>=3.4 symengine```

Python 3 is required and the code was tested using python version 3.8.3.
