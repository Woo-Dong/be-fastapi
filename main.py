
from dataclasses import asdict 
from typing import Optional 

import uvicorn 
from fastapi import FastAPI 

from app.database.conn import db 
from app.common.config import conf 
# from app.routes import index, auth

def create_app(): 

    
    app = FastAPI() 
    
    cnf = conf() 
    conf_dict = asdict(cnf) 
    db.init_app(app, **conf_dict) 



    # Database Initialization 

    # Redis Initalization 

    # MiddleWare Definition

    # Router Definition 

    return app 


app = create_app() 

if __name__ == "__main__": 
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

