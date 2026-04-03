from fastapi import Header, HTTPException
from fastapi import APIRouter
from src.services import add_product, get_products, add_user, create_order

router = APIRouter()

# HOME
@router.get("/")
def home():
    return {"message": "Enterprise App Running 🚀"}

# PRODUCTS
@router.get("/products")
def list_products():
    return get_products()

@router.post("/products")
def create_product(name: str, price: int):
    return add_product(name, price)

@router.post("/products")
def create_product(name: str, price: int, x_token: str = Header(...)):
    check_token(x_token)
    return add_product(name, price)

@router.post("/orders")
def order(product_id: int, user_id: int, x_token: str = Header(...)):
    check_token(x_token)
    return create_order(product_id, user_id)

def check_token(x_token: str = Header(...)):
    if x_token != "secret123":
        raise HTTPException(status_code=401, detail="Unauthorized")