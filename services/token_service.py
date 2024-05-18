from services.db_service import user_dao


def add_token_to_blacklist(token: str):
    user_dao.blacklist_token(token)


def check_if_token_is_blacklisted(token: str) -> bool:
    return user_dao.is_token_blacklisted(token)
