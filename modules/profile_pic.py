import instaloader
from dotenv import load_dotenv
import os

# Cargar variables de entorno del archivo .env
load_dotenv()

def download_profile_pic(username: str) -> dict:
    try:
        # Crear instancia de Instaloader con carpeta destino
        L = instaloader.Instaloader(
            dirname_pattern=f"downloads/{username}",
            save_metadata=False,
            download_videos=False
        )

        # Login con tus credenciales del .env
        L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        # Obtener perfil y descargar foto de perfil
        profile = instaloader.Profile.from_username(L.context, username)
        L.download_profilepic(profile)

        return {
            "success": True,
            "path": f"downloads/{username}/"
        }

    except Exception as e:
        return {
            "error": f"❌ Error al descargar la foto de perfil: {str(e)}"
        }

