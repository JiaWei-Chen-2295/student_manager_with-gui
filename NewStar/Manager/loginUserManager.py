from NewStar.Dao.UserDao import UserDao


def loginCheck(username, pwd):
    ud = UserDao()
    user = ud.selectByUsername(username)
    if user.password == pwd:
        return True
    return False