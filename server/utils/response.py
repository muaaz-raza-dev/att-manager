from fastapi.responses import JSONResponse
from typing import TYPE_CHECKING,Any

def Respond(payload:Any=None,success:bool=True,message:str="Okay",status_code:int=200):
    return JSONResponse(
        status_code=status_code,
        content={"success": False if success != 200 else True ,"payload":payload  , "message":message}
    )