import flet as ft
import asyncio
import threading

def main(page: ft.Page):
    page.title = "Server Cloner"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Input Fields
    token_input = ft.TextField(label="Discord Token", password=True, can_reveal_password=True)
    source_id = ft.TextField(label="Source Server ID")
    target_id = ft.TextField(label="Target Server ID")
    
    # Status Text
    status_text = ft.Text("Ready to Clone", color="blue")

    def start_clone(e):
        # This is where you would call your discord.py logic
        status_text.value = f"Cloning from {source_id.value}..."
        status_text.color = "yellow"
        page.update()
        
        # Here you would start your Discord script in a thread
        print(f"Token: {token_input.value}")

    # UI Layout
    page.add(
        ft.Column(
            [
                ft.Text("Discord Server Cloner", size=30, weight="bold"),
                token_input,
                source_id,
                target_id,
                ft.ElevatedButton("Start Cloning", on_click=start_clone),
                status_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Change the very last line from:
# ft.app(target=main)

# To this:
if __name__ == "__main__":
    ft.run(main)