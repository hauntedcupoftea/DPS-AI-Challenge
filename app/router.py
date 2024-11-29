"""all fastapi routers go here"""
from fastapi import APIRouter, Depends, status, HTTPException
from app.functions import *
from app.basemodels import *

qna = APIRouter(
    prefix='/forecast',
    tags=['forecast']
)

@qna.post('/luke-skywalker-wiki', status_code=status.HTTP_200_OK, response_model=QResponse)
def api_rag_skywalker(request: QQuery):
    return luke_skywalker_rag(request, lss, llm)