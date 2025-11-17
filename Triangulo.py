import math
import tkinter as tk
from tkinter import messagebox

# --- FUNÇÕES DE LÓGICA ---


def limpar_campos():
    """Limpa todos os campos de entrada e o rótulo de resultado."""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)

    # Limpa e reseta a formatação do rótulo de resultado
    label_resultado.config(text="", fg="black", font=("Arial", 11))


def calcular():
    """Calcula o perímetro e a área usando a Fórmula de Heron."""
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # 1. Validação de lados positivos
        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Erro", "Os lados devem ser números positivos.")
            return

        # 2. Condição de Existência do Triângulo
        if a + b <= c or a + c <= b or b + c <= a:
            messagebox.showerror(
                "Erro",
                "Os lados informados não formam um triângulo válido. A soma de dois lados deve ser maior que o terceiro.",
            )
            return

        # Cálculo do Perímetro e Área (Fórmula de Heron)
        perimetro = a + b + c
        s = perimetro / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))

        # Exibe o resultado com formatação de sucesso
        label_resultado.config(
            text=f"✅ Sucesso!\nPerímetro: {perimetro:.2f}\nÁrea: {area:.2f}",
            fg="darkgreen",
            font=("Arial", 11, "bold"),
        )

    except ValueError:
        messagebox.showerror(
            "Erro", "Por favor, insira apenas números válidos (ex: 3, 4, 5)."
        )


# --- ESTRUTURA DA INTERFACE ---


def configurar_interface():
    # Variáveis globais para os widgets de entrada e saída
    global entry_a, entry_b, entry_c, label_resultado

    janela = tk.Tk()
    janela.title("Calculadora de Triângulo (Heron)")
    janela.minsize(350, 310)
    janela.resizable(True, False)

    # Título
    titulo = tk.Label(
        janela, text="📐 Área e Perímetro do Triângulo", font=("Arial", 14, "bold")
    )
    titulo.pack(pady=15)

    # Entradas de Dados
    frame_inputs = tk.Frame(janela)
    frame_inputs.pack(pady=5, padx=20)

    # Lado A
    tk.Label(frame_inputs, text="Lado A:", width=8, anchor="w").grid(
        row=0, column=0, padx=5, pady=5, sticky="w"
    )
    entry_a = tk.Entry(frame_inputs, width=25)
    entry_a.grid(row=0, column=1)

    # Lado B
    tk.Label(frame_inputs, text="Lado B:", width=8, anchor="w").grid(
        row=1, column=0, padx=5, pady=5, sticky="w"
    )
    entry_b = tk.Entry(frame_inputs, width=25)
    entry_b.grid(row=1, column=1)

    # Lado C
    tk.Label(frame_inputs, text="Lado C:", width=8, anchor="w").grid(
        row=2, column=0, padx=5, pady=5, sticky="w"
    )
    entry_c = tk.Entry(frame_inputs, width=25)
    entry_c.grid(row=2, column=1)

    # Frame para os Botões
    frame_botoes = tk.Frame(janela)
    frame_botoes.pack(pady=15)

    # Botão Calcular
    botao_calcular = tk.Button(
        frame_botoes,
        text="Calcular",
        command=calcular,
        bg="#2E8B57",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5,
    )
    botao_calcular.pack(side=tk.LEFT, padx=10)  # Alinha à esquerda

    # NOVO: Botão Limpar
    botao_limpar = tk.Button(
        frame_botoes,
        text="Limpar",
        command=limpar_campos,
        bg="#FF6347",
        fg="white",
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5,
    )
    botao_limpar.pack(
        side=tk.LEFT, padx=10
    )  # Alinha à esquerda, lado a lado com o Calcular

    # Resultado
    label_resultado = tk.Label(janela, text="", font=("Arial", 11))
    label_resultado.pack(pady=10)

    janela.mainloop()


if __name__ == "__main__":
    configurar_interface()
