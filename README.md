# Basic Guide to Python Concepts and Tools for Machine Learning

Repo introduces basic Python concepts with to begin mastery of programming, machine learning, and data science concepts.

This guide to Python overviews concepts and tools for machine learning that include environments, packages, scripts, and notebooks. 

Links to example files, websites, and notebooks will be referenced where available. Many subdirectories in this repo contain additional README files with a deeper dive into specific concepts or examples.

## Topics
- [Why Python](#why-python-for-machine-learning)
- [Supporting Knowledge](#supporting-knowledge)
- [Packages](#packages)
- [Essential Packages](#essential-packages)
- [Environments](#environments)
- 
- [Effective Programming](#effective-python-programming)
---


## Why Python for Machine Learning?
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

Python is a popular platform for machine learning due to its simplicity, readability, and extensive ecosystem of libraries and frameworks. Its syntax is straightforward, making it accessible for beginners and efficient for experienced programmers. Python’s robust community support and comprehensive documentation further enhance its usability in machine learning projects. Key libraries and packages such as Numpy, Pandas, Scikit-Learn, TensorFlow, and PyTorch provide powerful tools for numerical computations, data manipulation, and model building, streamlining the development process. More on [packages](#packages) found here. 

## Supporting Knowledge
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

To effectively work in Python for machine learning, it’s important to have knowledge of the following tools and concepts:

- **Git and GitHub:**
  - **Git:** A version control system that helps track changes to code, collaborate with others, and manage different versions of a project.
    - **Basic Commands:**
      ```bash
      git init          # Initialize a new repository
      git add .         # Stage changes
      git commit -m "message"  # Commit changes
      git push          # Push changes to a remote repository
      ```
  - **GitHub:** A platform for hosting and managing Git repositories, facilitating collaboration and sharing of code. **NOTE:** Repos can be private or public-therefore, it is important to consider what information is shared in each and with whom.

- **Command Line Interfaces (CLIs):**
  - CLIs allow for efficient navigation and execution of commands on your computer. Familiarity with basic command line operations is essential for tasks such as setting up environments, managing packages, and running scripts.
    - **Basic Commands:**
      ```bash
      ls                # List directory contents
      cd path/to/directory  # Change directory
      mkdir new_directory   # Create a new directory
      ```
    - **NOTE:** Many CLIs exist and may vary for many reasons including operating system. Be sure to find the correct instructions for your workspace. 

---

## Packages
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

A package in Python is a collection of modules organized in directories that provide reusable code and functionality. Packages allow you to structure your Python code logically and systematically, facilitating code management and reuse. They can include various types of files, such as modules (individual Python files), sub-packages (directories with their own `__init__.py` file), and data files.

**Example Structure of a Package:**

```
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        submodule1.py
```

- **`__init__.py`**: Indicates that the directory should be treated as a package.
- **Modules**: Python files (`.py`) containing code, functions, classes, and variables.
- **Sub-packages**: Nested directories with their own `__init__.py` files, further organizing code.

**Using a Package:**

```python
# Importing a module from a package
from mypackage import module1

# Using functions or classes from the imported module
result = module1.my_function()
```

### Package Benefits
There are many benefits to the package organization including sharing, updating, and reproducing analysis. For more details see: [Package Importance](./Markdowns/PackageImportance.md).

Key benefits elaborated on in the file linked above.

- **Code Reusability**
- **Maintainability**
- **Collaboration**
- **Reproducibility**
- **Robustness**


## Essential Packages
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

### [Numpy](https://numpy.org/)
Numpy is a library for numerical computations. Often used not only directly, but also is a dependency for many other libraries. 

- **Creating Arrays:**
  ```python
  import numpy as np
  a = np.array([1, 2, 3])
  ```
- **Array Operations:**
  ```python
  b = np.array([4, 5, 6])
  c = a + b  # array addition
  ```

### [Pandas](pandas.pydata.org)
Pandas is used for data manipulation and analysis. 

A pandas DataFrame holds a two-dimensional data structure that can store data of different types, including:
- Characters
- Integers
- Floating point values
- Categorical data
- Dates and times
- Boolean values

DataFrames are similar to spreadsheets, SQL tables, or the data.frame object in R. They are made up of rows and columns, and each cell can contain a single value. DataFrames are often used to store and analyze data from a variety of sources, such as CSV files, Excel spreadsheets, and SQL databases.

DataFrames can be used to perform a variety of data analysis tasks, such as:
- Filtering and sorting data
- Calculating summary statistics
- Creating visualizations
- Joining and merging dataframes
- Performing machine learning.

- **Creating DataFrames:**
  ```python
  import pandas as pd
  df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
  ```
- **Basic Operations:**
  ```python
  df['C'] = df['A'] + df['B']  # add new column
  ```

### [Scikit-Learn](https://scikit-learn.org/stable/)
Scikit-learn is a machine learning library. It offers a wide variety of analysis options, many of which follow a standard order of operations. Most commonly, the sequence is to instantiate a model, fit a model, and then predict with the model.

Analysis types include:
- Classification
- Regression
- Clustering
- Dimensionality Reduction
- Model Selection
- Data Preprocessing

- **Training a Model:**
  ```python
  from sklearn.linear_model import LinearRegression
  model = LinearRegression()
  model.fit(X_train, y_train)
  ```
- **Making Predictions:**
  ```python
  predictions = model.predict(X_test)
  ```
### [Matplotlib](https://matplotlib.org/)
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is highly customizable and supports a wide range of plots and charts.
- **Key Features:**
  - **2D Plotting:** Line plots, scatter plots, bar charts, histograms, etc.
  - **Customization:** Extensive options for customizing the appearance of plots, including colors, labels, and styles.
  - **Integration:** Can be used with Jupyter Notebooks for interactive visualizations.
- **Example Usage:**
  ```python
  import matplotlib.pyplot as plt

  x = [1, 2, 3, 4, 5]
  y = [10, 20, 25, 30, 40]

  plt.plot(x, y)
  plt.xlabel('X-axis label')
  plt.ylabel('Y-axis label')
  plt.title('Sample Plot')
  plt.show()
  ```

### [Seaborn](https://seaborn.pydata.org/)
Seaborn is a data visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
- **Key Features:**
  - **Statistical Plots:** Supports complex visualizations like violin plots, box plots, pair plots, and heatmaps.
  - **Themes:** Comes with built-in themes for styling Matplotlib graphics.
  - **DataFrames:** Works seamlessly with Pandas DataFrames for data visualization.
- **Example Usage:**
  ```python
  import seaborn as sns
  import matplotlib.pyplot as plt

  # Load sample dataset
  data = sns.load_dataset('iris')

  # Create a pair plot
  sns.pairplot(data, hue='species')
  plt.show()
  ```

### More Advanced Libraries
Python has a large and ever-growing number of resources for machine learning, AI, visualizations, and more.

Additional advanced libraries of interest for data science:
- [Keras](https://keras.io/)
- [PyTorch](https://pytorch.org/)
- [TensorFlow](https://www.tensorflow.org/)
- [XGBoost](https://xgboost.readthedocs.io/en/stable/)
- [LightGBM](https://github.com/microsoft/LightGBM)
- [CatBoost](https://catboost.ai/)
- [Hugging Face Transformers](https://huggingface.co/)
- [FastAI](https://www.fast.ai/)

## Environments
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

Environments, and their management, is essential to successful project collaboration and maintenance. As Python version and packages change, it is vital to document the environment in which a project was made and deployed. Without this record, it is easy to introduce errors and issues into your code. A list of packages and versions can be generated with [Conda](https://www.anaconda.com/) or [pip](https://pypi.org/project/pip/) to help reduce such problems. Multiple Python environments can be stored and activated when needed. See [Environments](./Environment/README.md) for more details.



## 3. Writing Scripts

Scripts are Python files (.py) that contain code to be executed.

- **Basic Structure:**
  ```python
  # myscript.py
  import numpy as np
  import pandas as pd

  def main():
      df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
      df['C'] = df['A'] + df['B']
      print(df)

  if __name__ == "__main__":
      main()
  ```
- **Running a Script:**
  ```bash
  python myscript.py
  ```

## 4. Using Notebooks

Notebooks, such as Jupyter Notebooks, allow for interactive code execution and visualization.

- **Installing Jupyter:**
  ```bash
  conda install jupyter
  # or
  pip install jupyter
  ```
- **Starting a Notebook:**
  ```bash
  jupyter notebook
  ```
- **Basic Operations in a Notebook:**
  ```python
  import numpy as np
  import pandas as pd
  import matplotlib.pyplot as plt

  # Create data
  x = np.linspace(0, 10, 100)
  y = np.sin(x)

  # Plot data
  plt.plot(x, y)
  plt.show()
  ```

---

## Effective Python Programming
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

To maximize efficiency, data scientists not only rely on packages and libraries, but must also customize their workflow and tools. A myriad of tools exist for text editing, debugging, optimization, and testing. Available features include color syntax highlighting, color themes, testing frameworks, and documentation standards.

I highly encourage taking the time to invest in researching, selecting, and fine-tuning your work tools and flows. This investment will save many hours down the road by providing a positive workspace and on-the-go feedback.

A concise list of options with brief descriptions is in [HelpfulTools](./Markdowns/HelpfulTools.md).