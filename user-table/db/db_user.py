from fastapi import HTTPException
from sqlalchemy.orm import Session
from db.models import DbUser
from db.hash import Hash  # Assuming this is your password hasher
from schemas import UserBase  # Replace with your actual schema

def create_student(db: Session, request: UserBase):
    # Validate phone number is all digits
    if not request.phonenumber.isdigit():
        raise HTTPException(
            status_code=422,
            detail="Phone number must contain digits only."
        )
 
    # Check if email or phone number already exists
    existing_user = db.query(DbUser).filter(
        (DbUser.email == request.email) | 
        (DbUser.phonenumber == request.phonenumber)
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="User with this email or phone number already exists."
        )

    # Create and save new user
    new_user = DbUser(
        username=request.username,
        email=request.email,
        phonenumber=request.phonenumber,
        password=Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get the all users
def get_all_users(db: Session):
    return db.query(DbUser).all()
    
#get the id based user
def get_user(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()

#Update the User
def update_user(db: Session, id: int, request):
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.username = request.username
    user.email = request.email
    user.phonenumber = request.phonenumber
    user.password = Hash.bcrypt(request.password)

    db.commit()
    db.refresh(user)
    return user

# def delete_user(db: Session, id: int):
#   user = db.query(DbUser).filter(DbUser.id == id).first()
#   db.delete(user)
#   db.commit()
#   return 'ok'

def delete_user(db: Session, id: int):
    user = db.query(DbUser).filter(DbUser.id == id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}










#########################################################################################

# def update_user(db: Session, id: int, request: UserBase):
#   user = db.query(DbUser).filter(DbUser.id == id)

#   if not user:
#         raise HTTPException(status_code=404, detail="User not found")
  
#   user.update({
#     DbUser.username: request.username,
#     DbUser.email: request.email,
#     DbUser.phonenumber: request.phonenumber,
#     DbUser.password: Hash.bcrypt(request.password)
#   })
#   db.commit()
#   return 'ok'