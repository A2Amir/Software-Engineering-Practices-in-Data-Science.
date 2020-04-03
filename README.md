# Software Engineering Practices 

 This Repo is about the following practices of software engineering and how they apply in data science.

<b>
 
1.	Writing clean 
 
2.	Writing modular code

3.	Writing efficient code

4.	Code refactoring

5.	Adding meaningful documentation

6.	Using version control

7.	Testing

8.	Logging

9.	Code reviews
</b>

# 1.	Clean Code

The first practice I'll talk about is writing code in a way that is clean and modular. When you're working in industry, your code could potentially be used in production. Production code just means, code that is run on production servers. For example, when you're on your laptop using software products like Google, or Amazon, the code that's running the service you're using is production code. 

Ideally, code that's being used in production should meet a number of criteria to ensure reliability and efficiency before it becomes public. 

**CLEAN means** readable, simple, and concise. A characteristic of production quality code that is crucial for collaboration and maintainability in software development. 

### Writing Clean Code: Meaningful Names

**Tip: Use meaningful names**
* Be descriptive and imply type - E.g. for booleans, you can prefix with is_ or has_ to make it clear it is a condition. You can also use part of speech to imply types, like verbs for functions and nouns for variables.

* Be consistent but clearly differentiate - E.g. age_list and age is easier to differentiate than ages and age. 
* Avoid abbreviations and especially single letters - (Exception: counters and common math variables) Choosing when these exceptions can be determined based on the audience for your code. If you work with other data scientists, certain variables may be common knowledge. While if you work with full stack engineers, it might be necessary to provide more descriptive names in these cases as well. 
* Long names != descriptive names - You should be descriptive, but only with relevant information. E.g. good functions names describe what they do well without including details about implementation or highly specific uses.

Try testing how effective your names are by asking a fellow programmer to guess the purpose of a function or variable based on its name, without looking at your code. Coming up with meaningful names often requires effort to get right.

### Writing Clean Code: Nice Whitespace

**Tip: Use whitespace properly**

* Organize your code with consistent indentation - the standard is to use 4 spaces for each indent. You can make this a default in your text editor.
* Separate sections with blank lines to keep your code well organized and readable.
* Try to limit your lines to around 79 characters, which is the guideline given in the PEP 8 style guide. In many good text editors, there is a setting to display a subtle line that indicates where the 79 character limit is. 

For more guidelines, check out [the code layout section of PEP 8](https://www.python.org/dev/peps/pep-0008/?#code-lay-out).

# 2.	Modular Code

**MODULAR:** logically broken up into functions and modules. An important characteristic of production quality code that makes your code more organized, efficient, and reusable. Modularizing your code or breaking up your code into logical functions and modules really helps you organize your program in cleaner and more efficient.

<p align="right">
<img src="./imgs/1.png" alt="Modular Code"  width="600" height="400"/>
<p align="center">
 
 **MODULE** is a file. Modules allow code to be reused by encapsulating them into files that can be imported into other files.


### Writing Modular Code 
**Tip: DRY (Don't Repeat Yourself)**

Don't repeat yourself! Modularization allows you to reuse parts of your code. Generalize and consolidate repeated code in functions or loops.

**Tip: Abstract out logic to improve readability**

Abstracting out code into a function not only makes it less repetitive, but also improves readability with descriptive function names. Although your code can become more readable when you abstract out logic into functions, it is possible to over-engineer this and have too many modules, so use your judgement. 

**Tip: Minimize the number of entities (functions, classes, modules, etc.)**

There are tradeoffs to having function calls instead of inline logic. If you have broken up your code into an unnecessary amount of functions and modules, you'll have to jump around everywhere if you want to view the implementation details for something that may be too small to be worth it. Creating more modules doesn't necessarily result in effective modularization. 

**Tip: Functions should do one thing**

Each function you write should be focused on doing one thing. If a function is doing multiple things, it becomes more difficult to generalize and reuse. Generally, if there's an "and" in your function name, consider refactoring.

**Tip: Arbitrary variable names can be more effective in certain functions**

Arbitrary variable names in general functions can actually make the code more readable. 

**Tip: Try to use fewer than three arguments per function**

Try to use no more than three arguments when possible. This is not a hard rule and there are times it is more appropriate to use many parameters. But in many cases, it's more effective to use fewer arguments. Remember we are modularizing to simplify our code and make it more efficient to work with. If your function has a lot of parameters, you may want to rethink how you are splitting this up.

# 3.	Refactoring Code

REFACTORING means restructuring your code to improve its internal structure, without changing its external functionality. This gives you a chance to clean and modularize your program after you've got it working.

* Since it isn't easy to write your best code while you're still trying to just get it working, allocating time to do this is essential to producing high quality code. Despite the initial time and effort required, this really pays off by speeding up your development time in the long run.
* You become a much stronger programmer when you're constantly looking to improve your code. The more you refactor, the easier it will be to structure and write good code the first time.

To exercise refactoring check this [notebook](https://github.com/A2Amir/Software-Engineering-Practices-/blob/master/Code/refactor_wine_quality.ipynb).

# 4.	Efficient Code

Knowing how to write code that runs efficiently is another essential skill in software development. Optimizing code to be more efficient can mean making it:

* Execute faster
* Take up less space in memory/storage

The project you're working on would determine which of these is more important to optimize for your company or product. When we are performing lots of different transformations on large amounts of data, this can make orders of magnitudes of difference in performance.
To see a few examples of inefficient code, and practice refactoring to optimize their performance check these exercises below.

* [Optimizing - Common Books](https://github.com/A2Amir/Software-Engineering-Practices-/blob/master/Code/optimizing_code_common_books%20.ipynb)
* [Optimizing - Holiday Gifts](https://github.com/A2Amir/Software-Engineering-Practices-/blob/master/Code/optimizing_code_holiday_gifts.ipynb)

# 5.	Documentation

DOCUMENTATION is additional text or illustrated information that comes with or is embedded in the code of software. It is helpful for clarifying complex parts of code, making your code easier to navigate, and quickly conveying how and why different components of your program are used.

Several types of documentation can be added at different levels of your program:

* In-line Comments - line level
*	Docstrings - module and function level
* Project Documentation - project level

### In-line Comments

In-line comments are text following hash symbols throughout your code. They are used to explain parts of your code, and really help future contributors understand your work.

*	One way comments are used is to document the major steps of complex code to help readers follow. Then, you may not have to understand the code to follow what it does. However, others would argue that this is using comments to justify bad code, and that if code requires comments to follow, it is a sign refactoring is needed.
     
                                        c=a+b # adding two variables (In-line Comment)
                                      
* Comments are valuable for explaining where code cannot. For example, the history behind why a certain method was implemented a specific way. Sometimes an unconventional or seemingly arbitrary approach may be applied because of some obscure external variable causing side effects. These things are difficult to explain with code.

### Docstrings

Docstring, or documentation strings, are valuable pieces of documentation that explain the functionality of any function or module in your code. Ideally, each of your functions should always have a docstring. 
Docstrings are surrounded by triple quotes. The first line of the docstring is a brief explanation of the function's purpose (see example below). 
The next element of a docstring is an explanation of the function's arguments. you list the arguments, state their purpose, and state what types the arguments should be. Finally it is common to provide some description of the output of the function. Every piece of the docstring is optional; however, doc strings are a part of good coding practice.

~~~python

def population_density(population, land_area):
    """Calculate the population density of an area.

    Args:
    population: int. The population of the area
    land_area: int or float. This function is unit-agnostic, if you pass in values in terms of square km or square miles the function will return a density in those units.

    Returns:
    population_density: population/land_area. The population density of a 
    particular area.
    """
    return population / land_area

~~~
Check these links to get more information:
*	[PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/) 
* [NumPy Docstring Guide](https://numpydoc.readthedocs.io/en/latest/format.html)
