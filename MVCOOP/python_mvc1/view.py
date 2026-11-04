from python_mvc1.model import Task

class ConsoleView:

    @staticmethod
    def show_tasks(tasks: list[Task]):
        if not tasks:
            print("\n📌 [Список пуст] Задач пока нет. Самое время добавить!\n")
            return

        print("\n📋 ТВОЙ СПИСОК ЗАДАЧ:")
        print("=" * 30)
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")
        print("=" * 30 + "\n")

    @staticmethod
    def show_menu():
        print("✨ МЕНЮ УПРАВЛЕНИЯ ЗАДАЧАМИ ✨")
        print("  [1] ➕ Добавить новую задачу")
        print("  [2] 👀 Показать все задачи")
        print("  [3] ✅ Отметить как выполненную")
        print("  [4] 🗑️ Удалить задачу")
        print("  [0] 🚪 Выход из программы")
        print()

    @staticmethod
    def get_choice() -> str:
        return input("👉 Выбери действие (0-4): ").strip()

    @staticmethod
    def get_task_description() -> str:
        return input("✍️ Введите суть задачи: ").strip()

    @staticmethod
    def get_task_number(prompt: str) -> str:
        # Сохраняем кастомный промпт от контроллера, но добавляем иконку
        return input(f"🔢 {prompt}").strip()

    @staticmethod
    def show_message(msg: str):
        print(f"\n💡 СИСТЕМНОЕ СООБЩЕНИЕ: {msg}\n")