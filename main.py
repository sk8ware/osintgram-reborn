from modules.profile import get_profile_info
from modules.followers import get_followers
from modules.profile_pic import download_profile_pic
from modules.posts import download_posts
from modules.stories import download_stories
from modules.hashtags import extract_bio_hashtags
from modules.export import export_data
from utils.banner import print_banner
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def horizontal_rule() -> None:
    console.print("[green]" + "─" * 60 + "[/green]")

def show_profile(info: dict) -> None:
    table = Table(title="📌 Información del perfil", show_lines=True, header_style="bold magenta")
    table.add_column("Campo", style="cyan", no_wrap=True, justify="right")
    table.add_column("Valor", style="white")
    for key, value in info.items():
        if isinstance(value, bool):
            value = "[green]✅ Yes[/green]" if value else "[red]❌ No[/red]"
        table.add_row(key, str(value))
    console.print(table)

def show_followers(followers: list) -> None:
    table = Table(title="👥 Lista de Seguidores (máximo 20)", show_lines=True, header_style="bold yellow")
    table.add_column("#", style="cyan", justify="center")
    table.add_column("Usuario", style="white")
    for i, user in enumerate(followers[:20]):
        table.add_row(str(i + 1), user)
    console.print(table)

def main() -> None:
    print_banner("ascii")
    try:
        while True:
            console.print("\n[bold blue]Seleccione una opción:[/]")
            console.print("[cyan][1][/cyan] Obtener información del perfil")
            console.print("[cyan][2][/cyan] Listar seguidores")
            console.print("[cyan][3][/cyan] Descargar foto de perfil en HD")
            console.print("[cyan][4][/cyan] Descargar publicaciones y metadatos")
            console.print("[cyan][5][/cyan] Descargar stories disponibles")
            console.print("[cyan][6][/cyan] Extraer hashtags de la biografía")
            console.print("[cyan][7][/cyan] Exportar resultados a TXT/JSON")
            console.print("[cyan][0][/cyan] Salir")
            console.print("\n[bold cyan]Opción > [/bold cyan]", end="")
            option = input().strip()

            if option == "0":
                break

            if option not in ["1", "2", "3", "4", "5", "6", "7"]:
                console.print("[red]⚠️  Opción inválida.[/red]")
                continue

            console.print("\n[bold cyan]Ingrese username:[/] ", end="")
            username = input().strip()
            if not username:
                console.print("[red]⚠️  Debes ingresar un usuario válido.[/red]")
                continue

            if option == "1":
                info = get_profile_info(username)
                console.print("\n[bold green]📄 Perfil encontrado:[/]")
                show_profile(info)

            elif option == "2":
                result = get_followers(username)
                if "error" in result:
                    console.print(f"\n[red]{result['error']}[/red]\n")
                else:
                    console.print(f"\n[bold blue]👥 Seguidores encontrados: {result['count']}[/bold blue]\n")
                    show_followers(result['followers'])

            elif option == "3":
                console.print("\n[bold yellow]⚙️ Descargando foto de perfil HD...[/bold yellow]")
                download_profile_pic(username)

            elif option == "4":
                console.print("\n[bold yellow]⚙️ Descargando publicaciones...[/bold yellow]")
                download_posts(username)

            elif option == "5":
                console.print("\n[bold yellow]⚙️ Descargando stories...[/bold yellow]")
                download_stories(username)

            elif option == "6":
                console.print("\n[bold yellow]⚙️ Extrayendo hashtags...[/bold yellow]")
                extract_bio_hashtags(username)

            elif option == "7":
                console.print("\n[bold yellow]⚙️ Exportando datos...[/bold yellow]")
                export_data(username)

            horizontal_rule()

    except KeyboardInterrupt:
        console.print()
        horizontal_rule()
        console.print(
            Panel(
                "Hack the world 🧠💀",
                title="👋 Hasta pronto",
                subtitle="Osintgram-Reborn",
                style="bold purple",
            )
        )
        horizontal_rule()
        console.print()
        exit(0)

if __name__ == "__main__":
    main()

