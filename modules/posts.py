import instaloader
from dotenv import load_dotenv
import os
from rich.console import Console
from rich.panel import Panel

console = Console()
load_dotenv()

def download_posts(username: str, max_posts: int = 5) -> dict:
    try:
        console.print("\n[bold cyan]⚙️ Descargando publicaciones...[/bold cyan]")

        L = instaloader.Instaloader(
            dirname_pattern=f"downloads/{username}",
            save_metadata=True,
            download_video_thumbnails=False,
            download_geotags=False,
            post_metadata_txt_pattern="{caption}"
        )

        L.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

        profile = instaloader.Profile.from_username(L.context, username)

        count = 0
        for post in profile.get_posts():
            if count >= max_posts:
                break
            L.download_post(post, target=username)
            count += 1

        if count == 0:
            console.print(Panel("No se encontraron publicaciones para este perfil.", style="bold red"))
        else:
            console.print(Panel(f"✅ Se descargaron {count} publicaciones en [green]downloads/{username}[/green]", style="bold green"))

        return {
            "success": True,
            "count": count,
            "path": f"downloads/{username}/"
        }

    except instaloader.exceptions.PrivateProfileNotFollowedException:
        return {
            "error": "❌ El perfil es privado y no lo sigues. No se puede acceder a las publicaciones."
        }

    except instaloader.exceptions.ConnectionException:
        return {
            "error": "❌ Error de conexión con Instagram. Puede que hayan bloqueado temporalmente el acceso."
        }

    except Exception as e:
        return {
            "error": f"❌ Error inesperado: {str(e)}"
        }

