#### <p align="center">The project is currently in the development phase, and new features are being added!</p>
---

# SHOP SERVICE

The project takes data from a json file. Then from the console we have the ability to manage orders.
Project written in learning Python, text files, data management, data validation and testing. 

I plan to add a database layer and UI (FastAPI, Flask).


## Built With
- Python
- Pytest
- Unittest
- Poetry
- MySQL
- Docker


## Getting Started
1. Clone the repo

   ```sh
   git clone https://github.com/SzymiYay/easy-shop-app-2
   ```
2. To start the project, you need to have Python and Poetry installed on your computer.
3. Set on the project directory.
4. Run application:

   ```sh
   poetry run pyhton -m shop_app
   ```
5. Run tests:

   ```sh
   pytest
   ```
   
## Usage
Example TXT:
```txt
JAN;Kowal;20;2000;124
Adam;Nowak;40;5000;4253
Joanna;Drwal;23;1500;21
```
```txt
P((hone;3;2100;ELECTRONICS
TV;2;1100;ELECTRONICS
Washing Machine;4;400;ELECTRONICS
Earphones;3;140;ELECTRONICS
Tablet;3;800;ELECTRONICS
Tomato;200;5;GROCERIES
```


From the text file, get the data. Then, using the get_orders function to validate the data, 
place it in an array and create a CarsService object.
Having such an object, you can manage the data in various ways.

```python
def main() -> None:
   CUSTOMERS_PATH: Final = 'shop_app/data/customers.txt'
   PRODUCTS_PATH: Final = 'shop_app/data/products.txt'

   customers = get_customers_data(CUSTOMERS_PATH)
   products = get_products_data(PRODUCTS_PATH)

    om = OrdersManager(customers, products)
    ss = ShopService(om._get_customers_and_products())
    
    print(ss.get_customer_who_bought_most_products())
    print(ss.get_customer_who_spent_most_money())
    print(ss.get_statistics_about_products())
```


## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/new-feature`)
3. Commit your Changes (`git commit -m 'Add some new-feature'`)
4. Push to the Branch (`git push origin feature/new-feature`)
5. Open a Pull Request


## License
Distributed under the MIT License. See `LICENSE.txt` for more information.


## Contact
Szymon Frączek - szymoon09@gmail.com
