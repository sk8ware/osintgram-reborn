from modules.profile import get_profile_info
from modules.followers import get_followers
from utils.banner import print_banner
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def horizontal_rule() -> None:
    """Imprime una línea horizontal verde."""
    console.print("[green]" + "─" * 60 + "[/green]")

def show_profile(info: dict) -> None:
    """Muestra la información del perfil en una tabla bonita."""
    table = Table(title="📌 Información del perfil",
                  show_lines=True,
                  header_style="bold magenta")

    table.add_column("Campo", style="cyan", no_wrap=True, justify="right")
    table.add_column("Valor", style="white")

    for key, value in info.items():
        if isinstance(value, bool):
            value = "[green]✅ Yes[/green]" if value else "[red]❌ No[/red]"
        table.add_row(key, str(value))

    console.print(table)

def show_followers(followers: list) -> None:
    """Muestra los seguidores en una tabla."""
    table = Table(title="👥 Lista de Seguidores (máximo 20)",
                  show_lines=True,
                  header_style="bold yellow")

    table.add_column("#", style="cyan", justify="center")
    table.add_column("Usuario", style="white")

    for i, user in enumerate(followers[:20]):
        table.add_row(str(i + 1), user)

    console.print(table)

def main() -> None:
    print_banner("ascii")

    try:
        while True:
            console.print("\n[bold cyan]Ingrese username:[/] ", end="")
            username = input().strip()

            if not username:
                console.print("[red]⚠️  Debes ingresar un usuario válido.[/]")
                continue

            info = get_profile_info(username)
            console.print("\n[bold green]📄 Perfil encontrado:[/]\n")
            show_profile(info)
            horizontal_rule()

            choice = input("\n¿Deseas listar los seguidores? (s/n): ").lower()
            if choice == "s":
                result = get_followers(username)
                if "error" in result:
                    console.print(f"\n[red]{result['error']}[/red]\n")
                else:
                    console.print(f"\n[bold blue]👥 Seguidores encontrados: {result['count']}[/bold blue]\n")
                    show_followers(result['followers'])

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

