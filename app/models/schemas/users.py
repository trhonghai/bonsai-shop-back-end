from app.models.domains import users as _users_domain


class UserSignUpIn(
    _users_domain.UserUsername, _users_domain.UserPwd
):

    class Config:
        orm_mode = True
