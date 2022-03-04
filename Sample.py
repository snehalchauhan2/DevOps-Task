# =======================================================
# CODE BY SNEHAL CHAUHAN:
# PERFORMING SAMPLE TASKS IDS
# TASK LINK : https://github.com/revieve/devops-interview
# EMAIL : SNEHALCHAUHAN.DEV@GMAIL.COM
# PHONE NUMBER : +91 8160673087

# INSTALL PANDAS PACKAGE USING pip install pandas
# run using command python Sample.py  
# =======================================================


import pandas as pd
import re

df_allcustomers = pd.read_csv('customers.csv')
df_allorders = pd.read_csv('orders.csv')
df_allproducts = pd.read_csv('products.csv')



print('============================')
print("PERFORMING TASK 1 ")
try: 
    # CREATING NEW DATAFRAME WITH ID AND EUROS
    df_orderprices = pd.DataFrame(columns=['id', 'euros'])

    # LOOPING THROUGH ALL IDS
    for ind_order in df_allorders.index:

        product_ids = re.sub("[ ]", ",", df_allorders['products'][ind_order])
       
        # FILTER PRODUCTS MATCHING ORDER PRODUCTS
        df_filter_products = df_allproducts.query('id in ['+product_ids+']',inplace=False) 
        new_row = {'id':df_allorders['id'][ind_order].astype(int), 'euros':df_filter_products['cost'].sum()}
        
        # STOER PRODUCT PRICES
        df_orderprices = df_orderprices.append(new_row, ignore_index=True)


    df_orderprices.to_csv('order_prices.csv')
except:
  print("An exception occurred")
else: 
    print("order_prices.csv generated successfully")
    print('TASK 1 COMPLETED')
    print('============================')


print("PERFORMING TASK 2 ")
try: 
    # CREATING NEW DATAFRAME
    df_productcustomers = pd.DataFrame(columns=['id', 'customer_ids'])

    # LOOPING THROUGH PRODUCTS
    for ind_product in df_allproducts.index:
        all_customers = []
        product_id = df_allproducts['id'][ind_product]
        # LOOPING THROUGH ORDERS 
        for ind_order in df_allorders.index:       
            products  = df_allorders['products'][ind_order].split(' ')

            #CHECKING IF PRODUCT EXIST
            if(product_id.astype(str) in products):
                all_customers.append(df_allorders['customer'][ind_order].astype(str))


        new_row = {'id':product_id, 'customer_ids': ' '.join(all_customers)}
        
        df_productcustomers = df_productcustomers.append(new_row, ignore_index=True)
    
    df_productcustomers.to_csv('product_customers.csv')
except:
  print("An exception occurred")
else: 
    print("product_customers.csv generated successfully")
    print('TASK 2 COMPLETED')
    print('============================')


print("PERFORMING TASK 3 ")


try: 
    # CREATE NEW DATASET 
    df_productcustomers = pd.DataFrame(columns=['id', 'firstname','lastname','total_euros'])

    # LOOPING THROUGH CUSTOMERS
    for ind_customer in df_allcustomers.index:
        # OPENING ORDER PRICE TABLE FOR READ WHICH IS CREATED EARLIER STORING SUM OR ORDER PRICE 
        df_orderprices_read = pd.read_csv('order_prices.csv')
        customer_id = df_allcustomers['id'][ind_customer]
        
        #FETCHIN ALL ORDERS FOR CUSTOMER  
        sub_df_allorders = df_allorders[df_allorders['customer'] == customer_id]
        comma_seperated_order = ','.join([str(i) for i in sub_df_allorders['id']])

        # FETCHING ALL PRICES FOR CUSTOMER 
        df_orderprices_read.query('id in ['+comma_seperated_order+']',inplace=True)
        new_row = {'id':customer_id, 'firstname':df_allcustomers['firstname'][ind_customer], 'lastname':df_allcustomers['lastname'][ind_customer],'total_euros':df_orderprices_read['euros'].sum() }
        df_productcustomers = df_productcustomers.append(new_row, ignore_index=True)

    df_productcustomers.to_csv('customer_ranking.csv')
except Exception as e: 
    print(e)
else: 
    print("customer_ranking.csv generated successfully")
    print('TASK 3 COMPLETED')
    print('============================')
