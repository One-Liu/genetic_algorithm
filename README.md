# ABOUT
* This mini-project contains a general genetic algorithm that supports changing the configuration of some of its attributes. In the next diagram we can see the algorithm process.

![Genetic algorithm process](https://github.com/user-attachments/assets/b1f1e88a-7e34-4d1e-bb97-ae19d79f11bf)

* The evaluation.py file contains the problem that has the fitness function. In this case, the implemented problem is the Triangle Classification. The Triangle Classification problem involves determining the type of a triangle based on its side lengths.
* You can change the way the solutions are being evaluated in the evaluation.py file. The method score() defined in the parent class Evaluation is considered to be the method where the fitness of the solution is given.
* As we can observe in the class diagram, the Factory Method pattern design was used almost everywhere, so you can add more evaluations/problems or types of gen, selections and so on without too much trouble.

![Class diagram](https://github.com/user-attachments/assets/fec30070-32be-4e29-a228-cc384e91a787)

# How to run the program (Windows)
1. Create and activate a virtual environment (optional).
```
py -m venv .venv
.venv\Scripts\activate
```
2. Install the requirements specified in the requirements.txt file.
```
py -m pip install -r requirements.txt
```
3. Execute the main.py file.
```
py main.py
```

If you're using other OS or you're having trouble with the first two steps, this [link](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) might help you out.

Feel free to take inspiration from this code to create your own Genetic Algorithm applied to your problem!\
I'll be grateful if you reference this project.
