# inventory-management
Inventory Management using Django Restful API 
Sure! Here’s a focused `README.md` file for your Django inventory management project:

```markdown
# Inventory Management API

This project is a RESTful API for managing inventory items, built with Django and Django REST Framework. It includes user registration, authentication via JWT, and caching using Redis.

## Features

- User registration and authentication using JWT.
- CRUD operations for inventory items.
- Redis caching for improved performance.

## Technologies Used

- Python
- Django
- Django REST Framework
- Redis
- Django REST Framework SimpleJWT

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/inventory-management.git
   cd inventory-management
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Redis is installed and running:**
   ```bash
   redis-cli ping
   ```
   You should see a response of `PONG`.

## Configuration

1. **Update Django settings:**
   Ensure the following configuration is added to `settings.py`:
   ```python
   CACHES = {
       'default': {
           'BACKEND': 'django_redis.cache.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
           'OPTIONS': {
               'CLIENT_CLASS': 'django_redis.client.DefaultClient',
           }
       }
   }
   ```

## Usage

1. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

2. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

3. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

4. **Use Postman or `curl` to interact with the API.**

## API Endpoints

### User Registration

- **Endpoint:** `/api/register/`
- **Method:** `POST`
- **Body:**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```

### Obtain JWT Token

- **Endpoint:** `/api/token/`
- **Method:** `POST`
- **Body:**
  ```json
  {
      "username": "your_username",
      "password": "your_password"
  }
  ```

### Inventory Item CRUD Operations

- **Create Item**
  - **Endpoint:** `/api/inventory/`
  - **Method:** `POST`
  - **Body:**
    ```json
    {
        "name": "Item Name",
        "quantity": 10,
        "price": 99.99
    }
    ```

- **Retrieve Items**
  - **Endpoint:** `/api/inventory/`
  - **Method:** `GET`

- **Update Item**
  - **Endpoint:** `/api/inventory/{id}/`
  - **Method:** `PUT`
  - **Body:**
    ```json
    {
        "name": "Updated Item",
        "quantity": 20,
        "price": 89.99
    }
    ```

- **Delete Item**
  - **Endpoint:** `/api/inventory/{id}/`
  - **Method:** `DELETE`



## License

This project is licensed under the MIT License.
```

### Notes:

- Replace `https://github.com/yourusername/inventory-management.git` with the actual URL of your repository.
- Feel free to modify any section to better fit your project specifics or add more details if needed. If you need anything else, just let me know!
