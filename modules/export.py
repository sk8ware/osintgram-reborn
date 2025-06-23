import os
import json

def export_data(username: str, data: dict, format: str = "txt") -> dict:
    try:
        os.makedirs("exports", exist_ok=True)
        filename = f"exports/{username}.{format}"

        if format == "json":
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        elif format == "txt":
            with open(filename, "w", encoding="utf-8") as f:
                for key, value in data.items():
                    f.write(f"{key}: {value}\n")
        else:
            return {"error": "Formato no soportado. Usa 'txt' o 'json'."}

        return {"success": True, "file": filename}
    except Exception as e:
        return {"error": str(e)}

