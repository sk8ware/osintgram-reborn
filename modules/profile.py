import instaloader

def get_profile_info(username):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, username)

    return {
        "username": profile.username,
        "fullname": profile.full_name,
        "bio": profile.biography,
        "followers": profile.followers,
        "following": profile.followees,
        "is_private": profile.is_private,
    }
