# Test data-engineer python
## Before starting
 * Fork the project in your namespace
 * Change project visibility (Settings, General, click on `Visibility, project features, permissions` change project visibility from public to private)
## After you push your codes
 * add it@dataimpact.fr as **reporter** in settings, members
 * answer the email with the project link in it 
 
# Test
Some really important tips:
 * Comments and tests are a big plus
 * You might need pytest
 * There are three parts (algorithm, advance, data) you can choose to skip one 
 * You can use internet
 

## First Part (python algorithm)

### Exercise 1
Print every number between 1 and 100 as follows:
For every multiple of 3 print "Three".
For every multiple of 5 print "Five".
And for every multiple of both 3 and 5 print "ThreeFive"

*The output should be as follows:*

```
1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
16
```

### Exercise 2 (15 min)
Find the Missing Number

You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates in the list. One of the integers is missing in the list. Write an efficient code to find the missing integer.

Examples:
```
Input: arr = [1, 2, 3, 6, 4, 7, 8] --> Output: 5

Input: arr = [1, 2, 3, 5] --> Output: 4
```

### Exercise 3 (25 min)
Sort an array without changing position of negative numbers

Given an array arr[] of N integers, the task is to sort the array without changing the position of negative numbers (if any) i.e. the negative numbers need not be sorted.
Examples:

```
Input: arr = [2, -6, -3, 8, 4, 1] --> Output: 1 -6 -3 2 4 8

Input: arr = [-2, -6, -3, -8, 4, 1] --> Output: -2 -6 -3 -8 1 4
```
## Second Part (python advanced)

### Exercise 1 (5 min)

Make the test `test_my_set` work

### Exercise 2 (10 min)

Rewrite decorator_check_max_int to force the function "add" not to return values greater than maxsize

### Exercise 3 (10 min)

Rewrite ignore_exception so that it ignores the exception in its argument and returns None if this exception raises

### Exercise 4 (20 min)

Test the class `CacheDecorator` without touching it, some of your tests may not pass because the class is bugged

### Exercise 5 (10 min)
Write the metaclass MetaInherList like ForceToList inherits from list

### Exercise 6 (15)
create a metaclass that checks if classes have an attribute named 'process' which must be a method taking 3 arguments

## Third Part (data)
*You can use pandas in this part*

### Exercice 1

In the `third_part/data` directory you'll find a compressed json file named "products.json.gz".
That file contains a list of products defined as objects, each product object contains infomation relevant to a specific product.

**An example product object is as follows:**

```json
{  
    "idappcat" : "2076,3B,19C,138D,NULL,NULL",
    "refproduitenseigne" : 364980,
    "libelle" : "Nature bio champignons émincés 230g ",
    "categorieenseigne" : ""
}
```
  1) Read the json file. Parse it and store it a variable called product_list
  2) Write a function called `clean_cat` that can remove the NULL fields of each category
  (*For example when calling clean_cat on "2076,3B,19C,138D,NULL,NULL" the output should be "2076,3B,19C,138D".*)
  3) Apply this function to all products

