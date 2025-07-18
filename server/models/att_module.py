from  beanie import Document,Link 
from enum import Enum
from models.generals import TimeStamps
from pydantic import  BaseModel
from datetime import datetime     
from typing import TYPE_CHECKING,Optional,List
from models.organization import Organization
if TYPE_CHECKING: # type: ignore
    from models.user import User
    from models.group import Group
class days (Enum):
    mon = "mon"
    tue = "tue" 
    wed = "wed" 
    thu = "thu"
    fri = "fri" 
    sat = "sat" 
    sun = "sun" 

class attendance_frequency (Enum): 
    daily = "daily" 
    custom = "custom"

class Group_to_User (BaseModel):
    group : Link["Group"]
    users :  List[Link["User"]]

class attendance_module(Document,TimeStamps):
    name:str
    description:Optional[str] 

    groups: List[Link["Group"]]
    
    frequency: attendance_frequency 

    organization_id : Link["Organization"]

    # Assign User to take attendance
    groups_to_user : List[Group_to_User]  
    

    is_active:bool = True 
    end_date : Optional[datetime]

