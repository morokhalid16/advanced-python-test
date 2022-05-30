#import something if needed
from tkinter.tix import COLUMN
import pandas as pd
import gzip
# exercise 1
#q1
product_list = pd.read_json('data/products.json.gz')
#q2
def clean_cat():
    pattern = '|'.join(['NULL,', ',NULL'])
    product_list["idappcat"] = product_list["idappcat"].str.replace(pattern, "")
    print(product_list["idappcat"].sample(3))
    return 0


# exercise 2 
def import_raw_data():
    # todo exercise 2
    df_17_10 = pd.read_csv('data/17-10-2018.3880.gz', compression='gzip', header=0, sep=';')
    df_18_10 = pd.read_csv('data/18-10-2018.3880.gz', compression='gzip', header=0, sep=';')
    back_office = pd.read_csv('data/back_office.csv.gz')
    return df_17_10, df_18_10, back_office


def process_data():
    # todo exercise 2
    df_17_10, df_18_10, back_office = import_raw_data()
    df = pd.concat([df_17_10, df_18_10])
    df['identifiantproduit'] = df['identifiantproduit'].astype(str)
    df = df.merge(back_office, left_on="identifiantproduit" , right_on='pe_ref_in_enseigne')
    
    return df


def average_prices():
    # todo exercise 3
    df = process_data()
    price_by_product = df.groupby('identifiantproduit').agg({'prixproduit':'mean'})
    price_by_product = price_by_product.rename(columns={"prixproduit": "prix moyen"})
    price_by_product.to_csv('data/average_price.csv')
    return price_by_product


def count_products_by_categories_by_day():
    # todo exercise 4
    df = process_data()
    nbr_categories_by_day = df.groupby(['p_id_cat', 'categorieenseigne']).agg({'prixproduit':lambda x : x.count() / 2}) # car data sur 2 jours
    print(nbr_categories_by_day) 
    return nbr_categories_by_day 


def average_products_by_categories():
    # todo exercise 4
    df = process_data()
    nbr_categories_by_day = df.groupby(['p_id_cat', 'categorieenseigne']).agg({'prixproduit':lambda x : x.count()}) # le nombre pendant les 2 jours
    print(nbr_categories_by_day)  
    return nbr_categories_by_day


if __name__ == '__main__':
   
    count_products_by_categories_by_day()
    average_products_by_categories()
   
    
