from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def home():
    pass

@router.get("/moduls")
def moduls():
    pass

@router.get("/modul{number_modul}")
def moduls(number_modul: int):
    pass

@router.get("/modul{number_modul}-lesson{number_lesson}")
def moduls(number_modul: int, number_lesson: int):
    pass