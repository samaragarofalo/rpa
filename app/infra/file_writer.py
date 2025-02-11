import json
import traceback


def save_results_to_json(results: list, keywords: str) -> None:
    safe_keywords = keywords.replace(" ", "_")
    file_title = f"resultado_pesquisa_{safe_keywords}.json"

    try:
        with open(file_title, "w", encoding="utf-8") as file:
            json.dump(results, file, ensure_ascii=False, indent=4)
        print(f"Arquivo JSON salvo como: {file_title}")
    except Exception as ex:
        print("Erro ao salvar o arquivo JSON:", ex)
        print(traceback.format_exc())
