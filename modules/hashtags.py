import instaloader
from dotenv import load_dotenv
import os
import re

# Cargar variables de entorno
load_dotenv()

def extract_bio_hashtags(username: str) -> dict:
    try:
        L = instaloader.Instaloader()
        L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        profile = instaloader.Profile.from_username(L.context, username)
        bio = profile.biography

        # Buscar hashtags con expresión regular
        hashtags = re.findall(r"#(\w+)", bio)

        if not hashtags:
            return {
                "success": False,
                "message": "⚠️ No se encontraron hashtags en la biografía."
            }

        return {
            "success": True,
            "count": len(hashtags),
            "hashtags": hashtags
        }

    except Exception as e:
        return {
            "error": f"❌ Error al extraer hashtags: {str(e)}"
        }

