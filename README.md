# Test data-engineer python
## Before starting
 * Fork the project in your namespace
 * **Caution! very important:** Change project visibility (Settings, General, click on `Visibility, project features, permissions` change project visibility from public to private)
## After pushing your codes
 * Add it@dataimpact.fr as **reporter** in `settings, members`
 * Answer the email with your project link in it 
 
# Test
Some really important tips:
 * Comments and tests are a big plus
 * You might need pytest (and you can use any other package)
 * There are three parts (algorithm, advanced, data) you can choose to skip one.
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

Rewrite `ignore_exception` so that it ignores the exception in its argument and returns None if this exception raises

### Exercise 4 (20 min)

Write the tests for the class `CacheDecorator` without touching it, some of your tests should not pass because this class is a little buggy. 

### Exercise 5 (10 min)

Write the metaclass `MetaInherList` so that the class `ForceToList` inherits from `list` built-in. (read `test_meta_list` in the tests for more information)

### Exercise 6 (15 min)
create a metaclass that checks if classes have an attribute named 'process' which must be a method taking 3 arguments

## Third Part (data)
*You can use pandas in this part*

### Exercice 1 (15 min)

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
  1) Read the json file. Parse it and store it in a variable called product_list
  2) Write a function called `clean_cat` that can remove the NULL fields of each category
  (*For example when calling clean_cat on "2076,3B,19C,138D,NULL,NULL" the output should be "2076,3B,19C,138D".*)
  3) Apply this function to all products

## Exercise 2 (35 min)
+    **The files are located in third_part/data**
+    **There are two shops' data and one file with an extract of our asset data repository**


1) Import raw data from shops

|refenseigne|refmagasin|categorieenseigne|prixproduit|prixunitaireproduit|prixproduitsansreduction|identifiantproduit|promotion|promotiontexte|ean|position|disponible|nouveau|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|8|3880|"Offres spéciales|Promotions"|5.85|0.15|9.75|85061|1|Réduction immédiate de 40%|NaN|1|NaN|NaN|
|8|3880|"Offres spéciales|Promotions"|2.17|9.77|4.35|51605|1|Réduction immédiate de 50%|NaN|2|NaN|NaN|
|8|3880|"Offres spéciales|Promotions"|5.80|11.60|5.80|61289|1|Le 3ème est gratuit, profitez-en !|NaN|3|NaN|NaN|
|8|3880|"Offres spéciales|Promotions"|5.80|11.60|5.80|78386|1|Le 3ème est gratuit, profitez-en !|NaN|4|NaN|NaN|
|8|3880|"Offres spéciales|Promotions"|2.32|4.64|4.65|3700|1|Réduction immédiate de 50%|NaN|5|NaN|NaN|

+ **refenseigne => Retailer's id**
+ **refmagasin => Shop's id**
+ **categorieenseigne => Retailer's products' categorization - Category where the product was scrapped**
+ **prixproduit => Product price in the shop**
+ **prixunitaireproduit => Unit price of the product in the shop** - Useless in the test
+ **prixproduitsansreduction => Price of the product in the shop whithout discount** - Useless in the test
+ **identifiantproduit => Product's id in the shops**
+ **promotion => Dataimpact's promotion id** - Useless in the test
+ **promotiontexte => Product's promotional text in the shop** - Useless in the test
+ **ean => Product's EAN** - Useless in the test
+ **position => Product's position on the scrapped page** - Useless in the test
+ **disponible => Product's availability** - Useless in the test
+ **nouveau => Has the product been scrapped on the "New products" page of the shops** - Useless in the test

2) Import our asset data repository

|pe_ref_in_enseigne | pe_id | p_id_cat|
|---|---|---|
|35143 | 400479 | 1481E|
|7428 | 413257 | 116D|
|19197 | 413258 |1318E|
|6420 | 413259 | 2003E|
|24668 | 413260 | 253D|

+ **pe_ref_in_enseigne => Products id in the shops**
+ **pe_id => Dataimpact's products id**
+ **p_id_cat => Dataimpact's products' categorization's id**

3) Merge the data from the shops with the data from our asset data repository. (write the `import_raw_data` and `process_data` functions)

## Exercise 3 (15 min)
Average the prices of the products from the two days of the shop you processed. (write the `average_prices` function)

    The resulting file should be a CSV with the id of the products in one column and the price average in another one


## Exercise 4 (15 min)
Count how many products there is in each Dataimpact's category and each retailer's category by day. (write the `count_products_by_categories_by_day` function)
Average the numbers of products by Dataimpact's category and by retailer's category on both days. (write the `average_products_by_categories` function)


