from fastapi import APIRouter
from fastapi import Request
from fastapi.responses import JSONResponse
import databaseManager.eventActions as eventActions
import os


router = APIRouter()


@router.put("/jammer/activate")
def jammerArtivate(request: Request):
    os.system("touch /jammerActivated")
    eventActions.editRedirectID("/Database/Database.db", "12001", "12003")
    eventActions.editRedirectID("/Database/Database.db", "12101", "12103")
    return JSONResponse({
        "status": 200,
        "message": "Jammer activated"
    })


@router.put("/jammer/deactivate")
def jammerDeactivate(request: Request):
    os.system("rm /jammerActivated")
    eventActions.editRedirectID("/Database/Database.db", "12001", "12002")
    eventActions.editRedirectID("/Database/Database.db", "12101", "12102")
    return JSONResponse({
        "status": 200,
        "message": "Jammer deactivated"
    })


@router.get("/jammer/activated")
def jammerActivated(request: Request):
    if os.path.exists("/jammerActivated"):
        return JSONResponse({
            "status": 200,
            "message": "Jammer activated",
            "activated": 1
        })
    return JSONResponse({
        "status": 200,
        "message": "Jammer deactivated",
        "activated": 0
    })
