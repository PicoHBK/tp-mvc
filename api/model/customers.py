from ..database import DatabaseConnection

class Customer:
    def __init__(self, customer_id=None, first_name=None, last_name=None, phone=None, email=None, street=None, city=None, state=None, zip_code=None):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code

    @classmethod
    def create_customer(cls, customer):
        query = "INSERT INTO sales.customers (first_name, last_name, phone, email, street, city, state, zip_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        params = (customer.first_name, customer.last_name, customer.phone, customer.email, customer.street, customer.city, customer.state, customer.zip_code)
        DatabaseConnection.execute_query(query, params)
        DatabaseConnection.close_connection()

    @classmethod
    def get_customer(cls, customer_id):
        query = "SELECT first_name, last_name, phone, email, street, city, state, zip_code FROM sales.customers WHERE customer_id = %s;"
        params = (customer_id,)
        result = DatabaseConnection.fetch_one(query, params)
        DatabaseConnection.close_connection()
        
        if result is not None:
            return Customer(
                customer_id=customer_id,
                first_name=result[0],
                last_name=result[1],
                phone=result[2],
                email=result[3],
                street=result[4],
                city=result[5],
                state=result[6],
                zip_code=result[7]
            )
        else:
            return None
        
    @classmethod
    def get_all_customers(cls, query_params=None):
        query = "SELECT customer_id, first_name, last_name, phone, email, street, city, state, zip_code FROM sales.customers"
        params = ()

        if query_params:
            query += " WHERE " + " AND ".join(f"{key} = %s" for key in query_params.keys())
            params = tuple(query_params.values())

        results = DatabaseConnection.fetch_all(query, params)
        DatabaseConnection.close_connection()
        customers = []

        for result in results:
            customer = Customer(
                customer_id=result[0],
                first_name=result[1],
                last_name=result[2],
                phone=result[3],
                email=result[4],
                street=result[5],
                city=result[6],
                state=result[7],
                zip_code=result[8]
            )
            customers.append(customer)

        return customers
    
    @classmethod
    def update_customer(cls, customer_id, updated_data):
        print(updated_data)
        print(f"id {customer_id}")
        set_fields = ", ".join(f"{key} = %s" for key in updated_data.keys())
        query = f"UPDATE sales.customers SET {set_fields} WHERE customer_id = %s;"
        params = tuple(list(updated_data.values()) + [customer_id])
        DatabaseConnection.execute_query(query, params)
        DatabaseConnection.close_connection()

    @classmethod
    def delete_customer(cls, customer_id):
        try:
            customer_instance = cls.get_customer(customer_id)

            if not customer_instance:
                return False  # Cliente no encontrado

            query = "DELETE FROM sales.customers WHERE customer_id = %s;"
            params = (customer_id,)
            DatabaseConnection.execute_query(query, params)
            
            return True  # Cliente eliminado exitosamente
        finally:
            DatabaseConnection.close_connection()


