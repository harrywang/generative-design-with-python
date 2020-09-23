# About

This is my attempt of porting the p5.js code of the book ["Generative Design"](http://www.generative-gestaltung.de/2/) to Python 3 using [p5py](https://github.com/p5py/p5).

I use the same folder structure as the official [Github repo of the book](https://github.com/generative-design/Code-Package-p5.js).  
# Setup p5py

- Setup Python 3 and Homebrew on Mac ([check out a tutorial by me](https://medium.com/@HarryWang/how-to-setup-mac-for-python-development-37e5fd895151))
- Run `brew install glfw` to enable p5py dependency on Mac.
- Setup the Python virtual environment and install the packages. 

    ```
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
- Run a sketch using `python 01_P/P_1_0_01/sketch.py`