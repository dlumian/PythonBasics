# Python Environment Setup Guide

This guide will help you set up a Python environment using either conda and pip. 

Environment management ensures projects run smoothly and work across different systems.

Environments control language versions, dependencies, and dependency versions.

It is best practice to create a new environment for each project. This helps avoid dependency conflicts and makes each project more reproducible and manageable.

Key Sections:
- [Conda Envs](#conda-envs)
- [Pip Envs](#pip-envs)
- [Versioning](#version-naming-conventions)
- [Warngings](#warnings)
- [Tips](#additional-tips)

## Conda Envs
[Back to Top](#python-environment-setup-guide)
### What is Conda?
Conda is an open-source package management and environment management system that runs on Windows, macOS, and Linux. Conda quickly installs, runs, and updates packages and their dependencies.

### Setting Up an Environment with Conda
1. Install Anaconda or Miniconda:

    - [Anaconda](https://www.anaconda.com/) includes conda and many scientific packages.
    - [Miniconda](https://docs.anaconda.com/free/miniconda/) includes only conda and its dependencies.

1. Create a New Environment:

    ```conda create --name myenv python=3.8```
    
    Replace `myenv` with your desired environment name and `3.8` with the Python version you need.

1. Activate the Environment:

    ```conda activate myenv```

1. Install Packages:

    You can install packages individually or use a .yml file to install multiple packages at once.

    - Individual Packages:

        ```conda install numpy pandas```

    - Using a .yml File:

        See `environment.yml` file in this directory.

        Example file structure:

        ```yaml
        name: myenv
        channels:
            - defaults
        dependencies:
            - python=3.8
            - numpy
            - pandas
            - pip
            - pip:
                - some_pip_package
        ```

        Create the environment with:

        ```conda env create -f environment.yml```

1. Deactivate the Environment:

    ```conda deactivate```

1. Remove an Environment:

    ```conda remove --name myenv --all```

## Pip Envs
[Back to Top](#python-environment-setup-guide)
### What is Pip?
Pip is the package installer for Python. You can use pip to install packages from the Python Package Index (PyPI) and other indexes.

### Setting Up an Environment with Pip
1. Install Virtualenv:

    ```pip install virtualenv```

1. Create a New Environment:

    ```virtualenv myenv```

    Replace `myenv` with your desired environment name.

1. Activate the Environment:

    Windows:

    ```myenv\Scripts\activate```

    macOS/Linux:

    ```source myenv/bin/activate```

1. Install Packages:

    You can install packages individually or use a `requirements.txt` file to install multiple packages at once.

    - Individual Packages:

        ```pip install numpy pandas```

    - Using a `requirements.txt` file:

        See `requirements.txt` file in this directory.

        Example file structure:
        
        ```txt
        numpy
        pandas
        ```

        Then, install the packages with:

        ```pip install -r requirements.txt```

1. Deactivate the Environment:

    ```deactivate```

1. Remove an Environment:
    Use a file tool to locate the environment folder and move it to `Trash`.

## Version Naming Conventions
[Back to Top](#python-environment-setup-guide)

Many packages are updated or abandoned across time. Therefore, naming conventions for packages include a numeric indicator of release version. The standard convetion for this is to use "major.minor.micro".

When specifying package versions, it's important to understand version naming conventions to avoid compatibility issues:

- ### Exact Version:

    ```numpy==1.19.2```

- ### Minimum Version:

    ```numpy>=1.19.2```

- ### Version Range:

    ```numpy>=1.19.2,<1.20.0```

- ### Any Version:

    ```numpy```


## Warnings: 
[Back to Top](#python-environment-setup-guide)

This section highlights common issues when good environment habits are not followed or understood. 

### Breaking Changes
Newer versions of packages may introduce changes that are not compatible with your code. Always test your code after updating packages.

### Incompatible Version Errors
Some packages may have dependencies that require specific versions of other packages. Installing incompatible versions can lead to errors.
To mitigate these issues, consider using the exact versions of packages that you have tested and know to work with your project.

## Additional Tips
[Back to Top](#python-environment-setup-guide)

- Listing Installed Packages:

    - Conda:
    
        ```conda list```

    - Pip:

        ```pip list```

- Exporting Environment:

    - Conda:

        ```conda env export --no-builds > environment.yml```

    - Pip:

        ```pip list format=freeze > requirements.txt```
