import tkinter as tk
from tkinter import messagebox
import math

# Função para calcular área e perímetro
def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror("Erro", "Os lados informados não formam um triângulo válido.")
            return
        perimetro = a + b + c

        # Calcula área (fórmula de Heron)
        s = perimetro / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        
        label_resultado.config(
            text=f"Perímetro: {perimetro:.2f}\nÁrea: {area:.2f}"
        )

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira apenas números válidos.")

# Janela principal
janela = tk.Tk()
janela.title("Calculadora de Triângulo")
janela.geometry("300x280")
janela.resizable(False, False)

# Título
titulo = tk.Label(janela, text="Área e Perímetro do Triângulo", font=("Arial", 12, "bold"))
titulo.pack(pady=10)

# Entradas 
frame_inputs = tk.Frame(janela)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Lado A:").grid(row=0, column=0, padx=5, pady=5)
entry_a = tk.Entry(frame_inputs, width=10)
entry_a.grid(row=0, column=1)

tk.Label(frame_inputs, text="Lado B:").grid(row=1, column=0, padx=5, pady=5)
entry_b = tk.Entry(frame_inputs, width=10)
entry_b.grid(row=1, column=1)

tk.Label(frame_inputs, text="Lado C:").grid(row=2, column=0, padx=5, pady=5)
entry_c = tk.Entry(frame_inputs, width=10)
entry_c.grid(row=2, column=1)

# Botão 
botao = tk.Button(janela, text="Calcular", command=calcular, bg="#0078D7", fg="white", font=("Arial", 10, "bold"))
botao.pack(pady=10)

# Resultado
label_resultado = tk.Label(janela, text="", font=("Arial", 11))
label_resultado.pack(pady=10)

# Inicia a interface
janela.mainloop()
