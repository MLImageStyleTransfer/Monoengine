from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/", status_code=200)
def home_view() -> Response:
    return Response("<h1> Home </h1>")


@router.get("/about", status_code=200)
def about_view() -> Response:
    return Response("<h1> About </h1>")


@router.get("/user/auth", status_code=200)
def user_auth_view() -> Response:
    return Response("<h1> User auth </h1>")


@router.get("/user/{login}", status_code=200)
def user_view(login: str) -> Response:
    return Response(f"<h1> Login: {login} </h1>")


@router.get("/default_style_img", status_code=200)
def default_style_img() -> list[str]:
    return ["a", "b", "c"]
