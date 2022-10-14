# Restaurant App backend API
### Django, Django rest framework


## Features

- Restaurant Menu items view, create, update, delete
- Menu item order, order status update, order delete
- User authentication using **simple JWT token**
- New user registration, password change

Restaurant app api using **Django , Django rest framework**, user can view menu items and create new order after register on the app and administrator/stuff user can modify menu, modify order status using the app api.


## API end point

#### _User / Authentication_
| METHOD | EndPoint | Feature | ACCESS |
| ------ | ------ | ------ | ------ |
| _POST_ |  `/backend/api/v1/user/reg/` | _Register New User_ | _All Users_ |
| _POST_ |  `/backend/api/v1/user/login/` | _Login User_ | _All Users_ |
| _POST_ |  `/backend/api/v1/user/token/refresh/` | _Refresh the access token_ | _All Users_ |
| _POST_ |  `/backend/api/v1/user/change-password/` | _User password change_ | _Authentication Required_ |
| _POST_ |  `/backend/api/v1/user/logout/` | _User Logout_ | _All Users_ |

#### _Restaurant Menu_
| METHOD | EndPoint | Feature | ACCESS |
| ------ | ------ | ------ | ------ |
| _GET_ |  `/backend/api/v1/menu/` | _View all Menu items_ | _All Users_ |
| _POST_ |  `/backend/api/v1/menu/` | _Create a New Menu item_ | _Staff User_ |
| _PUT_ |  `/backend/api/v1/menu/{menu_id}` | _Update a Menu item_ | _Staff User_ |
| _DELETE_ |  `/backend/api/v1/menu/{menu_id}` | _Delete a Menu item_ | _Staff User_ |

#### _Restaurant Order_
| METHOD | EndPoint | Feature | ACCESS |
| ------ | ------ | ------ | ------ |
| _GET_ |  `/backend/api/v1/order/` | _View all Orders_ | _Staff User_ |
| _POST_ |  `/backend/api/v1/order/` | _Create a New Order_ | _Authentication Required_ |
| _GET_ |  `/backend/api/v1/order/{order_id}` | _Retrieve an order_ | _Authentication Required_   |
| _PUT_ |  `/backend/api/v1/order/{order_id}` | _Update an order status_ | _Staff User_ |
| _DELETE_ |  `/backend/api/v1/order/{order_id}` | _Delete an order_ | _Staff User_ |

#### _View full API Documentation_
| METHOD | EndPoint | Feature | ACCESS |
| ------ | ------ | ------ | ------ |
| _GET_ |  `/docs/` | _View Full API documentation_ | _All Users_ |

## How to run the Project

- Install Python
- Git clone the project
- Create your virtualenv
- Install the requirements with `pip install -r requirements.txt`
- Create you database with `python manage.py makemigrations` & `python manage.py migrate`
- Finally run ``` python manage.py runserver ```

**Thanks a lot!**
