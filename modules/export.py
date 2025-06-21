import json
import os

def export_data(username: str, data: dict, format: str = "json") -> dict:
    try:
        os.makedirs("exports", exist_ok=True)
        filename = f"exports/{username}.{format.lower()}"

        if format.lower() == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        elif format.lower() == "txt":
            with open(filename, "w", encoding="utf-8") as f:
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")
        else:
            return {
                "error": "❌ Formato no soportado. Usa 'json' o 'txt'."
            }

        return {
            "success": True,
            "file": filename
        }

    except Exception as e:
        return {
            "error": f"❌ Error al exportar datos: {str(e)}"
        }

