from fastapi import APIRouter, Depends
from fullstack_challenge_api.utils.db import get_db
from sqlalchemy.orm import Session
import json

router = APIRouter()


@router.get("/companies")
async def get_companies(db: Session = Depends(get_db)):
    try:
        companies_data = db.query().all()
    except(FileNotFoundError):
        return {"msg": "no companies data available","error": FileNotFoundError}
    return {"data": companies_data}


@router.post("/companies")
async def post_companies(db: Session = Depends(get_db)):
    try:
        f = open("../../../data/challenge_companies.json", 'r')
        data = json.load(f)
        print(data)
        f.close()
        db.add_all(data)
        db.commit()
    except:
        return {"error": "File path is incorrect or data not stored successfully"}
    return {
        "msg": "Successfully stored data on DB"
    }


@router.get("/deals")
async def get_deals(db: Session = Depends(get_db)):
    try:
        deals_data = db.query().all()
    except:
        return {"msg": "no deals data available"}
    return {"data": deals_data}


@router.post("/deals")
async def post_deals(db: Session = Depends(get_db)):
    try:
        f = open("../../../data/challenge_deals.json", 'r')
        data = json.load(f)
        print(data)
        f.close()
        db.add_all(data)
        db.commit()
    except:
        return {"error": "File path is incorrect or data not stored successfully"}
    return {
        "msg": "Successfully stored data on DB"
    }


