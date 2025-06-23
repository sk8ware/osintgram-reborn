import os
import json
from openai import OpenAI
from rich.console import Console

console = Console()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chat_with_openai(username: str) -> None:
    filepath = f"outputs/ai_summary_{username}.txt"
    history = []

    # Cargar resumen anterior si existe
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            prev = f.read()
        history.append({"role": "system", "content": f"Resumen anterior del perfil {username}: {prev}"})
    else:
        history.append({"role": "system", "content": f"Quiero analizar el perfil de Instagram '{username}' con IA."})

    console.print("\n[bold cyan]Inicia tu consulta (escribe 'exit' para salir):[/bold cyan]")

    while True:
        user_input = input("\nTú: ").strip()
        if user_input.lower() == "exit":
            console.print("[bold yellow]🧠 Cerrando chat con IA...[/bold yellow]")
            break

        history.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=history,
                temperature=0.7
            )
            reply = response.choices[0].message.content
            console.print(f"\n🤖 IA: {reply}")
            history.append({"role": "assistant", "content": reply})
        except Exception as e:
            console.print(f"[red]❌ Error al consultar la IA: {e}[/red]")
            return

    # Guardar en archivo
    with open(filepath, "w", encoding="utf-8") as f:
        resumen = next((h["content"] for h in reversed(history) if h["role"] == "assistant"), "")
        f.write(resumen if resumen else "No se encontró análisis de IA previo.")

