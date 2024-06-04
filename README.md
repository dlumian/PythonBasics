# Basic Guide to Python Concepts and Tools for Machine Learning

Repo introduces basic Python concepts with to begin mastery of programming, machine learning, and data science concepts.

This guide to Python overviews concepts and tools for machine learning that include environments, packages, scripts, and notebooks. Data science requires more than just Python proficiency, but covering all that is beyond the scope of this project. 

Resources for general DS and programming:
- [Model Training and Evaluation](./Markdowns/ModelEvaluation.md): Terminology and descriptions of core data science training and evaluation of models
- [Supporting Knowledge](#supporting-knowledge): Complimentary skillsets to programming in Python
- [Helpful Tools](./Markdowns/HelpfulTools.md): Tools and knowledge for data science. 

Links to example files, websites, and notebooks will be referenced where available. Many subdirectories in this repo contain additional README files with a deeper dive into specific concepts or examples.

[This brief summary](./Markdowns/DsTopics.md) of data science goals and topics may be informative, if you are new to ML and want a better understanding of what types of analyses exist and their importance. Specializing within the field can improve focus on what concepts to prioritize. 

## Topics
- [Python Basics Repo](#python-basics-repo)
- [Why Python](#why-python-for-machine-learning)
- [Supporting Knowledge](#supporting-knowledge)
- [Packages](#packages)
- [Essential Packages](#essential-packages)
- [Environments](#environments)
- [Workflow Tools](#basic-workflow-tools-scripts-and-notebooks)
- [Scripts](#writing-scripts)
- [Notebooks](#using-notebooks)
- [Effective Programming](#effective-python-programming)
---

## Python Basics Repo
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

This repo is designed to demonstrate key aspects of Python programming and basic data science. This readme provides an overview of key concepts. Additional information on some topics may be found in the `Markdowns` directory. md files include text, links, and code snippets. [Notebooks](#using-notebooks) (.ipynb) files include text, executable code, and data visualizations. [Python scripts](#writing-scripts) (.py) files also contain executable code and may save models and files, but do not display visuals directly.

Details on setting up workflow and running code is found throughout this file. Here is an overview of the directory file structure. Examples are designed to run independently. Therefore, once the appropriate [environment](#environments) is set up and activated, examples may be run in any order. 

### Directory Structure

- ClassificationExamples
  - [iris](./ClassificationExamples/iris/README.md): example workflow classifying 3 species of iris flowers
  - [random_forest_lecture](./ClassificationExamples/random_forest_lecture/random_forest.ipynb): a single notebook with in-depth details on decision trees and random forests. **Good starting point for individuals with programming experience looking for entry into machine learning** 
- Environment
  - README: details on environment installs and management tools
  - environment files: txt and ymls containing required details on Python version and packages 
- LICENSE: Info on using this repository
- Markdowns
  - [DsTopics.md](./Markdowns/DsTopics.md): Briefly summarizes data science concepts and types of analysis
  - [HelpfulTools.md](./Markdowns/HelpfulTools.md): Guide to setting up a workspace with modern tools such as debugging, tests, and Python environments
  - [ModelEvaluation.md](./Markdowns/ModelEvaluation.md): Descriptions of how model training should be conducted and evaluated
  - [PackageImportance.md](./Markdowns/PackageImportance.md): Elaborates on the value and benefits of properly creating modular code and following best practices
- PythonBasics
  - [Basics.ipynb](./PythonBasics/Basics.ipynb): Guide to datatypes and basic Python functionality-helpful for those who may need additional practice before the ML oriented examples
- README.md: This file with an overview of many topics. If new to Python, read the whole file. If experienced, use the [Topics](#topics) section to jump to topics of interest
- RegressionExamples
  - [housing](./RegressionExamples/housing/README.md): regression example using historic housing prices from Boston

### Example Directories
With the goal of consistency, several common directories may be found in example folders. Some examples may be a single notebook, while others contain all the directories listed below.

- clf_results: holds results of multiple runs with metrics and visuals for each
- images: images generated from EDA or analysis
- notebooks: collection of ordered notebooks to run
- README: markdown file with details about that specific example
- src: python scripts which may be imported into notebooks or executed directly

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

Environments, and their management, is essential to successful project collaboration and maintenance. It is vital to document the environment in which a project was made and deployed because Python versions and packages change. Without a record, it is easy to introduce errors and issues into your code. A list of packages and versions can be generated with [Conda](https://www.anaconda.com/) or [pip](https://pypi.org/project/pip/) to help reduce such problems. Multiple Python environments can be stored and activated when needed. See [Environments](./Environment/README.md) for more details.

## Basic Workflow Tools: Scripts and Notebooks

Code can be developed and executed in many different ways. The two primary data science options are scripts and notebooks. 

Choosing between [scripts](#writing-scripts) and [notebooks](#using-notebooks) depends on the task at hand and the stage of your workflow. Here are some guidelines on when to use each:

### Scripts Preferred for:
1. **Production Code**:
   - Scripts are ideal for code that needs to be run in production environments. They can be version-controlled more effectively and integrated into automated workflows.
   - Scripts are easier to test, maintain, and refactor compared to notebooks.

2. **Automation and Reproducibility**:
   - If you need to automate tasks, such as data processing pipelines, scripts are more suitable because they can be scheduled and executed without manual intervention.
   - Scripts are also better for ensuring reproducibility of your workflows.

3. **Complex Projects**:
   - For larger projects with multiple components, scripts (organized into modules and packages) are preferable. They allow for better organization, modularity, and separation of concerns.
   - Using scripts makes it easier to manage dependencies and environment configurations.

4. **Performance**:
   - If you need to optimize performance and reduce overhead, scripts are typically more efficient as they avoid the interactive overhead of notebooks.

### Notebooks Preferred for:
1. **Exploratory Data Analysis (EDA)**:
   - Notebooks are great for EDA because they allow you to iteratively run and refine your code, visualize data, and document insights in a linear, readable manner.
   - The ability to mix code, visualizations, and markdown makes it easy to understand and share your exploratory process.

2. **Data Visualization**:
   - If you are generating plots and visualizations, notebooks allow you to see the results immediately and make adjustments on the fly.

3. **Documentation and Tutorials**:
   - Notebooks are excellent for creating tutorials or documenting workflows because of their readability and interactivity.
   - Combining code with detailed explanations helps others (or future you) understand the thought process and logic behind the code.

4. **Interactive Development**:
   - For tasks where you need to quickly test hypotheses or experiment with different approaches, notebooks provide a flexible environment.

### Hybrid Preferred for:
Sometimes, a project may require both interactive analysis and automated processing. You can use notebooks for the interactive parts (like data exploration and visualization) and scripts for the automated parts (like data cleaning and model training).

1. **Prototyping to Production**:
   - You might start with a notebook for prototyping and exploration. Once the approach is validated, you can refactor the code into scripts for production deployment.
   - This allows you to benefit from the interactive development environment of notebooks while ensuring the robustness and maintainability of scripts.

2. **Comprehensive Reports**:
   - Notebooks can be used to create detailed reports with visualizations and explanations. Scripts can be called within these notebooks to run heavy computations or preprocess data.
   - This combination allows you to maintain clean, well-documented analyses while leveraging the efficiency of scripts for computational tasks.

### Practical Examples:
- **Machine Learning Workflow**:
  - **Notebook**: Initial data exploration, feature engineering, model prototyping, and visualizations.
  - **Script**: Data preprocessing pipeline, model training, evaluation, and deployment.

- **Data Analysis Project**:
  - **Notebook**: EDA, hypothesis testing, and generating visualizations for reports.
  - **Script**: Data extraction, transformation, and loading (ETL) processes, as well as scheduled reports generation.

- **Tutorial Development**:
  - **Notebook**: Creating interactive tutorials with step-by-step explanations and code snippets.
  - **Script**: Including complex functions or utility scripts to keep the notebook concise and focused on the teaching content.

By leveraging the strengths of both scripts and notebooks, you can create a workflow that is both efficient and easy to maintain, while also being adaptable to different stages of your projects.

## Writing Scripts
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

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

## Using Notebooks
[Back to Top](#basic-guide-to-python-concepts-and-tools-for-machine-learning)

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