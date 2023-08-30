from ..model.customers import Customer
from flask import request, jsonify

class CustomerController:
    @classmethod
    def create_customer(cls):
        customer = Customer(
            first_name=request.args.get('first_name', ''),
            last_name=request.args.get('last_name', ''),
            phone=request.args.get('phone', ''),
            email=request.args.get('email', ''),
            street=request.args.get('street', ''),
            city=request.args.get('city', ''),
            state=request.args.get('state', ''),
            zip_code=request.args.get('zip_code', '')
        )

        Customer.create_customer(customer)
        return {'message': 'Customer creado con éxito'}, 200
    
    @classmethod
    def get_customer(cls, customer_id):
        customer_instance = Customer.get_customer(customer_id)
        
        if customer_instance:
            response_data = {
                "id": customer_instance.customer_id,
                "nombre": customer_instance.first_name,
                "apellido": customer_instance.last_name,
                "teléfono": customer_instance.phone,
                "correo": customer_instance.email,
                "calle": customer_instance.street,
                "ciudad": customer_instance.city,
                "estado": customer_instance.state,
                "código_postal": customer_instance.zip_code
            }
            
            return jsonify(response_data), 200
        
        else:
            return {"msg": "No se encontró el cliente"}, 404
    
    @classmethod
    def get_all_customers(cls):
        query_params = request.args.to_dict()
        customers = Customer.get_all_customers(query_params)
        
        if customers:
            response_data = {
                "customers": [{
                    "customer_id": customer.customer_id,
                    "first_name": customer.first_name,
                    "last_name": customer.last_name,
                    "phone": customer.phone,
                    "email": customer.email,
                    "street": customer.street,
                    "city": customer.city,
                    "state": customer.state,
                    "zip_code": customer.zip_code
                } for customer in customers],
                "total": len(customers)
            }
            
            return jsonify(response_data), 200
        else:
            return {"msg": "No se encontraron clientes", "total": 0}, 404
        
    @classmethod
    def update_customer(cls, customer_id):
        customer_instance = Customer.get_customer(customer_id)

        if not customer_instance:
            return {"msg": "No se encontró el cliente"}, 404

        updated_data = {
            "first_name": request.json.get('first_name', customer_instance.first_name),
            "last_name": request.json.get('last_name', customer_instance.last_name),
            "phone": request.json.get('phone', customer_instance.phone),
            "email": request.json.get('email', customer_instance.email),
            "street": request.json.get('street', customer_instance.street),
            "city": request.json.get('city', customer_instance.city),
            "state": request.json.get('state', customer_instance.state),
            "zip_code": request.json.get('zip_code', customer_instance.zip_code)
        }
        
        Customer.update_customer(customer_id, updated_data)
        return {'message': 'Cliente actualizado con éxito'}, 200

    @classmethod
    def delete_customer(cls, customer_id):
        deleted = Customer.delete_customer(customer_id)

        if deleted:
            return {'message': 'Cliente eliminado con éxito'}, 200
        else:
            return {"msg": "No se encontró el cliente"}, 404

    




    
    # @classmethod
    # def get_actors(self):
    #     results = Actor.get_actors
    #     actors = []
    #     for result in results:
    #         actors.append({
    #             "id": result[0],
    #             "nombre": result[1],
    #             "apellido": result[2],
    #             "ultima_actualizacion": result[3]
    #     })
    #     return actors, 200
        

    # @classmethod
    # def update_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actor(self, actor):
    # #Implementación del método
    #     pass

    # @classmethod
    # def delete_actors(self):
    # #Implementación del método
    #     pass