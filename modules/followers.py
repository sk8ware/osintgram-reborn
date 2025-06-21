import instaloader
import os
from dotenv import load_dotenv
from rich.console import Console

console = Console()
load_dotenv()

def login_instagram() -> instaloader.Instaloader:
    """Inicia sesión en Instagram usando Instaloader y guarda la sesión para uso futuro."""
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")
    session_file = f"{username}.session"

    L = instaloader.Instaloader()

    try:
        # Si ya hay una sesión, la carga
        L.load_session_from_file(username, session_file)
        console.print(f"[green]✅ Sesión cargada correctamente desde '{session_file}'[/green]")
    except FileNotFoundError:
        # Si no hay sesión, hace login y la guarda
        try:
            console.print("[yellow]🔐 Iniciando sesión por primera vez...[/yellow]")
            L.login(username, password)
            L.save_session_to_file(session_file)
            console.print(f"[green]✅ Sesión guardada como '{session_file}'[/green]")
        except Exception as e:
            console.print(f"[red]❌ Error en el login: {e}[/red]")
            raise e

    return L

def get_followers(target_username: str) -> dict:
    """Obtiene los seguidores de un usuario si el perfil es público."""
    try:
        L = login_instagram()
        profile = instaloader.Profile.from_username(L.context, target_username)

        followers = [f.username for f in profile.get_followers()]
        return {
            "count": len(followers),
            "followers": followers
        }

    except Exception as e:
        return {
            "error": f"❌ Error al obtener seguidores: {e}"
        }
