import os
import json
import instaloader
from openai import OpenAI
from rich.console import Console

console = Console()

# Configura cliente OpenAI solo si existe la API KEY
API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=API_KEY) if API_KEY else None

def get_profile_info(username):
    try:
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
    except Exception as e:
        console.print(f"[red]❌ Error al obtener datos del perfil: {e}[/red]")
        return {}

def analyze_profile_with_ia(username: str) -> None:
    filepath = f"outputs/ai_summary_{username}.txt"

    profile_data = get_profile_info(username)

    if not profile_data:
        console.print("[red]⚠️ No se pudo obtener información del perfil.[/red]")
        return

    if not client:
        console.print("[yellow]⚠️ La API de OpenAI no está configurada. Análisis con IA desactivado.[/yellow]")
        return

    prompt = f"""
Eres un analista digital experto en OSINT. A continuación se proporciona la información pública extraída de un perfil de Instagram. Elabora un informe técnico y detallado que cubra:

1. Perfil de usuario y exposición pública
2. Posibles intereses o comportamientos inferidos
3. Nivel de privacidad y visibilidad de datos sensibles
4. Nivel de riesgo digital (0 a 100)
5. Recomendaciones para mejorar la seguridad del perfil

Información extraída del perfil (@{username}):
{json.dumps(profile_data, indent=2, ensure_ascii=False)}
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.5
        )
        summary = response.choices[0].message.content
        console.print(f"\n[bold green]📄 Análisis generado por IA:[/bold green]\n{summary}")

        os.makedirs("outputs", exist_ok=True)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(summary)

    except Exception as e:
        console.print(f"[red]❌ Error durante el análisis IA: {e}[/red]")

def chat_with_openai(username: str) -> None:
    analyze_profile_with_ia(username)

