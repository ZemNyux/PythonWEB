import tkinter as tk
from tkinter import messagebox

def analyze_profile():
    name = entry_name.get()

    try:
        raw_matches = entry_matches.get().split(",")
        matches = []
        for m in raw_matches:
            matches.append(int(m.strip()))

        total_games = len(matches)
        avg_score = sum(matches) / total_games if total_games > 0 else 0
        best_score = max(matches) if total_games > 0 else 0
        worst_score = min(matches) if total_games > 0 else 0

        player_profile = {
            "nickname": name,
            "stats": {
                "matches_played": total_games,
                "average_score": round(avg_score, 2),
                "max_score": best_score,
                "min_score": worst_score
            },
            "status": "Молодец! Ты крутой пацан!" if avg_score >= 7 else "К сожалению, пересдача((("
        }

        result_text = (
            f"Игрок: {player_profile['nickname']}\n"
            f"Всего матчей: {total_games}\n"
            f"Средний балл: {player_profile['stats']['average_score']}\n"
            f"Итог: {player_profile['status']}"
        )
        lbl_result.config(text=result_text, fg="#00ffcc")

        try:
            filename = f"{name}_profile_report.txt"
            file = open(filename, "w", encoding="utf8")
            file.write(f"=== PROFILE REPORT ===\n")
            file.write(f"Nickname: {player_profile['nickname']}\n")
            file.write(f"Matches: {matches}\n")
            file.write(f"Average: {player_profile['stats']['average_score']}\n")
            file.write(f"Status: {player_profile['status']}\n")
            file.close()

            messagebox.showinfo("Успех", f"Отчет успешно сохранен в файл:\n{filename}")
        except Exception as file_error:
            print(f"Случилось ошибочка в файле: {file_error}")

    except ValueError:
        messagebox.showerror("Ошибка", "Введи корректные числа через запятую в поле матчей!")

root = tk.Tk()
root.title("Nikita's Profile & Stats Analyzer")
root.geometry("450x450")
root.config(bg="#1e1e1e")

# Заголовок
lbl_title = tk.Label(root, text="Game Profile & Stats Analyzer", bg="#1e1e1e", fg="#ffffff",
                     font=("Arial", 14, "bold"))
lbl_title.pack(pady=15)

lbl_name = tk.Label(root, text="Никнейм игрока:", bg="#1e1e1e", fg="#cccccc", font=("Arial", 11))
lbl_name.pack(anchor="w", padx=40)

entry_name = tk.Entry(root, font=("Arial", 11), width=30)
entry_name.pack(anchor="w", padx=40, pady=5)
entry_name.insert(0, "Nikita")

lbl_matches = tk.Label(root, text="Результаты матчей/оценки, через запятую:", bg="#1e1e1e", fg="#cccccc",
                       font=("Arial", 11))
lbl_matches.pack(anchor="w", padx=40, pady=(10, 0))

entry_matches = tk.Entry(root, font=("Arial", 11), width=30)
entry_matches.pack(anchor="w", padx=40, pady=5)
entry_matches.insert(0, "8, 9, 7, 10, 6")

btn_analyze = tk.Label()
btn_run = tk.Button(root, text="Анализировать и записать в файл", command=analyze_profile, bg="#007acc", fg="#ffffff",
                    font=("Arial", 11, "bold"), padx=10, pady=5)
btn_run.pack(pady=20)

lbl_result = tk.Label(root, text="Ожидание данных...", bg="#1e1e1e", fg="#888888", font=("Arial", 10), justify="left")
lbl_result.pack(padx=40, pady=10)

root.mainloop()