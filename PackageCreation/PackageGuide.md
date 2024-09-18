# Python Packages

## **Importance**

1. **Reusability**:
   - Packages allow developers to encapsulate functionality in reusable modules.
   - Once packaged, code can be imported and used across multiple projects without rewriting.
   - Example: A utility package for data manipulation can be reused in various data science projects.

2. **Maintainability**:
   - By organizing code into packages, it's easier to manage, update, and fix bugs.
   - Modifications in a well-structured package can be reflected in all projects that depend on it.
   - Separate components of a large system can be independently maintained within packages.

3. **Collaboration**:
   - Packages make it easier for teams to work together, as code is modular and shareable.
   - Versioning ensures collaborators use consistent versions, minimizing conflicts.
   - A package hosted on platforms like GitHub or PyPI enables wider access and contribution from others.

4. **Distribution**:
   - Packaging allows easy distribution of software to users.
   - Public repositories like PyPI enable anyone to install the package with a simple command (`pip install`).
   - This accelerates adoption and makes libraries and tools available to the entire Python community.

5. **Encapsulation**:
   - Packages encapsulate specific functionalities and keep project codebases clean and modular.
   - Encapsulation helps with code separation and prevents functions from different areas from conflicting with each other.

## **Pros and Cons of GitHub vs PyPI for Package Management**

### **GitHub** (Source Code Hosting & Development)

**Pros**:
- **Collaboration & Open Development**: GitHub is built for collaborative development, version control, and tracking issues. It's ideal for open-source projects or collaboration within teams.
- **Pull Requests and Contributions**: GitHub allows contributors to submit changes via pull requests, making it easy to manage external contributions.
- **Version Control**: GitHub offers a full version history of the package, making it easier to track changes and revert if necessary.
- **Continuous Integration (CI)**: Integration with CI/CD tools (e.g., GitHub Actions) makes it easy to test the package on different environments.
- **Documentation**: GitHub repositories can include detailed documentation, README files, and examples, making it user-friendly for developers.

**Cons**:
- **Manual Installation**: Users have to clone or download the repo and install it manually with `pip install -e .`, which is less convenient than `pip install` from PyPI.
- **No Built-in Package Distribution**: GitHub is primarily for source code hosting, not distribution. You need external tools (like `twine`) to upload your package to PyPI.
- **Not Suitable for Wide Distribution**: GitHub is not meant for the widespread distribution of packages to the Python community, and package discoverability is lower compared to PyPI.

### **PyPI** (Python Package Index – Distribution Platform)

**Pros**:
- **Easy Installation**: PyPI makes it simple for users to install packages with a single command: `pip install package-name`.
- **Widespread Distribution**: PyPI is the standard repository for Python packages, making your package discoverable and easily accessible to the Python community.
- **Versioning and Dependencies**: PyPI supports versioning and automatic resolution of dependencies, ensuring users get the right version of the package and its dependencies.
- **Standard Platform for Packages**: Being the main distribution platform, PyPI integrates well with `pip`, which is widely used in Python environments.

**Cons**:
- **No Collaboration Features**: Unlike GitHub, PyPI is purely for distribution and doesn’t have built-in features for collaboration, such as pull requests or issue tracking.
- **More Rigid Requirements**: PyPI has more stringent packaging requirements (e.g., correct metadata, versioning, documentation) that need to be met before uploading a package.
- **No Source Control**: While PyPI hosts packages, it doesn’t include features like version control, CI/CD, or source code browsing.
- **Manual Process for Updates**: Every new version needs to be built and uploaded manually or via CI/CD to PyPI.


### **Summary**:
- **GitHub**: Best for development, collaboration, and version control during the package creation process.
- **PyPI**: Best for distributing stable versions of a package to a broad audience for easy installation and use.

Both platforms serve complementary roles: **GitHub** is ideal for package development and collaboration, while **PyPI** is essential for distribution to the broader Python community.

# Step-by-step Guide

Here’s a step-by-step process for testing a Python package from GitHub, Test PyPI, and then publishing it to the official PyPI:

### 1. **Testing the package from GitHub**
This step helps ensure that the package works correctly directly from your repository before moving to PyPI.

1. **Clone or pull your repository** to ensure it's up-to-date:
   ```bash
   git clone https://github.com/yourusername/your-package.git
   # or
   git pull origin main
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install the package from the local directory**:
   ```bash
   pip install -e .
   ```

   The `-e` flag installs the package in "editable" mode, meaning any changes made to the source code will be reflected without reinstalling.

4. **Run your tests** (make sure you have a test suite set up using `pytest`, `unittest`, etc.):
   ```bash
   pytest
   ```

5. **Fix issues** if any tests fail.

## 2. **Testing the package with Test PyPI**

Test PyPI allows you to test the package distribution process without affecting the official PyPI repository. 

1. **Ensure your package files are ready**:
   Ensure your package has a `setup.py` and other necessary files (README, LICENSE, etc.).

2. **Build the package**:
   Two options presented for building.

   #### Traditional Approach (Without `build`)
   In the traditional approach, you would directly use `setup.py` for building and uploading packages like this:

   ```bash
   python setup.py sdist bdist_wheel
   ```
   This command generates both source distributions (`sdist`) and built distributions (`bdist_wheel`), which will be stored in the `dist/` folder.

   #### Modern Approach (With `build`)
   The `build` tool simplifies the building process by automating both the source and wheel building. Here’s how it works:

   **Install `build`**:
   If you haven't used it before, you'll need to install it:
   ```bash
   pip install build
   ```

   **Build the package**:
   From the directory containing your `setup.py` or `pyproject.toml` run:
   ```bash
   python -m build
   ```
   This command works in the current directory and looks for a `setup.py` or `pyproject.toml` file to build the package.

3. **Upload to Test PyPI**:
   - Use `twine` to upload to Test PyPI, which is a separate instance of PyPI for testing purposes:
     ```bash
     twine upload --repository testpypi dist/*
     ```

   - You will need to use your **Test PyPI** credentials.

5. **Install the package from Test PyPI** to test:
   - First, uninstall the package if it’s already installed:
     ```bash
     pip uninstall your-package
     ```

   - Install from Test PyPI:
     ```bash
     pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple your-package
     ```
   **NOTE:** Test Pypi will show pip install command on landing page for the project. Can use that to test install as it is the one that will be publically available. 

6. **Test your package**:
   After installation, test that your package works as expected.

### 3. **Publishing the package to PyPI**

Once you've confirmed everything works on Test PyPI, you can proceed to upload the package to the official PyPI repository.

1. **Check your version number**:
   Ensure the version in `setup.py` or `pyproject.toml` is incremented from any previous versions. PyPI does not allow overwriting the same version.

2. **Upload to PyPI**:
   - Use `twine` to upload the distribution files to the official PyPI repository:
     ```bash
     twine upload dist/*
     ```

   - You will need to use your **PyPI** credentials.

3. **Install the package from PyPI** (after uploading):
   - First, uninstall any previous versions of the package:
     ```bash
     pip uninstall your-package
     ```

   - Then, install the package from PyPI:
     ```bash
     pip install your-package
     ```

4. **Test the final package**:
   Test it in a clean environment or virtual environment to make sure the installation and functionality are working as expected.

---

### Summary of Steps:
1. **GitHub**: Clone the repo, install locally with `pip install -e .`, and run your tests.
2. **Test PyPI**: Build the package, upload to Test PyPI, and install from Test PyPI for final testing.
3. **PyPI**: Once everything works, upload the package to the official PyPI and test it by installing from PyPI.

This ensures the package works at each stage before it’s published for the wider Python community.