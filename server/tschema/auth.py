from pydantic import BaseModel ,Field
from   models.user import UserRole
from typing import TYPE_CHECKING,Optional


class PayloadRegisterOrganization(BaseModel):
    name:str = Field(...,min_length=4,max_length=8,pattren=r"^[a-zA-Z0-9\- ]+$")
    individuals_name : str =Field(...,pattren=r"^[A-Za-z]+$")
    

class PayloadRegisterAdmin(BaseModel):
    full_name:str 
    username:str 
    password:str = Field(...,min_length=8, pattren=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,20}$")
    phone:Optional[str] = Field(None,pattren=r"^\+?[1-9]\d{1,14}$")   # E.164 format for phone numbers
    role : UserRole=UserRole.admin 
    email:str

class PayloadLogin(BaseModel):
    username:str
    password:str
    

class PayloadRegisterUserManual(BaseModel):
    full_name:str 
    username:str 
    password:str = Field(...,min_length=8, pattren=r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,20}$")  
    email:str
    phone:Optional[str] = Field(...,pattren=r"^\+?[1-9]\d{1,14}$")  # E.164 format for phone numbers
    role:UserRole = UserRole.staff  # Default role is staff 

class PayloadRegisterUserAuto(PayloadRegisterUserManual):
    organization_name:str 


class PayloadApproveUser(BaseModel):
    user_id: str
    organization_id: str
    role: UserRole = UserRole.staff  # Default role is staff
    is_approved: bool = True  
