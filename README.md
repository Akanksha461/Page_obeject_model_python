# Introducing page object model
Creating Selenium test cases can result in an unmaintainable project. One of the reasons is that too many duplicated code is used. Duplicated code could be caused by duplicated functionality and this will result in duplicated usage of locators. The disadvantage of duplicated code is that the project is less maintainable. If some locator will change, you have to walk through the whole test code to adjust locators where necessary. By using the page object model we can make non-brittle test code and reduce or eliminate duplicate test code. Beside of that it improves the readability and allows us to create interactive documentation. Last but not least, we can create tests with less keystroke. An implementation of the page object model can be achieved by separating the abstraction of the test object and the test scripts.

![Image of POM](https://i2.wp.com/www.softwaretestingmaterial.com/wp-content/uploads/2017/10/Page-Object-Model-Framework.png?ssl=1)

## Advantanges of page object model
* code reusabity
* Code maintainability
* Object Repository 
* Readability
* Efficient & Scalable

## Disadvantages of page object model
* High Setup Time & Effort
* Skilled labor
* Specific

## Overall Project structure:
The overall project structure should look like this now:

The files we should be interested in at this point are:

1. [Base.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/base.py)
    base file defines all the basic function of selnium which is used in this project. 
1. [locators.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/locators.py)
    locator file defines all the locators used in this project.
1. [pages.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/pages.py)
    Page file defines all the functions used in testpages according to page.
1. [testCases.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/testCases.py)
    From the name itself it is cleared that this file defines all the testcase which is implemented.
1. [testpages.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/testPages.py)
    This is the main file by executing this file all the test script will run accordingly defined in testcases.
1. [users.py](https://github.com/Akanksha461/Page_obeject_model_python/blob/master/users.py)
    User file defines all the credentials of user. like login etc.
    
### How to execute
```
type the below command
python3 <testpages.py> 

```
