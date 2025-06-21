from instaloader import Instaloader, Profile
from dotenv import load_dotenv
import os

# Carga las variables del archivo .env
load_dotenv()
IG_USERNAME = os.getenv("IG_USERNAME")
IG_PASSWORD = os.getenv("IG_PASSWORD")

def get_followers(username):
    try:
        loader = Instaloader()

        # Login con la cuenta dummy
        loader.login(IG_USERNAME, IG_PASSWORD)

        profile = Profile.from_username(loader.context, username)

        if profile.is_private:
            return {
                "error": "❌ El perfil es privado. No se pueden listar los seguidores."
            }

        followers = []
        for follower in profile.get_followers():
            followers.append(follower.username)

        return {
            "count": len(followers),
            "followers": followers
        }

    except Exception as e:
        return {
            "error": f"❌ Error al obtener seguidores: {str(e)}"
        }

