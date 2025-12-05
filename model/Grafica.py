import matplotlib.pyplot as plt

def grafica(Pwf, Qo):
    fig = plt.figure(figsize=(8, 6))  # tamaño opcional
    ax = fig.add_subplot(111)
    ax.plot(Qo, Pwf, marker='o', color='b', linewidth=2)
    # Etiquetas y título
    ax.set_title("Curva IPR - yacimiento Saturado", fontsize=14)
    ax.set_ylabel("Presión de fondo fluyente Pwf (psi)", fontsize=12)
    ax.set_xlabel("Tasa de producción Q (bbl/día)", fontsize=12)
    # Cuadrícula y visualización
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    return fig
