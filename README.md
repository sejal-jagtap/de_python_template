# de_python_template
Python Project Template for Data Engineering System (IDS 706):

1. Setup 

--> Clone Repository: (cmd)

    git clone https://github.com/sejal-jagtap/de_python_template.git
    cd de_python_template

--> Create and activate virtual environment: (cmd)

    python -m venv .de_python_template
    .\.de_python_template\Scripts\activate

Note: For macOS/Linux users:

    python3 -m venv .de_python_template
    source .de_python_template/bin/activate

--> Upgrade pip and install dependencies: (cmd)
 
    python -m pip install --upgrade pip
    pip install -r requirements.txt

2. How to use code

Code is written in hello.py
Functions in hello.py: say_hello(), add(), subtract()

    from hello import say_hello, add, subtract

    print(say_hello("Sejal")) #function used to greet the user
    print(add(6, 2))          #function used to add two numbers eg 6+2 =8
    print(subtract(6, 3))     #function used to subtract two numbers eg. 6-3 =3

--> Expected Output:
Hello, Sejal, welcome to Data Engineering Systems (IDS 706)!
8
3

3. Testing

Tests are written in test_hello.py

--> Command to run all tests: (cmd)

    make test

--> Command to run individual test file: (cmd)

    python -m pytest -vv test_hello.py

4. Make file commands (cmd)
    make install     #Installs dependencies
    make test        #Runs pytest
    make lint        #Runs flake8
    make format      #Formats code with black
    make clean       #Cleans cache and coverage files

5. CI/CD

--> This repository uses GitHub Actions to automate testing and linting on every push or pull request.
--> Workflow runs include:
    Install dependencies
    Lint with flake8
    Run pytest with coverage
--> Workflow: https://github.com/sejal-jagtap/de_python_template/blob/main/.github/workflows/main.yml

6. Additional Notes

--> Always activate your virtual environment before running commands or tests.
--> VS Code users: set the interpreter to .de_python_template for auto-activation.
--> Optional: macOS/Linux users may need to adjust activate paths (source .de_python_template/bin/activate).