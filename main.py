import flet as ft
import random

def main(page: ft.Page):
    page.title = "Game Tebak Angka Pro"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    angka_rahasia = random.randint(1, 100)

    ikon_game = ft.Icon(name=ft.Icons.STADIA_CONTROLLER, size=60, color="blue")
    
    # Link gambar piala yang benar agar muncul di HP
    gambar_menang = ft.Image(
        src="https://icons8.com", 
        width=150, height=150, visible=False
    )
    
    judul = ft.Text("TEBAK ANGKA 1-100", size=28, weight="bold")
    hasil_teks = ft.Text("Coba tebak angkanya!", size=20)
    input_angka = ft.TextField(
        label="Masukkan Angka", width=200, 
        text_align="center", border_radius=15, 
        keyboard_type=ft.KeyboardType.NUMBER
    )

    def cek_tebakan(e):
        try:
            user_guess = int(input_angka.value)
            if user_guess == angka_rahasia:
                hasil_teks.value = "MENANG! 🏆"
                hasil_teks.color = "green"
                gambar_menang.visible = True
            elif user_guess < angka_rahasia:
                hasil_teks.value = "Terlalu KECIL! ⬆️"
            else:
                hasil_teks.value = "Terlalu BESAR! ⬇️"
        except:
            hasil_teks.value = "Hanya angka ya! ❌"
        input_angka.value = ""
        page.update()

    btn_tebak = ft.ElevatedButton("CEK ANGKA", on_click=cek_tebakan)
    page.add(ikon_game, judul, gambar_menang, hasil_teks, input_angka, btn_tebak)

ft.app(target=main)

