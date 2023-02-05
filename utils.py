
def user_to_dict(raw_data):
    return {
        "id": raw_data.id,
        "first_name": raw_data.first_name,
        "last_name": raw_data.last_name,
        "age": raw_data.age,
        "email": raw_data.email,
        "role": raw_data.role,
        "phone": raw_data.phone
    }


def order_to_dict(data):
    return {
        "id": data.id,
        "name": data.name,
        "description": data.description,
        "start_date": data.start_date,
        "end_date": data.end_date,
        "address": data.address,
        "price": data.price,
        "customer_id": data.customer_id,
        "executor_id": data.executor_id
    }


def offers_to_dict(data):
    return {
        "id": data.id,
        "order_id": data.order_id,
        "executor_id": data.executor_id
    }


