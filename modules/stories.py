import instaloader
from dotenv import load_dotenv
import os

# Cargar variables de entorno
load_dotenv()

def download_stories(username: str) -> dict:
    try:
        L = instaloader.Instaloader(
            download_video_thumbnails=False,
            dirname_pattern=f"downloads/{username}_stories"
        )

        # Login con credenciales desde .env
        L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        profile = instaloader.Profile.from_username(L.context, username)
        stories = L.get_stories(userids=[profile.userid])

        count = 0
        for story in stories:
            for item in story.get_items():
                L.download_storyitem(item, f"{username}_stories")
                count += 1

        if count == 0:
            return {
                "success": False,
                "message": "⚠️ No hay stories disponibles."
            }

        return {
            "success": True,
            "count": count,
            "path": f"downloads/{username}_stories/"
        }

    except Exception as e:
        return {
            "error": f"❌ Error al descargar stories: {str(e)}"
        }

